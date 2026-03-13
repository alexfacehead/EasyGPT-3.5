import os
from dotenv import load_dotenv
from src.unit_testing.testing import test_top_p_runs

load_dotenv()

QUESTION = os.getenv('QUESTION', '')
TOP_P_START = float(os.getenv('TEMP_START_VALUE', '0.07'))
TOP_P_STEPS = int(os.getenv('TEMP_RANGE', '10'))
SAVE_DIR = os.getenv('SAVE_DIR', 'src/unit_testing/unit_test_results')
REPEAT = int(os.getenv('REPEAT', '1'))


def main():
    for _ in range(REPEAT):
        test_top_p_runs(
            question=QUESTION,
            top_p_start=TOP_P_START,
            top_p_steps=TOP_P_STEPS,
            save_dir=SAVE_DIR,
        )


if __name__ == '__main__':
    main()
