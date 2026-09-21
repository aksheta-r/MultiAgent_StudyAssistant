import streamlit as st

from rag import process_pdf
from agents import *
from router import router_agent

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Multi-Agent AI Study Workspace",
    layout="centered"
)

# ---------------- LOAD CSS ----------------

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- TITLE ----------------

st.title("🧠 Multi-Agent AI Study Workspace")

st.markdown("""
An intelligent multi-agent learning assistant powered by
RAG, Vector Databases, and AI Agents.
""")

st.markdown("---")

# ---------------- FILE UPLOAD ----------------

uploaded_file = st.file_uploader(
    "📂 Upload Academic PDF",
    type=["pdf"]
)

vectordb = None

# ---------------- PROCESS PDF ----------------

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("📚 Processing academic document..."):

        vectordb = process_pdf("temp.pdf")

    st.success("✅ Document processed successfully!")

    st.markdown("---")

    # ---------------- TASK SELECTION ----------------

    st.subheader("🎯 Select Learning Task")

    task = st.radio(
        "",
        [
            "Explain Topic",
            "Generate Summary",
            "Generate Quiz"
        ]
    )

    # ---------------- DYNAMIC INPUT ----------------

    query = ""

    if task == "Explain Topic":

        query = st.text_input(
            "📘 Enter topic or concept",
            placeholder="Example: Explain Neural Networks"
        )

    elif task == "Generate Quiz":

        query = st.text_input(
            "❓ Enter topic for quiz (optional)",
            placeholder="Example: Deep Learning"
        )

    # ---------------- GENERATE BUTTON ----------------

    generate = st.button("🚀 Generate Response")

    st.markdown("---")

    # ---------------- RESPONSE GENERATION ----------------

    if generate:

        with st.spinner("🔍 Retrieving relevant content..."):

            retriever = vectordb.as_retriever()

            if query.strip() == "":
                query = "Generate response from uploaded document"

            docs = retriever.invoke(query)

            context = "\n".join(
                [doc.page_content for doc in docs]
            )

        st.info("🧠 Router Agent analyzing task...")

        route = router_agent(task)

        # ---------------- EXPLAINER ----------------

        if route == "explainer":

            st.info("📘 Explainer Agent generating response...")

            response = explainer_agent(
                context,
                query
            )

        # ---------------- SUMMARY ----------------

        elif route == "summary":

            st.info("📝 Summary Agent generating response...")

            response = summary_agent(context)

        # ---------------- QUIZ ----------------

        elif route == "quiz":

            st.info("❓ Quiz Agent generating response...")

            response = quiz_agent(context)

        # ---------------- EVALUATOR ----------------

        st.info("✅ Evaluator Agent validating output...")

        final_response = evaluator_agent(response)

        st.markdown("---")

        st.subheader("📄 AI Response")

        st.write(final_response)

else:

    st.info("📂 Upload a PDF document to begin.")