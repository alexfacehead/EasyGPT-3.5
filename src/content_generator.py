from typing import Optional, Tuple
from src.utils.constants import FILE_FORMATTER, QUESTION_FIXER_PART_ONE, QUESTION_FIXER_PART_TWO,\
    CONTEXT_EXPANSION, TREE_OF_THOUGHT_MAKER_SECOND_HALF, TREE_OF_THOUGHT_MAKER_FIRST_HALF,\
        AUTOMATED_CONTEXT_CALLER
from src.chat_completion_generator import ChatCompletionGenerator
from src.utils.logging import Logger
from termcolor import colored
from src.utils.env_setup import EnvironmentSetup

logger = Logger()
env_and_flags = EnvironmentSetup()

class ContentGenerator:
    def __init__(self, prompt_num: Optional[int] = None, model: Optional[str] = None, super_charged: Optional[str] = None, default_compilation: Optional[str] = "", temperature: Optional[float] = 0.33):
        """
        Constructor for the ContentGenerator class
        
        Args:
            prompt_num (int, optional): The number of the prompt to use. Defaults to None.
            openai_api_key (str, optional): The API key for OpenAI. Defaults to None.
            model (str, optional): The model for OpenAI. Defaults to None.
            super_charged (str, optional): The super charged mode for GPT-4. Defaults to None.
            default_completion (str, optional): Defaults to nothing, but if you want a chat history, input what you'd like for querying purposes.
        """
        # Basics
        self.context_total = ""
        self.prompt_num = prompt_num
        self.openai_api_key = env_and_flags.openai_api_key
        self.model = env_and_flags.model
        self.super_charged = env_and_flags.super_charged
        self.temperature = temperature
        
        # Initialize a gpt-3.5-turbo chat completer
        self.chat_completer_big = ChatCompletionGenerator(temperature=temperature, prompt_num=prompt_num, openai_api_key=self.openai_api_key, model="gpt-4-0314", super_charged=self.super_charged)
        
        # Initialize a gpt-4-0314 chat completer (more powerful)
        self.chat_completer_small = ChatCompletionGenerator(prompt_num=prompt_num, openai_api_key=self.openai_api_key, model="gpt-3.5-turbo-16k", super_charged=self.super_charged, temperature=self.temperature)

    from typing import List, Dict

    def generate_plain_completion(self, json_file_input: List[Dict[str, str]], query: str):
        # Ensure json_file_input is not empty and is a list
        if not json_file_input or not isinstance(json_file_input, list):
            print(colored("INVALID CONVERSATION HISTORY", 'red'))
            return None

        # Get the last system and user messages from the conversation history
        last_system_message = json_file_input[-2]['content'] if len(json_file_input) > 1 else ""
        last_user_message = json_file_input[-1]['content'] if json_file_input else ""

        # Combine the last system message, last user message, and new user query into one string
        full_input_for_completion = f"{last_system_message}\n{last_user_message}\n{query}"

        # Generate a new completion using the chat_completer_small
        new_completion = self.chat_completer_small.generate_completion(env_and_flags.model, [
            {"role": "system", "content": last_system_message},
            {"role": "user", "content": last_user_message + "\n" + query}
        ])

        return new_completion

    def perfect_question(self, user_input_question: str):
        total_fixer_prompt = QUESTION_FIXER_PART_ONE + user_input_question + QUESTION_FIXER_PART_TWO
        print(colored(total_fixer_prompt, 'yellow'))
        fixed_user_input_question = self.chat_completer_big.generate_completion(env_and_flags.model, [{"role": "system", "content": total_fixer_prompt}])
        return fixed_user_input_question

    def make_initial_context(self, user_input_question: str):
        if user_input_question == "":
            print(colored("NO QUESTION PROVIDED", 'red'))
            exit(1)
        full_input_for_context = AUTOMATED_CONTEXT_CALLER + "\n\n" + user_input_question
        print(colored(full_input_for_context, 'yellow'))
        initial_context = self.chat_completer_small.generate_completion(env_and_flags.model, [{"role": "system", "content": AUTOMATED_CONTEXT_CALLER}, {"role": "user", "content": user_input_question}])
        return initial_context

    def expand_context(self, initial_context: str):
        expanded_context = self.chat_completer_small.generate_completion(env_and_flags.model, [{"role": "system", "content": CONTEXT_EXPANSION}, {"role": "user", "content": initial_context}])
        return expanded_context

    def make_tree_of_thought_final(self, expanded_context: str):
        total_system_message_input = TREE_OF_THOUGHT_MAKER_FIRST_HALF + "[CONTEXT]:\n" + expanded_context + "\n\n" + TREE_OF_THOUGHT_MAKER_SECOND_HALF
        tree_of_thought_final = self.chat_completer_big.generate_completion(env_and_flags.model, [{"role": "system", "content": total_system_message_input}])
        print(colored("Final Tree of Thought Prompt:\n", 'magenta'))
        print(colored(tree_of_thought_final + "\n", 'green'))
        return tree_of_thought_final

    def get_final_answer(self, tree_of_thought_final: str, user_question: str):
        updated_user_question = "Experts, please come to a consensus on the following question:\n\n" + user_question
        print(colored("Final question to be asked:\n", 'red'))
        print(colored(updated_user_question, 'magenta'))
        final_answer = self.chat_completer_big.generate_completion(env_and_flags.model, [{"role": "system", "content": tree_of_thought_final}, {"role": "user", "content": updated_user_question}])
        print(colored("Generated answer:\n", 'magenta'))
        print(colored(final_answer, 'magenta'))
        return final_answer

    def compile(self, user_input_question) -> Tuple:
        # Fix question
        perfected_question = self.perfect_question(user_input_question)
        print(colored("Your formatted question is below:\n", 'blue'))
        print(colored(perfected_question + "\n", 'green'))
        
        # Make initial list of related topics
        inital_context = self.make_initial_context(perfected_question)
        print(colored("Initial context:\n", 'red'))
        print(colored(inital_context, 'magenta'))
        
        # Expand on that substantially
        expanded_context = self.expand_context(inital_context)
        print(colored("Expanded context:", 'red'))
        print(colored(expanded_context, 'magenta'))

        # Use Tree of Thought to increase the robustness of a response
        tree_of_thought_final = self.make_tree_of_thought_final(expanded_context)
        
        # Retrieve a final answer
        final_answer = self.get_final_answer(tree_of_thought_final, perfected_question)
        return [tree_of_thought_final, final_answer]
    
    def format_file_name(self, user_input_question: str) -> str:
        formatted_file_name = self.chat_completer_big.generate_completion(env_and_flags.model, [{"role": "system", "content": FILE_FORMATTER}, {"role": "user", "content": user_input_question}])
        return formatted_file_name