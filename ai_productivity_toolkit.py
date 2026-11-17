
# Module 02 - AI Productivity Toolkit
# Codomax Digital Solutions

def summarize_text(text):
    return f"""
Summarize the following text into 3 bullet points:
{text}
"""

def write_email(purpose, tone="Professional"):
    return f"""
Write a business email.
Purpose: {purpose}
Tone: {tone}
Include a suitable subject and professional closing.
"""

def coding_assistant(task):
    return f"""
Act as a senior C# developer.
Task: {task}
Provide clean code, explanation, and error handling.
"""

def research_assistant(topic):
    return f"""
Act as a research assistant.
Research topic: {topic}
Provide introduction, findings, benefits,
challenges, and conclusion.
"""


if __name__ == "__main__":

    print("AI PRODUCTIVITY TOOLKIT")
    print("=======================")

    print("\n1. SUMMARIZATION")
    print(summarize_text(
        "Generative AI improves developer productivity."
    ))

    print("\n2. EMAIL WRITING")
    print(write_email("Request a project status update"))

    print("\n3. CODING ASSISTANT")
    print(coding_assistant(
        "Create a C# method to retrieve an order by ID"
    ))

    print("\n4. RESEARCH ASSISTANT")
    print(research_assistant(
        "Generative AI in software development"
    ))
