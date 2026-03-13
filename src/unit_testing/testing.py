import os
import time

from termcolor import colored
from dotenv import load_dotenv

from src.content_generator import ContentGenerator

load_dotenv()

# Test configuration from .env
QUESTION_TEST = os.getenv('QUESTION', '')
TOP_P_START = float(os.getenv('TEMP_START_VALUE', '0.07'))
TOP_P_STEPS = int(os.getenv('TEMP_RANGE', '10'))
SAVE_DIR = os.getenv('SAVE_DIR', 'src/unit_testing/unit_test_results')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
MODEL = os.getenv('MODEL', 'gpt-4')


def test_top_p_runs(question=QUESTION_TEST, top_p_start=TOP_P_START,
                    top_p_steps=TOP_P_STEPS, save_dir=SAVE_DIR):
    """Run the pipeline across a range of top_p values and save results."""
    print(colored(f"Test question: {question}", 'red'))

    if not isinstance(question, str) or not question:
        raise ValueError("Question must be a non-empty string.")

    # Create save directory, appending a number if it already has >200 files
    if not os.path.exists(save_dir) or len(os.listdir(save_dir)) > 200:
        os.makedirs(save_dir, exist_ok=True)
    else:
        count = 1
        base_dir = save_dir.rstrip('/')
        while os.path.exists(save_dir):
            count += 1
            save_dir = f"{base_dir}_{count}/"
        os.makedirs(save_dir)

    # Generate a filename from the question
    formatter = ContentGenerator(api_key=OPENAI_API_KEY, model=MODEL, top_p=0.1)
    formatted_file_name = formatter.format_file_name(question)

    # Calculate top_p values to test
    top_p_values = [round(top_p_start * i, 2) for i in range(1, top_p_steps + 1)]
    top_p_values = [v for v in top_p_values if v <= 1.0]

    for top_p in top_p_values:
        content_generator = ContentGenerator(api_key=OPENAI_API_KEY, model=MODEL, top_p=top_p)
        start_time = time.time()
        _, final_answer = content_generator.compile(question)
        elapsed = time.time() - start_time

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        result = f"Timestamp: {timestamp}\nTop P: {top_p}\nElapsed Time: {elapsed:.2f} seconds\n\n{final_answer}\n\n"

        with open(f"{save_dir}/{formatted_file_name}_{top_p}.txt", "w") as f:
            f.write(result)
