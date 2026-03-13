# EasyGPT

A context-enrichment pipeline that iteratively builds rich background context from sparse inputs, then generates a task-adaptive system message to steer any OpenAI model toward better answers.

## How It Works

The pipeline runs 5 steps on every question:

1. **Question Refinement** — fixes grammar, resolves ambiguity
2. **Topic Generation** — produces a list of distinct, related topics
3. **Context Expansion** — synthesizes topics into rich background prose
4. **Adaptive System Message** — analyzes the question type (debugging, explanation, analysis, etc.) and generates a tailored system message using the expanded context
5. **Final Answer** — answers the question with the enriched system message steering the model

## Getting Started

### Prerequisites

- Python 3.9+
- An OpenAI API key

### Installation

```bash
git clone https://github.com/alexfacehead/EasyGPT-3.5
cd EasyGPT-3.5
python3 -m venv my_venv
source my_venv/bin/activate
pip install -r requirements.txt
```

### Configuration

Copy `.env.template` to `.env` and add your API key:

```
OPENAI_API_KEY=sk-your-key-here
MODEL=gpt-5.1-mini
PIPELINE_MODEL=gpt-5.1
TEMPERATURE=0.33
TOP_P=0.5
QUERY_MODE=False
```

- `MODEL` — used for follow-up queries and file naming (cheaper)
- `PIPELINE_MODEL` — used for the 5 pipeline steps (more capable)

### Usage

#### Web UI (recommended)

```bash
streamlit run app.py
```

Opens a browser with a text area that handles multi-line paste (including code), shows pipeline progress, and supports follow-up chat.

#### CLI

```bash
python main.py
```

Optional flags (override `.env`):

```bash
python main.py --model gpt-5.1-mini --pipeline_model gpt-5.1 --temperature 0.33 --query_mode
```

### Running Tests

Test the pipeline across a range of `top_p` values:

```bash
python run_tests.py
```

Configure test parameters in `.env`:

```
QUESTION='What is the integral of e^3x?'
TEMP_START_VALUE=0.07
TEMP_RANGE=10
SAVE_DIR=src/unit_testing/unit_test_results
REPEAT=1
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE).

## Support

For questions, reach out at alexfacehead@hotmail.com with subject line "EASYGPT".

## FAQ

See [FAQ.md](FAQ.md).
