import unittest
import sys
import os
import time
from src.content_creator import ContentGenerator

class TestContentGenerator(unittest.TestCase):

    def test_temperature_runs(self):
        temperatures = [round(0.05 * i, 2) for i in range(1, 12)]
        question = "What is the impact of global warming on the polar ice caps?"

        for temperature in temperatures:
            content_generator = ContentGenerator(temperature=temperature)
            start_time = time.time()
            _, final_answer = content_generator.compile(question)
            end_time = time.time()
            elapsed_time = end_time - start_time

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            result = f"Timestamp: {timestamp}\nTemperature: {temperature}\nElapsed Time: {elapsed_time:.2f} seconds\n\n{final_answer}\n\n"

            with open(f"resources/prompts/temperature_{temperature}.txt", "a") as f:
                f.write(result)

if __name__ == '__main__':
    unittest.main()