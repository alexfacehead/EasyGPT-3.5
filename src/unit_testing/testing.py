import unittest
import time
import argparse
import os
from src.content_generator import ContentGenerator
#from src.utils.helpers import compile_unit_test_prompts

class TestContentGenerator(unittest.TestCase):

    def test_temperature_runs(self):
        # Fetch arguments
        parser = argparse.ArgumentParser(description='Set the question for the content generator test')
        parser.add_argument('--question_test', type=str, help="Specify the question for the test", default="What is the consensus on climate change?")
        parser.add_argument('--temp_start_value', type=float, help="This specifies which temperature value you'd like to start at. Default is 0.1, lowest possible is 0. Be wary of running too many test cases.", default=0.1)
        parser.add_argument('--temp_range', type=int, help="Specify the range for which you would like to test LLM temperatures. Higher numbers mean more test cases, up to 2.0.", default=20)
        parser.add_argument('--save_dir', type=str, help="Directory to save the unit test results", default="src/unit_testing/unit_test_results/")
        parser.add_argument('--repeat', type=int, help="Repeat the question as many times as you like. Input is an integer.", default=1)
        args = parser.parse_args()

        question = args.question_test
        temp_start_value = args.temp_start_value
        temp_range = args.temp_range
        save_dir = args.save_dir
        repeat = args.repeat

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

        simple_formatter = ContentGenerator(temperature=0.15, irrelevant_content=True)
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

if __name__ == '__main__':
    unittest.main()