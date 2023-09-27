import argparse
import os
import glob
import shutil
import json
from typing import Optional
from termcolor import colored

from src.utils.logs_and_env import Logger
from src.content_creator import ContentGenerator
from src.utils.helpers import format_string

import argparse
import os
import glob
import shutil
import json
from typing import Optional
from termcolor import colored

from src.utils.logs_and_env import Logger
from src.content_creator import ContentGenerator
from src.utils.helpers import format_string


def main(query: Optional[str], openai_api_key: Optional[str], model: Optional[str], super_charged: Optional[bool]) -> str:
    # Create a Logger and Initialize Env Vars
    logger_instance = Logger()
    logger = logger_instance.get_logger()

    # If the values are not provided as arguments, fetch them from the environment
    openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
    model = model or os.getenv("MODEL")
    super_charged = super_charged or os.getenv("SUPER_CHARGED")

    logger.info(f"MODEL: {model}")
    censored_key = format_string(openai_api_key)
    logger.info(f"OPENAI_API_KEY: {censored_key}")

    # Initialize a content generator
    content_generator = ContentGenerator(model, openai_api_key, super_charged)

    # Get user's question
    prompt_message = "Enter your question in one to two sentences. Try to make it as accurate, concise, and salient as possible:\n"
    colored_prompt = colored(prompt_message, 'green')
    main_user_question = input(colored_prompt)

    final_output = content_generator.compile(main_user_question)

    if len(final_output) > 1:
        print(colored("Success! Please evaluate your results against a trusted source.", 'green'))
    else:
        logger.error("Error occurred while parsing final output, perhaps index-related, perhaps incorrect function call.")
        exit(1)

    if len(final_output) > 1:
        return final_output[1]
    else:
        logger.error("Error occurred.")
        exit(1)

def interactive_mode(self, query: str, prompt_num: Optional[int]) -> None:
        """
        Executes the script in an interactive mode, continuously taking user queries and generating completions.
        It also manages the conversation history and writes it back to the prompt file after each interaction.
        
        Args:
            query (str): The initial user query to start the interaction.
            prompt_num (int): The prompt to be retrieved from resources/prompts/prompt_*.txt
        """
        # Find the script's directory and the prompt directory
        script_dir = os.getcwd()
        prompt_dir = os.path.join(script_dir, "resources", "prompts")


        if self.prompt_num is None:
            # Use the most recent prompt
            list_of_files = glob.glob(os.path.join(prompt_dir, "*.txt"))
            prompt_file = max(list_of_files, key=os.path.getctime)
        else:
            # Use a specific prompt
            prompt_file = os.path.join(prompt_dir, f"prompt_{self.prompt_num}.txt")

        # Read the system message from the prompt file
        with open(prompt_file, "r") as f:
            system_message = f.read()


        # Make backup of the prompt file
        shutil.copy2(prompt_file, prompt_file + ".bak")

        # Initialize the conversation history
        conversation_history = [
            {
                "role": "system",
                "content": system_message
            }
        ]

        while True:
            response = self.generate_completion(conversation_history + [{"role": "user", "content": query}])
            print(response)

            # Update the conversation history
            conversation_history.append({
                "role": "user",
                "content": query
            })
            conversation_history.append({
                "role": "assistant",
                "content": response
            })

            # Write the updated conversation history back to the prompt file
            with open(prompt_file, "w") as f:
                json.dump(conversation_history, f, indent=4, ensure_ascii=False)

            query = input("Enter your next query, or 'exit' to quit: ")
            if query.lower() == 'exit':
                break
class Query:
    def __init__(self):
        self.logger_instance = Logger()
        self.logger = self.logger_instance.get_logger()

    def interactive_mode(self, query: str, prompt_num: Optional[int]) -> None:
        """
        Executes the script in an interactive mode, continuously taking user queries and generating completions.
        It also manages the conversation history and writes it back to the prompt file after each interaction.
        
        Args:
            query (str): The initial user query to start the interaction.
            prompt_num (int): The prompt to be retrieved from resources/prompts/prompt_*.txt
        """

        # Use Logger's method to get the prompt directory
        prompt_dir = self.logger_instance.prompt_dir()

        if prompt_num is None:
            # Use the most recent prompt
            list_of_files = glob.glob(os.path.join(prompt_dir, "*.txt"))
            prompt_file = max(list_of_files, key=os.path.getctime)
        else:
            # Use a specific prompt
            prompt_file = os.path.join(prompt_dir, f"prompt_{prompt_num}.txt")

        # Read the system message from the prompt file
        with open(prompt_file, "r") as f:
            system_message = f.read()

        # Make backup of the prompt file
        shutil.copy2(prompt_file, prompt_file + ".bak")

        # Initialize the conversation history
        conversation_history = [
            {
                "role": "system",
                "content": system_message
            }
        ]

        while True:
            # This is a hypothetical method. You'll need to define/implement it or adjust as needed.
            response = self.generate_completion(conversation_history + [{"role": "user", "content": query}])
            print(response)

            # Update the conversation history
            conversation_history.append({
                "role": "user",
                "content": query
            })
            conversation_history.append({
                "role": "assistant",
                "content": response
            })

            # Write the updated conversation history back to the prompt file
            with open(prompt_file, "w") as f:
                json.dump(conversation_history, f, indent=4, ensure_ascii=False)

            query = input("Enter your next query, or 'exit' to quit: ")
            if query.lower() == 'exit':
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, help="Run this command to query a particular System Message with a user message as many times as you like.")
    parser.add_argument("--num", type=int, help="Specify a particular prompt number from the default prompt directory.")
    parser.add_argument("--openai_api_key", type=str, help="Your personal API key for OpenAI.")
    parser.add_argument("--model", type=str, help="Model chosen from OpenAI.")
    parser.add_argument("--super_charged", action="store_true", help="Super charged mode for GPT-4 - increases prompt quality.")
    args = parser.parse_args()

    main(args.query, args.openai_api_key, args.model, args.super_charged)