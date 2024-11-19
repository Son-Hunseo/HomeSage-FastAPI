from langchain_openai import ChatOpenAI
from util.keys.api_key import get_openai_apikey
from util.embedding.load_vector_store_faiss import load_vector_store
from langchain.chains.combine_documents import create_stuff_documents_chain
from model.analyze.Dto import RequestAnalyzeDto, ResponseAnalyzeDto
from service.analyze.analyze_prompt_template import get_analyze_prompt_template
from service.analyze.static_analyze_prompt import registered_prompt, ledger_prompt

def get_analyze_ai_response(requestAnalyzeDto: RequestAnalyzeDto):

    # llm
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=get_openai_apikey(),
    )

    prompt_template = get_analyze_prompt_template()

    term_vector_store = load_vector_store("./util/data/vector_store/term_faiss_index")
    fraud_vector_store = load_vector_store("./util/data/vector_store/prevention_fraud_faiss_index")

    term_retriever = term_vector_store.as_retriever()
    fraud_retriever = fraud_vector_store.as_retriever()

    document_chain = create_stuff_documents_chain(llm, prompt_template)

    result = document_chain.invoke(
        {
            "registered_prompt": registered_prompt,
            "ledger_prompt": ledger_prompt,
            "context": term_retriever.invoke(requestAnalyzeDto.registered_text + requestAnalyzeDto.ledger_text),
            "fraud_context": fraud_retriever.invoke(requestAnalyzeDto.registered_text + requestAnalyzeDto.ledger_text),
            "registered_text": requestAnalyzeDto.registered_text,
            "ledger_text": requestAnalyzeDto.registered_text
        }
    )

    return ResponseAnalyzeDto(result=result)