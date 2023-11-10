# CONTRIBUTING.md

Welcome to the OpenAI ChatCompletions All-Model Enhancer project! Your interest in contributing to this innovative tool is thrilling. This document is your roadmap for setting up a development environment and understanding our unit testing framework.

## Setting Up Your Development Environment

Embarking on your contribution journey begins with a proper setup. For guidance on installing `git`, `venv`, and other prerequisites, our `README.md` and `FAQ.md` are your trusty companions.

Once equipped with the essentials, clone the repository, breathe life into a virtual environment, and embrace the dependencies as outlined in the `README.md`.

## Running Unit Tests

Unit tests are the guardians of our codebase. They vigilantly protect against regressions and ensure the application's behavior is as expected.

To run the existing unit tests:

1. Anchor yourself in the project's root directory.
2. Summon the `run_tests.py` script with Python:

```bash
python run_tests.py
```

This incantation calls upon the `test_temperature_runs` function from `src/unit_testing/testing.py`. It embarks on a quest to test the application's mettle at various "top_p" values, steering the AI's creative helm.

Customize your test parameters through the mystical `.env` file or declare them directly in your shell's environment. The variables at play are:

- `QUESTION`: The enigmatic prompt for the AI's contemplation.
- `TEMP_START_VALUE`: The "top_p" parameter's initial seed.
- `TEMP_RANGE`: The span of "top_p" values to test, multiplying the start value up to a cap of 1.0.
- `SAVE_DIR`: The sacred ground where test results find rest.
- `REPEAT`: The ritual repetition of the test.
- `TOP_P`: The AI's guiding star for response randomness.

## Writing Unit Tests

As you weave new features or mend the fabric of our code, penning unit tests is a rite of passage. Here's how to honor this tradition:

1. Pinpoint the essence of what requires testing, be it a nascent function, method, or class.
2. In the `src/unit_testing/testing.py` module or within the `src/unit_testing` directory, craft a new test function or module.
3. Employ the `ContentGenerator` from `src/content_generator.py` to mimic the AI's prompt generation.
4. Assert that the `ContentGenerator`'s output aligns with the prophecy (expected results).
5. When testing the abyss (error conditions), handle exceptions with care and assert their emergence as foretold.

Behold, a test function in its simplest form:

```python
def test_example_feature():
    # Prepare the offerings (test inputs and expected outputs)
    test_input = "Example input"
    expected_output = "Expected output"
    
    # Conjure the ContentGenerator
    content_generator = ContentGenerator()
    
    # Challenge the feature under test
    actual_output = content_generator.some_new_feature(test_input)
    
    # Verify the actual output against the expected
    assert actual_output == expected_output, "The new feature strayed from the expected path."
```

## Submitting Your Contributions

Once your masterpiece is ready and unit tests are scribed:

1. Fork the repository on the GitHub altar.
2. Branch out to create a new narrative for your changes.
3. Commit your tale and push it to your fork.
4. Open a pull request to merge your story with the original repository.

Narrate your changes with clarity and sprinkle additional context to aid the maintainers in their understanding.

Your contribution is a beacon of progress for the OpenAI ChatCompletions All-Model Enhancer project. We are grateful for your dedication to enhancing this tool for all.

---------------------------------------------------------------

# Advanced Testing with GPT-4

For those blessed with access to `gpt-4-1106-preview` and bestowed with generous rate limits or RPD, a higher echelon of testing awaits. This advanced ritual involves merging the essence of multiple unit tests into a single tome for the `gpt-4-1106-preview` model to analyze with a pre-crafted System Message.

### Aggregating Test Outputs

To weave together the outputs from `src/unit_testing/*`, Unix acolytes can employ the `cat` command, while Windows disciples can invoke PowerShell. The aim is to unify the unit test scriptures, each preceded by its title, into a singular volume for analysis.

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

In the realm of Windows, PowerShell shall serve you well:

```powershell
cd src\unit_testing\
Get-ChildItem -Filter * | ForEach-Object {
    Add-Content -Path ..\aggregated_results.txt -Value "Filename: $($_.Name)"
    Get-Content $_.FullName | Add-Content -Path ..\aggregated_results.txt
    Add-Content -Path ..\aggregated_results.txt -Value "`n`n"
}
```

### Analyzing Results with GPT-4

With the aggregated tome at hand, prepare it as an offering to the `gpt-4-1106-preview` model. Craft a System Message to guide the model in its quest for patterns, anomalies, and a summary of the "top_p" values' efficacy.

Here's how you might commune with the aggregated results and the pre-made System Message:

```python
from src.content_generator import ContentGenerator

# Unveil the aggregated results
with open('aggregated_results.txt', 'r') as file:
    aggregated_results = file.read()

# The System Message, a prelude to analysis
system_message = """
Analyze the following test results from multiple runs of the OpenAI ChatCompletions All-Model Enhancer unit tests. Look for patterns in the AI's responses, any anomalies in the results, and provide a summary of the effectiveness of different 'top_p' values used during the tests. [UNIT TESTING RESULTS TO-BE-ANALYZED BELOW]:
"""

# Invoke the ContentGenerator with the wisdom of gpt-4-1106-preview
content_generator = ContentGenerator(model='gpt-4-1106-preview')

# Merge the System Message with the aggregated results
analysis_input = system_message + "\n\n" + aggregated_results

# Seek the analysis
analysis_output = content_generator.generate_plain_completion(analysis_input)

# Reveal the analysis results
print(analysis_output)