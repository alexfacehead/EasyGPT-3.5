import time
import argparse
import os
from src.content_generator import ContentGenerator
from dotenv import load_dotenv

# Load the .env file into the environment
load_dotenv()

# Set defaults or get from environment
QUESTION_TEST = os.getenv('QUESTION')
TEMP_START_VALUE = float(os.getenv('TEMP_START_VALUE'))
TEMP_RANGE = int(os.getenv('TEMP_RANGE'))
SAVE_DIR = os.getenv('SAVE_DIR', str("src/unit_testing/unit_test_results"))
REPEAT = int(os.getenv('REPEAT'))
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = os.getenv('MODEL')

def test_temperature_runs(question=QUESTION_TEST, temp_start_value=TEMP_START_VALUE, temp_range=TEMP_RANGE, save_dir=SAVE_DIR, repeat=REPEAT):

    # Ensure save directory exists and handle duplicates
    if (not os.path.exists(save_dir)) or (os.path.exists(save_dir) and len(os.listdir(save_dir)) > 200):
        os.makedirs(save_dir)
    else:
        count = 1
        base_save_dir = save_dir.rstrip('/')
        while os.path.exists(save_dir):
            count += 1
            save_dir = f"{base_save_dir}_{count}/"
        os.makedirs(save_dir)

    simple_formatter = ContentGenerator(temperature=0.15)
    formatted_file_name = simple_formatter.format_file_name(question)

    # Calculate the temperatures based on the inputs: limit the max to 2.0.
    temperatures = [round(temp_start_value * i, 2) for i in range(1, temp_range + 1)]
    temperatures = [temp for temp in temperatures if temp <= 2.0]

    for temperature in temperatures:
        content_generator = ContentGenerator(temperature=temperature)
        start_time = time.time()
        _, final_answer = content_generator.compile(question)
        end_time = time.time()
        elapsed_time = end_time - start_time

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        result = f"Timestamp: {timestamp}\nTemperature: {temperature}\nElapsed Time: {elapsed_time:.2f} seconds\n\n{final_answer}\n\n"

        with open(f"{save_dir}/{formatted_file_name}_{temperature}.txt", "w") as f:
            f.write(result)

# Run the tests
test_temperature_runs(question=QUESTION_TEST, temp_start_value=TEMP_START_VALUE, temp_range=TEMP_RANGE, save_dir=SAVE_DIR, repeat=REPEAT)