from pydantic import BaseModel

class BaseChatEntity(BaseModel):
    type: str
    message: str

class AIChat(BaseChatEntity):
    type: str = "AI"

class HumanChat(BaseChatEntity):
    type: str = "Human"