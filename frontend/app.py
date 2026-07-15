import streamlit as st

from styles import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
)

from api import generate_report


# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "research_result" not in st.session_state:
    st.session_state.research_result = None

if "last_question" not in st.session_state:
    st.session_state.last_question = ""


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🧠 Multi-Agent Research Assistant")

st.caption(
    "AI-Powered Research using LangGraph + FastAPI"
)


# --------------------------------------------------
# Research Form
# --------------------------------------------------

with st.form("research_form"):

    question = st.text_area(
        "Research Topic",
        value=st.session_state.last_question,
        height=180,
        placeholder="Example: How is Generative AI changing healthcare?",
    )

    submitted = st.form_submit_button(
        "🚀 Generate Report",
        use_container_width=True,
    )


# --------------------------------------------------
# Generate Research
# --------------------------------------------------

if submitted:

    if not question.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("🔍 Multi-Agent System is researching..."):

        st.session_state.research_result = generate_report(question)
        st.session_state.last_question = question


# --------------------------------------------------
# Display Result
# --------------------------------------------------

if st.session_state.research_result:

    data = st.session_state.research_result

    st.success("✅ Research completed successfully!")

    st.subheader("📊 Research Metrics")

    metric1, metric2 = st.columns(2)

    with metric1:
        st.metric(
            "⏱ Execution Time",
            f"{data['execution_time']} sec",
        )

    with metric2:
        st.metric(
            "🤖 Agents Executed",
            len(data["trace"]),
        )

    st.divider()

    st.subheader("⚙ Agent Execution")

    for step in data["trace"]:

        with st.expander(
            f"✅ {step['agent']}",
            expanded=False,
        ):
            st.write(step["message"])
    st.divider()

    st.subheader("📄 Research Report")

    st.markdown(data["report"])

    download1, download2 = st.columns(2)

    with download1:

        st.download_button(
            "📥 Download Markdown",
            data=data["report"],
            file_name="research_report.md",
            mime="text/markdown",
            use_container_width=True,
        )

    with download2:

        st.button(
            "📄 PDF (Coming Soon)",
            disabled=True,
            use_container_width=True,
        )