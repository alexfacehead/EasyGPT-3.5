import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

from src.content_generator import ContentGenerator
from src.utils.file_handler import FileManager

# ── Page config ──────────────────────────────────────────────────────
st.set_page_config(page_title="EasyGPT", page_icon="*", layout="centered")

st.markdown("""
<style>
    .stApp { max-width: 900px; margin: 0 auto; }
    .pipeline-step { padding: 0.5rem 0; border-bottom: 1px solid #333; }
</style>
""", unsafe_allow_html=True)

st.title("EasyGPT")
st.caption("Context-enrichment pipeline with adaptive system messages")

# ── Sidebar config ───────────────────────────────────────────────────
with st.sidebar:
    st.header("Configuration")

    api_key = st.text_input("OpenAI API Key", value=os.getenv("OPENAI_API_KEY", ""), type="password")
    model = st.text_input("Default Model", value=os.getenv("MODEL", "gpt-5.1-mini"))
    pipeline_model = st.text_input("Pipeline Model", value=os.getenv("PIPELINE_MODEL", "gpt-5.1"))
    temperature = st.slider("Temperature", 0.0, 2.0, float(os.getenv("TEMPERATURE", "0.33")), 0.01)
    top_p = st.slider("Top P", 0.0, 1.0, float(os.getenv("TOP_P", "0.5")), 0.01)
    prompt_dir = st.text_input("Save Directory", value=os.getenv("PROMPT_DIR", "resources/prompts"))

    st.divider()
    st.caption(f"Pipeline: **{pipeline_model}**")
    st.caption(f"Follow-ups: **{model}**")

# ── Session state ────────────────────────────────────────────────────
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "pipeline_ran" not in st.session_state:
    st.session_state.pipeline_ran = False

# ── Main input ───────────────────────────────────────────────────────
question = st.text_area(
    "Enter your question (code paste works here):",
    height=150,
    placeholder="Paste code, ask a question, or both...",
)

run_pipeline = st.button("Run Pipeline", type="primary", disabled=not question or not api_key)

if run_pipeline and question and api_key:
    st.session_state.conversation = []
    st.session_state.pipeline_ran = False

    generator = ContentGenerator(
        api_key=api_key,
        model=model,
        pipeline_model=pipeline_model,
        temperature=temperature,
        top_p=top_p,
    )

    # Step-by-step pipeline with progress
    progress = st.empty()
    details = st.expander("Pipeline Details", expanded=False)

    with details:
        progress.progress(0.0, text="Step 1/5: Fixing question...")
        perfected = generator.perfect_question(question)
        st.markdown("**Perfected Question:**")
        st.info(perfected)

        progress.progress(0.2, text="Step 2/5: Generating initial context...")
        initial_ctx = generator.make_initial_context(perfected)
        st.markdown("**Initial Context (topics):**")
        st.info(initial_ctx)

        progress.progress(0.4, text="Step 3/5: Expanding context...")
        expanded_ctx = generator.expand_context(initial_ctx)
        st.markdown("**Expanded Context:**")
        st.info(expanded_ctx)

        progress.progress(0.6, text="Step 4/5: Building adaptive system message...")
        system_message = generator.generate_system_message(expanded_ctx, perfected)
        st.markdown("**System Message:**")
        st.code(system_message, language=None)

        progress.progress(0.8, text="Step 5/5: Generating final answer...")
        final_answer = generator.get_final_answer(system_message, perfected)

    progress.progress(1.0, text="Done!")

    # Display answer
    st.divider()
    st.markdown("### Answer")
    st.markdown(final_answer)

    # Save conversation
    conversation = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": question},
        {"role": "assistant", "content": final_answer},
    ]
    st.session_state.conversation = conversation
    st.session_state.pipeline_ran = True
    st.session_state.generator = generator

    # Save to disk
    FileManager.ensure_directory_exists(prompt_dir)
    run_num = FileManager.get_highest_run_num(prompt_dir) + 1
    FileManager.save_content(prompt_dir, "prompt_and_answer", run_num, conversation)

# ── Follow-up chat ───────────────────────────────────────────────────
if st.session_state.pipeline_ran and st.session_state.conversation:
    st.divider()
    st.markdown("### Follow-up Questions")

    # Show conversation history (skip system message)
    for msg in st.session_state.conversation:
        if msg["role"] == "system":
            continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    followup = st.chat_input("Ask a follow-up question...")
    if followup:
        with st.chat_message("user"):
            st.markdown(followup)

        generator = st.session_state.generator
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = generator.generate_plain_completion(
                    st.session_state.conversation, followup
                )
            st.markdown(answer)

        st.session_state.conversation.append({"role": "user", "content": followup})
        st.session_state.conversation.append({"role": "assistant", "content": answer})

        # Save updated conversation
        FileManager.ensure_directory_exists(prompt_dir)
        run_num = FileManager.get_highest_run_num(prompt_dir) + 1
        FileManager.save_content(prompt_dir, "prompt_and_answer", run_num,
                                 st.session_state.conversation)
