import argparse
import os
import json
from typing import Optional
from termcolor import colored

from src.utils.logs_and_env import Logger
from src.content_creator import ContentGenerator
from src.utils.helpers import format_string

def get_argument(value, default):
    return value if value is not None else default

def main(query: Optional[str] = None,
         openai_api_key: Optional[str] = None,
         model: Optional[str] = None,
         super_charged: Optional[bool] = False,
         temperature: Optional[float] = 0.33,
         prompt_dir: Optional[str] = "resources/prompt") -> str:

    openai_api_key = get_argument(openai_api_key, os.getenv("OPENAI_API_KEY"))
    model = get_argument(model, os.getenv("MODEL"))
    super_charged = get_argument(super_charged, os.getenv("SUPER_CHARGED") == 'True')
    temperature = get_argument(temperature, args.temperature)
    query = get_argument(query, args.query)
    prompt_dir = get_argument(prompt_dir, args.prompt_dir)

    run_num = 0
    
    if temperature != None:
        print(colored(f"TEMPERATURE CHOSEN: {temperature}\n", 'red'))
    else:
        print(colored(f"TEMPERATURE: 0.33\n", 'red'))

    # Create a Logger and Initialize Env Vars
    logger_instance = Logger()
    logger = logger_instance.get_logger()

    logger.info(f"MODEL: {model}")
    censored_key = format_string(openai_api_key)
    logger.info(f"OPENAI_API_KEY: {censored_key}")

    # Initialize a content generator
    content_generator = ContentGenerator(model, openai_api_key, super_charged, temperature=temperature)

    # Get user's question
    prompt_message = "Enter your question in one to two sentences. Try to make it as accurate, concise, and salient as possible:\n"
    colored_prompt = colored(prompt_message, 'green')
    main_user_question = input(colored_prompt + "\n" + colored("ENTER QUESTION HERE: ", 'red', attrs=['bold']))
    def ensure_directory_exists(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def get_next_available_filename(directory, base_filename, run_num):
        while True:
            filename = f"{directory}/prompt_and_answer_{run_num}.txt"
            if not os.path.exists(filename):
                return filename
            run_num += 1

    def save_content(directory, base_filename, run_num, content):
        ensure_directory_exists(directory)
        filename = get_next_available_filename(directory, base_filename, run_num)
        with open(filename, 'w') as file:
            json.dump(content, file, indent=2)

    # Get final output, and save it for interactive querying
    final_output = content_generator.compile(main_user_question)
    saved_combined_content = [{"role": "system", "content": final_output[0]}, {"role": "user", "content": final_output[1]}]

    # Assuming prompt_dir and run_num are defined
    save_content(prompt_dir, 'prompt_and_answer', run_num, saved_combined_content)

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Your script description here")
    parser.add_argument("--query", type=str, help="Enter your next question here, which will continue from the last prompts, rotationally deleting older results for context preservation.")
    parser.add_argument("--temperature", type=float, help="Higher value is more random/creative.")
    parser.add_argument("--openai_api_key", type=str, help="Your OPENAI_API_KEY")
    parser.add_argument("--model", type=str, help="Your chosen OpenAI model")
    parser.add_argument("--super_charged", type=lambda x: (str(x).lower() == 'true'), help="If you have access to GPT-4, empowers results.")
    parser.add_argument("--prompt_dir", type=str, help="The directory for which you'd like to save your prompts and answer histories.", default="resources/prompts")
    args = parser.parse_args()
    
    main(
        query=args.query,
        temperature=args.temperature,
        openai_api_key=args.openai_api_key,
        model=args.model,
        super_charged=args.super_charged,
        prompt_dir=args.prompt_dir
    )
