import os
import re
import json


class FileManager:

    @staticmethod
    def get_highest_run_num(directory):
        """Find the highest run number among existing prompt_and_answer files."""
        if not os.path.exists(directory):
            return 0
        highest = 0
        for filename in os.listdir(directory):
            match = re.match(r'prompt_and_answer_(\d+)\.txt', filename)
            if match:
                highest = max(highest, int(match.group(1)))
        return highest

    @staticmethod
    def ensure_directory_exists(directory):
        os.makedirs(directory, exist_ok=True)

    @staticmethod
    def save_content(directory, base_filename, run_num, content):
        """Save conversation content as JSON to a numbered file."""
        FileManager.ensure_directory_exists(directory)
        filename = f"{directory}/prompt_and_answer_{run_num}.txt"
        with open(filename, 'w') as f:
            json.dump(content, f, indent=2)
