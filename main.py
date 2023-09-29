import argparse
import os
import json
import re

from typing import Optional
from termcolor import colored

from src.utils.logs_and_env import Logger
from src.content_creator import ContentGenerator
from src.utils.helpers import format_string

def get_argument(value, default):
    return value if value is not None else default

def main(query_mode: Optional[bool] = None,
         openai_api_key: Optional[str] = None,
         model: Optional[str] = None,
         super_charged: Optional[bool] = False,
         temperature: Optional[float] = 0.33,
         prompt_dir: Optional[str] = "resources/prompt") -> str:

    openai_api_key = get_argument(openai_api_key, os.getenv("OPENAI_API_KEY"))
    model = get_argument(model, os.getenv("MODEL"))
    super_charged = get_argument(super_charged, os.getenv("SUPER_CHARGED") == 'True')
    temperature = get_argument(temperature, args.temperature)
    query_mode = get_argument(query_mode, args.query_mode)
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
    
    def get_highest_run_num(directory):
        highest_run_num = 0
        for filename in os.listdir(directory):
            match = re.match(r'prompt_and_answer_(\d+)\.txt', filename)
            if match:
                run_num = int(match.group(1))
                highest_run_num = max(highest_run_num, run_num)
        return highest_run_num

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

    def add_user_question(json_output, user_question):
        # Create a new dictionary for the user's question
        user_question_dict = {
            "role": "user",
            "content": user_question
        }
        return user_question

    # Get final output, and save it for interactive querying
    final_output = content_generator.compile(main_user_question)
    saved_combined_content = [{"role": "system", "content": final_output[0]}, {"role": "user", "content": final_output[1]}]

    # Assuming prompt_dir and run_num are defined
    save_content(prompt_dir, 'prompt_and_answer', run_num, saved_combined_content)
    run_num = get_highest_run_num(prompt_dir) + 1

    if len(final_output) > 1:
        print(colored("Success! Please evaluate your results against a trusted source.", 'green'))
    else:
        logger.error("Error occurred while parsing final output, perhaps index-related, perhaps incorrect function call.")
        exit(1)

    next_question = input(colored_prompt + "\n" + colored("ENTER NEXT QUERY HERE (or type exit to quit): ", 'red', attrs=['bold']))
    next_user_input = str.lower(next_question)
    if next_user_input != exit:
        latest_file_name = f"{prompt_dir}/prompt_and_answer_{run_num - 1}.txt"  # Assuming the files are 0-indexed
        with open(latest_file_name, 'r') as file:
            json_file_output = json.load(file)
            json_file_output.append({"role": "user", "content": next_question})
            next_output = content_generator.generate_plain_completion(json_file_output, next_question)
            next_answer = "Answer to your next question:\n\n" + add_user_question(json_file_output, next_output)
            print(colored(next_answer, 'magenta'))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="An easier and far cheaper way to use the gpt-3.5-turbo API, with results nearly comparable to ChatGPT 4 - with more additions coming soon!")
    parser.add_argument("--query_mode", type=bool, help="Enter True or False to continue asking questions in this context.")
    parser.add_argument("--temperature", type=float, help="Higher value is more random/creative.")
    parser.add_argument("--openai_api_key", type=str, help="Your OPENAI_API_KEY")
    parser.add_argument("--model", type=str, help="Your chosen OpenAI model")
    parser.add_argument("--super_charged", type=lambda x: (str(x).lower() == 'true'), help="If you have access to GPT-4, empowers results.")
    parser.add_argument("--prompt_dir", type=str, help="The directory for which you'd like to save your prompts and answer histories.", default="resources/prompts")
    args = parser.parse_args()
    
    main(
        query_mode=args.query_mode,
        temperature=args.temperature,
        openai_api_key=args.openai_api_key,
        model=args.model,
        super_charged=args.super_charged,
        prompt_dir=args.prompt_dir
    )
