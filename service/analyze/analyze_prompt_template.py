from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_analyze_prompt_template():
    SYSTEM_TEMPLATE = """
    너는 부동산 전문가야.
    아래 사항들을 참고해서 해당 부동산에 대한 계약을 할 때, 주의해야할 점들을 분석해서 알려줘.
    
    {registered_prompt}
    
    {ledger_prompt}
    
    ## 참고 자료
    
    ### 부동산 용어
    {context}
    
    ### 전세사기 사례 및 주의점
    {fraud_context}
    
    # 제시된 등기부 등본
    {registered_text}

    # 제시된 건축물 대장
    {ledger_text}
    """

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                SYSTEM_TEMPLATE,
            ),
        ]
    )