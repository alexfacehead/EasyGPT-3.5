# CONTRIBUTING.md

Welcome to the OpenAI ChatCompletions All-Model Enhancer project! We're excited that you're interested in contributing. This document will guide you through the process of setting up your environment for development and explain how to run and write unit tests based on our source code.

## Setting Up Your Development Environment

Before you can contribute, you'll need to set up your development environment. Please refer to the `README.md` and `FAQ.md` for instructions on installing `git`, `venv`, and other prerequisites.

Once you have the prerequisites installed, you can clone the repository, set up a virtual environment, and install the dependencies as described in the `README.md`.

## Running Unit Tests

Unit tests are an essential part of our development process. They help ensure that new changes don't break existing functionality and that the application behaves as expected.

To run the existing unit tests, follow these steps:

1. Navigate to the root directory of the project.
2. Run the `run_tests.py` script using Python:

```bash
python run_tests.py
```

The `run_tests.py` script will invoke the `test_temperature_runs` function from the `src/unit_testing/testing.py` module. This function tests the application's behavior at different "top_p" values, which control the randomness of the AI's responses.

The script uses environment variables to customize the test parameters. You can set these variables in the `.env` file or export them directly in your shell. Here are the variables used:

- `QUESTION`: The question or prompt to test with the AI.
- `TEMP_START_VALUE`: The starting value for the "top_p" parameter.
- `TEMP_RANGE`: The range of "top_p" values to test: this multiplies, so if your starting temp is 0.1, and range is 10, 10 tests will be run (0.1, 0.2, 0.3 ... 1.0)
- `SAVE_DIR`: The directory where test results will be saved.
- `REPEAT`: The number of times to repeat the test.
- `TOP_P`: The "top_p" value for the AI's responses.

## Writing Unit Tests

When contributing new features or fixing bugs, you should also write unit tests to cover your changes. Here's a guide to writing unit tests for this project:

1. Identify the functionality that needs to be tested. This could be a new function, method, or class that you've added or modified.
2. Create a new test function in the `src/unit_testing/testing.py` module or a new test module in the `src/unit_testing` directory.
3. Use the `ContentGenerator` class from the `src/content_generator.py` module to simulate generating prompts with the AI.
4. Write assertions to check that the output of the `ContentGenerator` matches the expected results.
5. If you're testing error conditions, make sure to handle exceptions appropriately and assert that they are raised when expected.

Here's an example of a simple test function:

```python
def test_example_feature():
    # Set up test inputs and expected outputs
    test_input = "Example input"
    expected_output = "Expected output"
    
    # Instantiate the ContentGenerator
    content_generator = ContentGenerator()
    
    # Run the feature being tested
    actual_output = content_generator.some_new_feature(test_input)
    
    # Assert that the actual output matches the expected output
    assert actual_output == expected_output, "The new feature did not produce the expected output."
```

## Submitting Your Contributions

Once you've made your changes and written unit tests, you can submit your contributions as follows:

1. Fork the repository on GitHub.
2. Create a new branch for your changes.
3. Commit your changes and push them to your fork.
4. Open a pull request against the original repository.

Please provide a clear description of your changes and any additional context that might help the maintainers understand your contribution.

Thank you for contributing to the OpenAI ChatCompletions All-Model Enhancer project! Your efforts help make this tool better for everyone.

## Advanced Testing with GPT-4

For contributors with access to the `gpt-4-1106-preview` model and higher rate limits or RPD (requests per day), we offer a more advanced testing approach. This method involves aggregating the output from multiple unit tests into a single file, which can then be analyzed by the `gpt-4-1106-preview` model using a pre-made System Message.

### Aggregating Test Outputs

To aggregate the outputs from the `src/unit_testing/*` directory, you can use the `cat` command in Unix-based systems or its equivalent in Windows. The goal is to concatenate the contents of all unit test result files, separated by their filenames, into a single file for analysis.

Here's how you can do it:

#### Unix-based Systems (macOS and Linux):

```bash
cd src/unit_testing/
for file in *; do
    echo "Filename: $file" >> ../aggregated_results.txt
    cat "$file" >> ../aggregated_results.txt
    echo "\n\n" >> ../aggregated_results.txt
done
```

#### Windows:

On Windows, you can use PowerShell to achieve similar results:

```powershell
cd src\unit_testing\
Get-ChildItem -Filter * | ForEach-Object {
    Add-Content -Path ..\aggregated_results.txt -Value "Filename: $($_.Name)"
    Get-Content $_.FullName | Add-Content -Path ..\aggregated_results.txt
    Add-Content -Path ..\aggregated_results.txt -Value "`n`n"
}
```

### Analyzing Results with GPT-4

Once you have the aggregated results file, you can use it as input for the `gpt-4-1106-preview` model. Create a System Message that instructs the model to analyze the test results across multiple runs. This message should guide the model to look for patterns, anomalies, or any other specific analysis you require.

Here's an example of how you might use the aggregated results file with a pre-made System Message:

```python
from src.content_generator import ContentGenerator

# Load the aggregated results
with open('aggregated_results.txt', 'r') as file:
    aggregated_results = file.read()

# Pre-made System Message for analysis
Run the main application with the query:
`Analyze the following test results from multiple runs of the OpenAI ChatCompletions All-Model Enhancer unit tests. Look for patterns in the AI's responses, any anomalies in the results, and provide a summary of the effectiveness of different 'top_p' values used during the tests. Ensure that there is space in your prompt for said results (such as [UNIT TESTING RESULTS TO-BE-ANALYZED BELOW]:`

Utilize the generated system message  with your output, which, how to be generated, will be explained below.

# Instantiate the ContentGenerator with access to gpt-4-1106-preview
content_generator = ContentGenerator(model='gpt-4-1106-preview')

# Combine the System Message with the aggregated results
analysis_input = system_message + "\n\n" + aggregated_results

# Generate the analysis
analysis_output = content_generator.generate_plain_completion(analysis_input)

# Output the analysis results
print(analysis_output)