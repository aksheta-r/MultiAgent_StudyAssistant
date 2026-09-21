from langchain_google_genai import ChatGoogleGenerativeAI

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="AIzaSyBUbnfpHJeYSe4_z7rRCZjjnP-q3a1bzII"
)

# ---------------- EXPLAINER AGENT ----------------

def explainer_agent(context, query):

    prompt = f"""
    You are an academic AI tutor.

    Using the given context:

    1. Explain the topic clearly
    2. Break down key concepts
    3. Give simple examples
    4. Highlight important notes

    Context:
    {context}

    Question:
    {query}
    """

    return llm.predict(prompt)


# ---------------- SUMMARY AGENT ----------------

def summary_agent(context):

    prompt = f"""
    Summarize the following academic content.

    Format:
    - Chapter Summary
    - Key Points
    - Important Definitions

    Context:
    {context}
    """

    return llm.predict(prompt)


# ---------------- QUIZ AGENT ----------------

def quiz_agent(context):

    prompt = f"""
    Generate a quiz from the following content.

    Include:
    - 3 MCQs
    - 2 Short Questions
    - Answers

    Context:
    {context}
    """

    return llm.predict(prompt)


# ---------------- EVALUATOR AGENT ----------------

def evaluator_agent(response):

    prompt = f"""
    Improve formatting, clarity, and readability
    of the following response.

    Response:
    {response}
    """

    return llm.predict(prompt)