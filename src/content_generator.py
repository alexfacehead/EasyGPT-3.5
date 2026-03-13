from typing import List, Dict, Tuple
from termcolor import colored

from src.utils.constants import (
    FILE_FORMATTER,
    QUESTION_FIXER_PART_ONE, QUESTION_FIXER_PART_TWO,
    CONTEXT_EXPANSION,
    SYSTEM_MESSAGE_GENERATOR,
    AUTOMATED_CONTEXT_CALLER,
)
from src.chat_completion_generator import ChatCompletionGenerator
from src.utils.logging import Logger

logger = Logger().get_logger()


class ContentGenerator:
    def __init__(self, api_key: str, model: str, pipeline_model: str = None,
                 temperature: float = 0.33, top_p: float = 0.5):
        """
        Orchestrates the context-enrichment prompting pipeline.

        Args:
            api_key: OpenAI API key.
            model: The default model (used for query mode, file naming, etc.).
            pipeline_model: The model used for pipeline steps. Defaults to model.
            temperature: Sampling temperature.
            top_p: Nucleus sampling parameter.
        """
        self.model = model
        self.pipeline_model = pipeline_model or model
        self.chat_completer = ChatCompletionGenerator(
            api_key=api_key,
            model=model,
            temperature=temperature,
            top_p=top_p,
        )

    def generate_plain_completion(self, conversation: List[Dict[str, str]], query: str) -> str:
        """Generate a follow-up completion using existing conversation context."""
        if not conversation or not isinstance(conversation, list):
            print(colored("INVALID CONVERSATION HISTORY", 'red'))
            return None

        # Find the system message from the conversation
        system_message = ""
        for msg in conversation:
            if msg.get("role") == "system":
                system_message = msg["content"]
                break

        # Build messages: system + all prior user/assistant turns + new query
        messages = [{"role": "system", "content": system_message}]
        for msg in conversation:
            if msg["role"] != "system":
                messages.append(msg)
        messages.append({"role": "user", "content": query})

        return self.chat_completer.generate_completion(messages)

    # ── Pipeline Steps ───────────────────────────────────────────────

    def perfect_question(self, user_input_question: str) -> str:
        """Step 0: Fix grammar, clarity, and ambiguity in the user's question."""
        prompt = QUESTION_FIXER_PART_ONE + user_input_question + QUESTION_FIXER_PART_TWO
        print(colored(prompt, 'yellow'))
        return self.chat_completer.generate_completion(
            [{"role": "system", "content": prompt}],
            model=self.pipeline_model,
        )

    def make_initial_context(self, user_input_question: str) -> str:
        """Step 1: Generate a list of distinct, related topics."""
        if not user_input_question:
            print(colored("NO QUESTION PROVIDED", 'red'))
            exit(1)
        full_input = AUTOMATED_CONTEXT_CALLER + "\n\n" + user_input_question
        print(colored(full_input, 'yellow'))
        return self.chat_completer.generate_completion([
            {"role": "system", "content": AUTOMATED_CONTEXT_CALLER},
            {"role": "user", "content": user_input_question},
        ], model=self.pipeline_model)

    def expand_context(self, initial_context: str) -> str:
        """Step 2: Synthesize topic list into rich background context."""
        return self.chat_completer.generate_completion([
            {"role": "system", "content": CONTEXT_EXPANSION},
            {"role": "user", "content": initial_context},
        ], model=self.pipeline_model)

    def generate_system_message(self, expanded_context: str, question: str) -> str:
        """Step 3: Build a task-adaptive system message from context and question."""
        user_input = (
            "[BACKGROUND CONTEXT]:\n" + expanded_context + "\n\n"
            "[QUESTION TO BE ANSWERED]:\n" + question
        )
        result = self.chat_completer.generate_completion(
            [
                {"role": "system", "content": SYSTEM_MESSAGE_GENERATOR},
                {"role": "user", "content": user_input},
            ],
            model=self.pipeline_model,
        )
        print(colored("Generated System Message:\n", 'magenta'))
        print(colored(result + "\n", 'green'))
        logger.info("System Message Generated:")
        logger.info(result)
        return result

    def get_final_answer(self, system_message: str, user_question: str) -> str:
        """Step 4: Generate the final answer using the enriched system message."""
        print(colored("Final question to be asked:\n", 'red'))
        print(colored(user_question, 'magenta'))
        answer = self.chat_completer.generate_completion([
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_question},
        ], model=self.pipeline_model)
        print(colored("Generated answer:\n", 'magenta'))
        print(colored(answer, 'magenta'))
        logger.info("Final answer generated:")
        logger.info(answer)
        return answer

    # ── Main entry point ─────────────────────────────────────────────

    def compile(self, user_input_question: str) -> Tuple[str, str]:
        """Run the full context-enrichment pipeline on a user question."""
        perfected_question = self.perfect_question(user_input_question)
        print(colored("Your formatted question is below:\n", 'blue'))
        print(colored(perfected_question + "\n", 'green'))

        initial_context = self.make_initial_context(perfected_question)
        print(colored("Initial context:\n", 'red'))
        print(colored(initial_context, 'magenta'))

        expanded_context = self.expand_context(initial_context)
        print(colored("Expanded context:", 'red'))
        print(colored(expanded_context, 'magenta'))

        system_message = self.generate_system_message(expanded_context, perfected_question)

        final_answer = self.get_final_answer(system_message, perfected_question)
        return (system_message, final_answer)

    def format_file_name(self, user_input_question: str) -> str:
        return self.chat_completer.generate_completion(
            messages=[
                {"role": "system", "content": FILE_FORMATTER},
                {"role": "user", "content": user_input_question},
            ]
        )
