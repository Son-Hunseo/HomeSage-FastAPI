from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from util.keys.api_key import get_openai_apikey
from service.chat.chat_prompt_template import get_chat_prompt_template
from util.embedding.load_vector_store_faiss import load_vector_store
from langchain.chains.combine_documents import create_stuff_documents_chain
from model.chat.Dto import RequestChatDto, ResponseChatDto

def get_chat_ai_response(requestChatDto: RequestChatDto):

    message_list = []

    # 이전 대화 기록이 없다면 현재 메시지만 주입
    if requestChatDto.chat_history == None:
        message_list = [HumanMessage(content=requestChatDto.message)]

    # 이전 대화 기록이 있다면 이전 발화까지 같이 주입 (스프링 백엔드에서 최대 최근 5개만 주입)
    else:
        for message in requestChatDto.chat_history:
            if message.type == "Human":
                message_list.append(HumanMessage(content=message.chat_body))
            else:
                message_list.append(AIMessage(content=message.chat_body))

        message_list.append(HumanMessage(content=requestChatDto.message))

    # llm
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=get_openai_apikey(),
    )

    prompt_template = get_chat_prompt_template()

    term_vector_store = load_vector_store("./util/data/vector_store/term_faiss_index")
    fraud_vector_store = load_vector_store("./util/data/vector_store/prevention_fraud_faiss_index")

    term_retriever = term_vector_store.as_retriever()
    fraud_retriever = fraud_vector_store.as_retriever()

    document_chain = create_stuff_documents_chain(llm, prompt_template)

    result = document_chain.invoke(
        {
            "context": term_retriever.invoke(requestChatDto.message) + fraud_retriever.invoke(requestChatDto.message),
            "messages": message_list
        }
    )

    return ResponseChatDto(message=result)