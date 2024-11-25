from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_registered_analyze_prompt_template():
    SYSTEM_TEMPLATE = """
    너는 부동산 전문가야.
    아래 사항들을 참고해서 해당 부동산에 대한 계약을 할 때, 주의해야할 점들을 분석해서 알려줘.
    듣는 이는 부동산에 대해서 전혀 배경 지식이 없는 사람이라고 생각하고, 쉬운 예시와 근거를 들면서 논리적으로 설명해줘
    그리고 종합적으로 판단한 등급도 측정해줘 A+, A, B+, B, C+, C, D, F 중에 하나로
    응답은 JSON 형식으로 응답해줘
    
    {{
        "result": "여기에 분석 내용 전체 내용",
        "summary": "여기에 분석 내용 요약",
        "score": "등급"
    }}
    
    {registered_prompt}
    
    ## 참고 자료
    
    ### 부동산 용어
    {context}
    
    ### 전세사기 사례 및 주의점
    {fraud_context}
    
    # 제시된 등기부 등본
    {registered_text}
    """

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                SYSTEM_TEMPLATE,
            ),
        ]
    )


def get_ledger_analyze_prompt_template():
    SYSTEM_TEMPLATE = """
    너는 부동산 전문가야.
    아래 사항들을 참고해서 해당 부동산에 대한 전반적인 설명을 해줘
    듣는 이는 부동산에 대해서 전혀 배경 지식이 없는 사람이라고 생각하고, 쉬운 예시와 근거를 들면서 논리적으로 설명해줘
    그리고 주의해야할 점이 있다면 이에대해서도 설명해줘
    그리고 종합적으로 판단한 등급도 측정해줘 A+, A, B+, B, C+, C, D, F 중에 하나로
    응답은 JSON 형식으로 응답해줘
    
    {{
        "result": "여기에 분석 내용 전체 내용",
        "summary": "여기에 분석 내용 요약",
        "score": "등급"
    }}

    {ledger_prompt}

    ## 참고 자료

    ### 부동산 용어
    {context}
    
    ### 전세사기 사례 및 주의점
    {fraud_context}

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