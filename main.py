import os
import json

from typing import Optional
from termcolor import colored

from src.utils.logging import Logger
from src.content_generator import ContentGenerator
from src.utils.helpers import format_string
from src.utils.env_setup import EnvironmentSetup
from src.utils.file_handler import *

env_and_flags = EnvironmentSetup()

def main(
    model: Optional[str] = "gpt-3.5-turbo-16k",
    temperature: Optional[float] = 0.33,
    query_mode: Optional[bool] = False,
    openai_api_key: Optional[str]= None,
    super_charged: Optional[bool]=False,
    prompt_dir: Optional[str]=os.path.join(os.getcwd(), "resources", "prompts")
):
    print("Starting...")

    run_num = 0
    
    if temperature != None:
        print(colored(f"TEMPERATURE CHOSEN: {temperature}\n", 'red'))
    else:
        print(colored(f"DEFAULT TEMPERATURE: 0.33\n", 'red'))
    
    if model != None:
        print(colored(f"MODEL CHOSEN: {model}\n", 'red'))
    else:
        print(colored(f"DEFAULT MODEL USED: gpt-3.5-turbo-16k\n", 'red'))

    # Create a Logger and Initialize Env Vars
    logger_instance = Logger()
    logger = logger_instance.get_logger()

    logger.info(f"MODEL: {model}")
    censored_key = format_string(env_and_flags.openai_api_key)
    logger.info(f"OPENAI_API_KEY: {censored_key}")

    # Initialize a content generator
    content_generator = ContentGenerator(env_and_flags.model, env_and_flags.openai_api_key, env_and_flags.super_charged, env_and_flags.temperature)

    # Get user's question
    prompt_message = "Enter your question in one to two sentences. Try to make it as accurate, concise, and salient as possible:\n"
    colored_prompt = colored(prompt_message, 'green')
    main_user_question = input(colored_prompt + "\n" + colored("ENTER QUESTION HERE: ", 'red', attrs=['bold']))

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
    FileManager.save_content(prompt_dir, 'prompt_and_answer', run_num, saved_combined_content)
    run_num = FileManager.get_highest_run_num(prompt_dir) + 1

    if len(final_output) > 1:
        print(colored("Success! Please evaluate your results against a trusted source.", 'green'))
    else:
        logger.error("Error occurred while parsing final output, perhaps index-related, perhaps incorrect function call or possibly context was too long.")
        exit(1)

    if env_and_flags.query_mode == True:
        next_question = input(colored_prompt + "\n" + colored("ENTER NEXT QUERY HERE (or type exit to quit): ", 'red', attrs=['bold']))
        if next_question.lower() != "exit":
            print("NOT EXIT!")
            latest_file_name = f"{prompt_dir}/prompt_and_answer_{run_num - 1}.txt"  # Assuming the files are 0-indexed
            with open(latest_file_name, 'r') as file:
                json_file_output = json.load(file)
                json_file_output.append({"role": "user", "content": next_question})
                next_output = content_generator.generate_plain_completion(json_file_output, next_question)
                next_answer = "Answer to your next question:\n\n" + add_user_question(json_file_output, next_output)
                print(colored(next_answer, 'magenta'))
        else:
            print("Program completed.")
    else:
        exit(0)


if __name__ == "__main__":
    main(
        model=env_and_flags.model,
        temperature=env_and_flags.temperature,
        query_mode=env_and_flags.query_mode,
        openai_api_key=env_and_flags.openai_api_key,
        super_charged=env_and_flags.super_charged,
        prompt_dir=env_and_flags.prompt_dir
    )