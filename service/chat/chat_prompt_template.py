from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_chat_prompt_template():

    SYSTEM_TEMPLATE = """
    너는 부동산 전문가야. 
    context를 근거로 질문에 답변해줘
    어떠한 근거로 그러한 대답을 했는지, step by step으로 설명해줘. (사례, 혹은 예시가 있다면 이를 언급)
    
    <context>
    {context}
    </context>
    """

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                SYSTEM_TEMPLATE,
            ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )