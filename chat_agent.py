from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Create LLM using Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def get_summary(text):
    prompt = f"Summarize this text:\n{text}"
    return llm.invoke([HumanMessage(content=prompt)]).content

def ask_followup(summary, question):
    prompt = f"Based on this summary:\n{summary}\n\nAnswer the question:\n{question}"
    return llm.invoke([HumanMessage(content=prompt)]).content
