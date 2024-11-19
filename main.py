from fastapi import FastAPI, HTTPException
from model.chat.Dto import RequestChatDto
from model.analyze.Dto import RequestAnalyzeDto
from service.chat.chat import get_chat_ai_response
from service.analyze.analyze import get_analyze_ai_response

app = FastAPI()

@app.post("/chat")
async def chat(requestChatDto: RequestChatDto):
    if requestChatDto.message.strip() == "":
        raise HTTPException(status_code=400, detail="빈 입력 요청")
    return get_chat_ai_response(requestChatDto)

@app.post("/analyze")
async def analyze(requestAnalyzeDto: RequestAnalyzeDto):
    if requestAnalyzeDto.registered_text.strip() == "" and requestAnalyzeDto.ledger_text.strip() == "":
        raise HTTPException(status_code=400, detail="빈 입력 요청")
    return get_analyze_ai_response(requestAnalyzeDto)