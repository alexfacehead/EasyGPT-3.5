# README.md

# OpenAI ChatCompletions API Wrapper

This project is a Python wrapper for the OpenAI ChatCompletions API. It allows you to generate powerful prompts easily starting with a single sentence. It is built on tree-of-thought prompting, and it includes unit testing, customization, parameters, and example use cases.

## Features

- Generate prompts using the OpenAI ChatCompletions API
- Unit testing for different temperature runs
- Customizable model, temperature, and query mode for endless conversation
- Save generated prompts and answers
- Query mode for interactive querying
- [COMING SOON!!!] A fullblown website and application for mobile devices.

## Installation
0. Have Python and venv setup at minimum.

1. Clone this repository:

```bash
git clone https://github.com/yourusername/yourrepository.git
```

2. Navigate to the project directory:

```bash
cd yourrepository
```

3. Create a virtual environment:

- On macOS and Linux:

```bash
python3 -m venv env
```

- On Windows:

```bash
py -m venv env
```

4. Activate the virtual environment:

- On macOS and Linux:

```bash
source env/bin/activate
```

- On Windows:

```bash
.\env\Scripts\activate
```

5. Install the requirements:

```bash
pip install -r requirements.txt
```

## Usage

1. Set your OpenAI API key in a `.env` file:

```bash
echo "OPENAI_API_KEY=yourapikey" > .env
```

2. Run the main script:

```bash
python main.py
```

You can customize the model, temperature, and query mode by passing arguments to the script. For example:

```bash
python main.py --model="gpt-3.5-turbo-16k" --temperature=0.33 --query_mode=True
```

3. Follow the prompts to enter your question.

4. The generated prompts and answers will be saved in the `resources/prompts` directory.

5. If you enabled query mode, you can continue asking questions in the same context.

6. Run the unit tests:

```bash
python run_tests.py
```

You can customize the question, temperature start value, temperature range, save directory, and repeat count by setting environment variables in the `.env` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Unit Testing & Contributions!

This project includes a script for running unit tests. The tests generate prompts for a range of temperatures and save the results.

To run the unit tests, use the following command:

```bash
python run_tests.py
```

You can customize the question, temperature start value, temperature range, save directory, and repeat count by setting environment variables in the `.env` file. For example:

```bash
echo "QUESTION='What is the meaning of life?'" >> .env
echo "TEMP_START_VALUE=0.1" >> .env
echo "TEMP_RANGE=10" >> .env
echo "SAVE_DIR='src/unit_testing/unit_test_results'" >> .env
echo "REPEAT=5" >> .env
```

After running the tests, you can view the results in the specified save directory. Each file is named with the format `temperature_X.txt`, where `X` is the temperature used for that test. The file `compilation.txt` contains a compilation of all test results.

# You May Also Simply Edit The `.env.template` File And Accomplish the Same Thing For Unit Testing