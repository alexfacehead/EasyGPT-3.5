# STEP 0: FORMAT QUESTION
QUESTION_FIXER_PART_ONE = (
    "Revise the following question for grammatical correctness, clarity, and readability "
    "while preserving the original meaning. Remove any outer quotes or backticks. "
    "Output only the revised question, nothing else.\n\n"
    "[QUESTION]:\n"
)

# STEP 0.1: SECOND HALF OF FORMATTING
QUESTION_FIXER_PART_TWO = (
    "\n\n[INSTRUCTIONS]:\n"
    "Accurately capture the intended meaning and resolve any ambiguities. "
    "Respond with only the revised question."
)

# STEP 1: CONTEXT GENERATOR
AUTOMATED_CONTEXT_CALLER = (
    "Given the following question, produce a single comma-separated list of distinct, "
    "related topics. Include both directly relevant and tangentially useful subjects — "
    "broad enough to enrich understanding, but still grounded in the question's domain.\n\n"
    "Requirements:\n"
    "- Each topic must be unique (no semantic duplicates)\n"
    "- Output a single sentence of comma-separated topics\n"
    "- Aim for breadth and quality over quantity\n\n"
    "The question:"
)

# STEP 2: EXPANSION
CONTEXT_EXPANSION = (
    "Synthesize the provided topic list into coherent, technically precise background context. "
    "The output will be integrated into a System Message for a language model, so structure it "
    "as flowing prose — not a list.\n\n"
    "Requirements:\n"
    "- Maintain the scope and intent of the original topics\n"
    "- Be concise but substantive — do not over-prune; models benefit from rich context\n"
    "- Organize coherently by theme rather than listing topics sequentially\n"
    "- Ensure accuracy and technical correctness throughout"
)

# STEP 3: ADAPTIVE SYSTEM MESSAGE GENERATOR
SYSTEM_MESSAGE_GENERATOR = (
    "You are a System Message architect. Given background context and the user's question, "
    "produce a System Message that will maximally steer a language model toward a thorough, "
    "accurate answer.\n\n"
    "Analyze the question to determine what kind of task it is (e.g. debugging, explanation, "
    "analysis, creative, mathematical, etc.) and tailor the System Message accordingly:\n\n"
    "- For technical/debugging questions: emphasize precision, step-by-step reasoning, "
    "and identifying root causes before proposing fixes\n"
    "- For explanatory questions: emphasize clarity, building from fundamentals, "
    "and connecting concepts to the reader's likely mental model\n"
    "- For analytical questions: emphasize examining multiple perspectives, "
    "weighing evidence, and distinguishing strong claims from speculation\n"
    "- For creative questions: emphasize originality, coherence, and engagement\n"
    "- For mathematical/formal questions: emphasize rigor, showing work, and verification\n\n"
    "Requirements:\n"
    "- Weave the background context naturally into the System Message\n"
    "- The System Message should be substantive — rich context steers models more effectively\n"
    "- Produce ONLY the System Message text — do not answer the question yourself\n"
    "- Do not prefix with labels like [SYSTEM MESSAGE]\n"
    "- Do not include instructions to 'act as' or role-play — just provide direct guidance "
    "and context that shapes how the model approaches the problem\n\n"
)

# FILE NAMING
FILE_FORMATTER = (
    "Convert the given statement or question into a concise Python-style filename "
    "using underscores. Preserve the key meaning.\n\n"
    "Example: \"What is 1+1?\" -> one_plus_one\n\n"
    "Output only the filename, nothing else."
)
