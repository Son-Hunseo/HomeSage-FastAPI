from langchain_openai import ChatOpenAI
from util.keys.api_key import get_openai_apikey
from util.embedding.load_vector_store_faiss import load_vector_store
from langchain.chains.combine_documents import create_stuff_documents_chain
from model.analyze.Dto import RequestRegisteredAnalyzeDto, RequestLedgerAnalyzeDto
from service.analyze.analyze_prompt_template import get_registered_analyze_prompt_template, get_ledger_analyze_prompt_template
from service.analyze.static_analyze_prompt import registered_prompt, ledger_prompt
import json

def get_registered_analyze_ai_response(requestRegisteredAnalyzeDto: RequestRegisteredAnalyzeDto):

    # llm
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=get_openai_apikey(),
    )

    llm.bind(resonse_format={"type": "json_object"}), ## 이게 JSON 응답을 위한 핵심, LangChain output parser를 쓰는게 아닌 openai api 스펙에 나온 파라미터 넣어주기)

    prompt_template = get_registered_analyze_prompt_template()

    term_vector_store = load_vector_store("./util/data/vector_store/term_faiss_index")
    fraud_vector_store = load_vector_store("./util/data/vector_store/prevention_fraud_faiss_index")

    term_retriever = term_vector_store.as_retriever()
    fraud_retriever = fraud_vector_store.as_retriever()

    document_chain = create_stuff_documents_chain(llm, prompt_template)

    result = document_chain.invoke(
        {
            "registered_prompt": registered_prompt,
            "context": term_retriever.invoke(requestRegisteredAnalyzeDto.registered_text),
            "fraud_context": fraud_retriever.invoke(requestRegisteredAnalyzeDto.registered_text),
            "registered_text": requestRegisteredAnalyzeDto.registered_text,
        }
    )

    return my_custom_parser(result)

def get_ledger_analyze_ai_response(requestLedgerAnalyzeDto: RequestLedgerAnalyzeDto):

    # llm
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=get_openai_apikey(),
    )

    llm.bind(resonse_format={"type": "json_object"}),  ## 이게 JSON 응답을 위한 핵심, LangChain output parser를 쓰는게 아닌 openai api 스펙에 나온 파라미터 넣어주기)

    prompt_template = get_ledger_analyze_prompt_template()

    term_vector_store = load_vector_store("./util/data/vector_store/term_faiss_index")
    fraud_vector_store = load_vector_store("./util/data/vector_store/prevention_fraud_faiss_index")

    term_retriever = term_vector_store.as_retriever()
    fraud_retriever = fraud_vector_store.as_retriever() # 건축물 대장 분석에서는 사기 분석 여지가 비교적 적으므로 문맥 2개정도만

    document_chain = create_stuff_documents_chain(llm, prompt_template)

    result = document_chain.invoke(
        {
            "ledger_prompt": ledger_prompt,
            "context": term_retriever.invoke(requestLedgerAnalyzeDto.ledger_text),
            "fraud_context": fraud_retriever.invoke(requestLedgerAnalyzeDto.ledger_text),
            "ledger_text": requestLedgerAnalyzeDto.ledger_text,
        }
    )

    return my_custom_parser(result)


# 출력에 코드블럭 백틱이 포함되서 나오는 것을 없애기 위한 파서 및 json 검증기
def my_custom_parser(ai_response:str):
    try:
        # 문자열에서 JSON 부분 찾기
        # `str.replace()`를 통해 백틱 제거
        json_str = ai_response.replace('```json', '').replace('```', '')

        # JSON 파싱
        parsed_json = json.loads(json_str.strip())

        return parsed_json

    except json.JSONDecodeError as e:
        print("Invalid JSON format:", e)