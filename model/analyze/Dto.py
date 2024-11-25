from pydantic import BaseModel

class RequestRegisteredAnalyzeDto(BaseModel):
    registered_text: str

class RequestLedgerAnalyzeDto(BaseModel):
    ledger_text: str
