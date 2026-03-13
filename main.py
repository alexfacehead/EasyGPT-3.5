import json

from termcolor import colored

from src.utils.logging import Logger
from src.content_generator import ContentGenerator
from src.utils.helpers import format_string
from src.utils.env_setup import EnvironmentSetup
from src.utils.file_handler import FileManager


def main():
    env = EnvironmentSetup()
    logger = Logger().get_logger()

    print("Starting...")
    print(colored(f"MODEL: {env.model}", 'red'))
    print(colored(f"PIPELINE MODEL: {env.pipeline_model}", 'red'))
    print(colored(f"TEMPERATURE: {env.temperature}", 'red'))
    print(colored(f"TOP_P: {env.top_p}\n", 'red'))

    if not env.openai_api_key:
        print(colored("ERROR: No API key found. Set OPENAI_API_KEY in .env or pass --openai_api_key.", 'red'))
        exit(1)

    logger.info(f"MODEL: {env.model}")
    logger.info(f"PIPELINE MODEL: {env.pipeline_model}")
    logger.info(f"OPENAI_API_KEY: {format_string(env.openai_api_key)}")

    content_generator = ContentGenerator(
        api_key=env.openai_api_key,
        model=env.model,
        pipeline_model=env.pipeline_model,
        temperature=env.temperature,
        top_p=env.top_p,
    )

    # Get user's question
    prompt_message = "Enter your question in one to two sentences. Try to make it as accurate, concise, and salient as possible:\n"
    main_user_question = input(
        colored(prompt_message, 'green') + "\n" + colored("ENTER QUESTION HERE: ", 'red', attrs=['bold'])
    )
    logger.info("The pre-formatted message you wrote:\n" + main_user_question)

    # Run the pipeline
    tree_of_thought, final_answer = content_generator.compile(main_user_question)
    conversation = [
        {"role": "system", "content": tree_of_thought},
        {"role": "user", "content": main_user_question},
        {"role": "assistant", "content": final_answer},
    ]

    # Save results
    FileManager.ensure_directory_exists(env.prompt_dir)
    run_num = FileManager.get_highest_run_num(env.prompt_dir) + 1
    FileManager.save_content(env.prompt_dir, 'prompt_and_answer', run_num, conversation)

    # Interactive query mode
    if env.query_mode:
        while True:
            next_question = input(colored("ENTER NEXT QUERY HERE (or type exit to quit): ", 'red', attrs=['bold']))
            if next_question.lower() == "exit":
                break

            next_answer = content_generator.generate_plain_completion(conversation, next_question)
            print(colored("Answer:\n\n" + next_answer, 'magenta'))
            logger.info("Generated follow-up answer:\n" + next_answer)

            conversation.append({"role": "user", "content": next_question})
            conversation.append({"role": "assistant", "content": next_answer})

            run_num += 1
            FileManager.save_content(env.prompt_dir, 'prompt_and_answer', run_num, conversation)

    print(colored("Success! Please evaluate your results against a trusted source.", 'green'))


if __name__ == "__main__":
    main()
