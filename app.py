import streamlit as st
from video_processor import process_video
from chat_agent import get_summary, ask_followup
from dotenv import load_dotenv
load_dotenv()

from chat_agent import get_summary, ask_followup

st.set_page_config(page_title="Video Understanding Assistant", layout="wide")

st.title("🎥 Video Understanding Chat Assistant")

# Upload video
video_file = st.file_uploader("Upload a video (max 2 minutes)", type=["mp4", "avi", "mov"])

if video_file is not None:
    with open("uploaded_video.mp4", "wb") as f:
        f.write(video_file.read())

    st.video("uploaded_video.mp4")

    if st.button("Process Video"):
        with st.spinner("Analyzing video..."):
            events = process_video("uploaded_video.mp4")
            summary = get_summary(events)

        st.success("Processing complete!")

        st.subheader("📌 Detected Events")
        st.write("\n".join(events))

        st.subheader("📝 Summary with Violations")
        st.write(summary)

        st.session_state["events"] = events
        st.session_state["summary"] = summary

# Multi-turn chat
if "summary" in st.session_state:
    st.subheader("💬 Ask a follow-up question")

    user_query = st.text_input("Your question", placeholder="E.g., What happened at 15 seconds?")
    if user_query:
        context = st.session_state.get("summary", "")
        response = ask_followup(context, user_query)
        st.markdown(f"**Assistant:** {response}")
