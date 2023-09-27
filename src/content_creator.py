from typing import Optional, Tuple
from src.utils.constants import CONTEXT_EXPANSION, TREE_OF_THOUGHT_MAKER_SECOND_HALF, TREE_OF_THOUGHT_MAKER_FIRST_HALF, AUTOMATED_CONTEXT_CALLER
from src.utils.helpers import sum_content_length
from src.chat_completion_generator import ChatCompletionGenerator
from src.utils.logs_and_env import Logger
from termcolor import colored

logger = Logger()
OPENAI_API_KEY = logger._get_env_variable("OPENAI_API_KEY")
MODEL = logger._get_env_variable("MODEL")
SUPER_CHARGED = logger._get_env_variable("SUPER_CHARGED")

class ContentGenerator:
    def __init__(self, prompt_num: Optional[int] = None, model: Optional[str] = None, super_charged: Optional[str] = None, default_compilation: Optional[str] = ""):
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
        self.openai_api_key = OPENAI_API_KEY
        self.model = MODEL
        self.super_charged = SUPER_CHARGED
        
        # Initialize a gpt-3.5-turbo chat completer
        self.chat_completer_small = ChatCompletionGenerator(prompt_num=prompt_num, openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", super_charged=super_charged)
        
        # Initialize a gpt-4-0314 chat completer (more powerful)
        self.chat_completer_big = ChatCompletionGenerator(prompt_num=prompt_num, openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", super_charged=super_charged)

    def make_initial_context(self, user_question: str, context: str = AUTOMATED_CONTEXT_CALLER):
        if user_question == "":
            print(colored("NO QUESTION PROVIDED", 'red'))
            exit(1)
        initial_context = self.chat_completer_big.generate_completion([{"role": "system", "content": AUTOMATED_CONTEXT_CALLER}, {"role": "user", "content": user_question}])
        return initial_context

    def expand_context(self, chat_completer_big: ChatCompletionGenerator, initial_context: str):
        expanded_context = chat_completer_big.generate_completion([{"role": "system", "content": CONTEXT_EXPANSION}, {"role": "user", "content": initial_context}])
        print(colored("Expanded context:\n", 'magenta'))
        print(colored(expanded_context, 'green'))
        return expanded_context

    def make_tree_of_thought_final(self, chat_completer_big: ChatCompletionGenerator, expanded_context: str):
        total_system_message_input = TREE_OF_THOUGHT_MAKER_FIRST_HALF + "[CONTEXT]:\n" + expanded_context + TREE_OF_THOUGHT_MAKER_SECOND_HALF
        tree_of_thought_final = chat_completer_big.generate_completion([{"role": "system", "content": total_system_message_input}, {"role": "user", "content": ""}])
        print(colored("Final prompt:\n", 'magenta'))
        print(colored(tree_of_thought_final, 'green'))
        return tree_of_thought_final
    
    def get_final_answer(self, chat_completer_big: ChatCompletionGenerator, tree_of_thought_final: str, user_question: str):
        user_input = "Experts, please come to a consensus on the following question:\n" + tree_of_thought_final
        final_answer = chat_completer_big.generate_completion([{"role": "system", "content": tree_of_thought_final}, {"role": "user", "content": user_question}])
        print(colored("Generated answer:\n"), 'magenta')
        print(colored(final_answer, 'magenta'))
        return final_answer
    
    def compile(self, user_input_question) -> Tuple:
        inital_context = self.make_initial_context(user_input_question)
        expanded_context = self.expand_context(self.chat_completer_big, inital_context)
        tree_of_thought_final = self.make_tree_of_thought_final(self.chat_completer_big, expanded_context)
        final_answer = self.get_final_answer(self.chat_completer_big, tree_of_thought_final, user_input_question)
        return [tree_of_thought_final, final_answer]