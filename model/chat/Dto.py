from typing import List, Optional
from pydantic import BaseModel
from model.chat.Entity import BaseChatEntity

class RequestChatDto(BaseModel):
    chat_history: Optional[List[BaseChatEntity]]
    message: str

class ResponseChatDto(BaseModel):
    message: str