from fastapi import FastAPI, UploadFile, File
from video_processor import process_video
from chat_agent import get_summary, ask_followup

app = FastAPI()

@app.post("/upload-video/")
async def upload_video(file: UploadFile = File(...)):
    with open("temp_video.mp4", "wb") as f:
        f.write(await file.read())
    
    events = process_video("temp_video.mp4")
    summary = get_summary(events)

    return {
        "events": events,
        "summary": summary
    }

@app.post("/ask/")
async def follow_up(q: str):
    return {"reply": ask_followup(q)}
