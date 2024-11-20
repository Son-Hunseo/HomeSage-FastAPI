from pydantic import BaseModel

class RequestRegisteredAnalyzeDto(BaseModel):
    registered_text: str

class ResponseRegisteredAnalyzeDto(BaseModel):
    result: str

class RequestLedgerAnalyzeDto(BaseModel):
    ledger_text: str

class ResponseLedgerAnalyzeDto(BaseModel):
    result: str
