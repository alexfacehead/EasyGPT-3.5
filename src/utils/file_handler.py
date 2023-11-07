import os
import re
import json
from typing import Optional

class FileManager:
    
    @staticmethod
    def get_highest_run_num(directory):
        highest_run_num = 0
        for filename in os.listdir(directory):
            match = re.match(r'prompt_and_answer_(\d+)\.txt', filename)
            if match:
                run_num = int(match.group(1))
                highest_run_num = max(highest_run_num, run_num)
        return highest_run_num

    @staticmethod
    def ensure_directory_exists(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def get_next_available_filename(directory, base_filename, run_num, addition: Optional[bool] = False):
        if not addition:
            while True:
                filename = f"{directory}/prompt_and_answer_{run_num}.txt"
                if not os.path.exists(filename):
                    return filename
                run_num += 1
        else:
            return f"{directory}/prompt_and_answer_{run_num}.txt"
    
    @staticmethod
    def save_content(directory, base_filename, run_num, content, addition: Optional[bool] = False) -> None:
        FileManager.ensure_directory_exists(directory)
        filename = base_filename
        if not addition:
            filename = FileManager.get_next_available_filename(directory, base_filename, run_num, addition)
        else:
            filename = f"{directory}/prompt_and_answer_{run_num}.txt"
        with open(filename, 'w') as file:
            json.dump(content, file, indent=2)