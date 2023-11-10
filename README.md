# OpenAI ChatCompletions All-Model Enhancer (Cost Reduction, Quality Enhancement)

Welcome to the OpenAI ChatCompletions API Wrapper, an intuitive Python tool designed to simplify the process of generating prompts using OpenAI's powerful ChatCompletions API. This wrapper leverages the tree-of-thought prompting technique to enhance the quality of interactions with AI models. It's perfect for developers and researchers looking to explore the capabilities of language models or integrate them into their applications.

You need not produce complicated queries, but instead, simply a few sentences. All history is *privately* saved and can be used later on. With the power of the System Message, this tool enhances output substantially by iteratively producing more context.

## Key Features

- **Prompt Generation**: Utilize the ChatCompletions API to create prompts from a single sentence, or as much as you'd like.
- **Interactive Querying**: Engage in an endless conversation with customizable query modes.
- **Unit Testing**: Test different temperature settings to ensure robustness.
- **Save Functionality**: Automatically save generated prompts and answers for later review.
- **Customization**: Tailor the model, temperature, and other parameters to your needs.
- **[COMING SOON]**: A comprehensive website and mobile application for an enhanced user experience.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Virtual environment (venv)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/alexfacehead/EasyGPT-3.5
cd EasyGPT-3.5
```

2. Set up a virtual environment:

```bash
# macOS and Linux
python3 -m venv env
source env/bin/activate

# Windows
py -m venv env
.\env\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

Rename the `.env` file based on the `.env.template` provided and populate it with your OpenAI API key and other optional settings. The only essentials are the key and model:

```plaintext
OPENAI_API_KEY=yourapikey
MODEL=gpt-3.5-turbo-16k
TEMPERATURE=0.33
QUERY_MODE=False
SUPER_CHARGED=False
PROMPT_DIR=resources/prompts
TOP_P=0.5
```

### Usage

Run the main script with optional arguments (if your `.env` file is populated, you don't need flags, but flags override `.env`:

```bash
python main.py --model="gpt-3.5-turbo-16k" --temperature=0.33 --query_mode=True
```

Follow the prompts to input your question. The generated content will be saved in the specified directory.

### Running Tests

To execute unit tests and generate prompts for a range of temperatures:

```bash
python run_tests.py
```

Customize the testing parameters by setting the appropriate environment variables in the `.env` file.

## Contributing

We welcome contributions from the community! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to make contributions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, questions, or to join the community, please reach out to us at alexfacehead@hotmail.com with subject line "EASYGPT"

## Frequently Asked Questions

For a list of common questions and troubleshooting tips, please refer to our [FAQ.md](FAQ.md) document.