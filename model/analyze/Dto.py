from pydantic import BaseModel

class RequestAnalyzeDto(BaseModel):
    registered_text: str
    ledger_text: str

class ResponseAnalyzeDto(BaseModel):
    result: str