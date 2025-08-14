import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key from environment
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error(" GEMINI_API_KEY not found in environment variables. Please set it in your .env file.")
    st.stop()

# Gemini Client
class GeminiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://generativelanguage.googleapis.com/v1beta"
        self.chat = self.Chat(self)

    class Chat:
        def __init__(self, parent):
            self.parent = parent
            self.completions = self.Completions(parent)

        class Completions:
            def __init__(self, parent):
                self.parent = parent

            def create(self, model, messages):
                contents = []
                for m in messages:
                    role = "user" if m["role"] != "assistant" else "model"
                    contents.append({"role": role, "parts": [{"text": m["content"]}]})

                r = requests.post(
                    f"{self.parent.url}/models/{model}:generateContent?key={self.parent.api_key}",
                    json={
                        "contents": contents,
                        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 500}
                    }
                )

                r.raise_for_status()
                data = r.json()
                st.write("🔍 Gemini API Raw Response:", data)

                try:
                    text = data["candidates"][0]["content"]["parts"][0]["text"]
                except (KeyError, IndexError):
                    text = data.get("promptFeedback", {}).get("blockReason", "⚠️ No valid response.")

                class Msg: content = text
                class Choice: message = Msg()
                class Response: choices = [Choice()]
                return Response()


def suggest(domain, query):
    messages = [
        {"role": "user", "content": f"You are a domain expert in {domain}. Keep advice crisp, practical, and in bullet points.\n\n{query}"}
    ]
    try:
        response = client.chat.completions.create("gemini-2.5-flash", messages)
    except requests.exceptions.HTTPError:
        st.warning("⚠️ gemini-2.5-flash failed, trying gemini-1.5-flash...")
        response = client.chat.completions.create("gemini-1.5-flash", messages)

    return response.choices[0].message.content


st.set_page_config(page_title="Gemini Expert Advisor", layout="centered")
st.title("Gemini Expert Advisor")

# Initialize Gemini client
client = GeminiClient(api_key=API_KEY)

# Domain & Question Input
domain = st.selectbox("Choose your domain", ["Health", "Sports", "Tech", "Non-Tech", "Startup", "Education"])
question = st.text_area("Ask your question", placeholder="e.g. How can I build a strong startup team?")

# Button Action
if st.button("Get Expert Suggestion"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = suggest(domain, question)
        st.markdown("### 💡 Expert Advice")
        st.markdown(answer)
    else:
        st.warning("Please enter a question.")
