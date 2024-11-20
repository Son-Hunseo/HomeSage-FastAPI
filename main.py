from fastapi import FastAPI, HTTPException
from model.chat.Dto import RequestChatDto
from model.analyze.Dto import RequestRegisteredAnalyzeDto, RequestLedgerAnalyzeDto
from service.chat.chat import get_chat_ai_response
from service.analyze.analyze import get_registered_analyze_ai_response, get_ledger_analyze_ai_response

app = FastAPI()

@app.post("/chat")
async def chat(requestChatDto: RequestChatDto):
    if requestChatDto.message.strip() == "":
        raise HTTPException(status_code=400, detail="빈 입력 요청")
    return get_chat_ai_response(requestChatDto)

@app.post("/analyze/registered")
async def analyze_registered(requestRegisteredAnalyzeDto: RequestRegisteredAnalyzeDto):
    if requestRegisteredAnalyzeDto.registered_text.strip() == "":
        raise HTTPException(status_code=400, detail="빈 입력 요청")
    return get_registered_analyze_ai_response(requestRegisteredAnalyzeDto)

@app.post("/analyze/ledger")
async def analyze_ledger(requestLedgerAnalyzeDto: RequestLedgerAnalyzeDto):
    if requestLedgerAnalyzeDto.ledger_text.strip() == "":
        raise HTTPException(status_code=400, detail="빈 입력 요청")
    return get_ledger_analyze_ai_response(requestLedgerAnalyzeDto)