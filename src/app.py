import datetime
import logging
import os
import sys
import uuid
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import Chroma
from langchain.schema.document import Document
from langchain.memory.buffer import ConversationBufferMemory
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from api_request import openstack_request
from openai import OpenAI
from constants import CLIENT_ERROR_MSG, LOG


def initiate_sessions():
    global sessions
    sessions = {}


def get_session(session_id):
    return sessions.get(session_id)


def new_session(model, temperature):
    # Create vectorstore
    llm = ChatOpenAI(
        model_name=model,
        temperature=float(temperature),
        openai_api_key=OPENAI_API_KEY)
    session_id = str(uuid.uuid4())
    memory, retriever = create_vectorstore(llm)
    # Create chat response generator
    generator = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=retriever,
                memory=memory)

    # Give the LLM date time context
    query = f"From now on you will use {datetime.datetime.now()} as current datetime for any datetime related user query"
    generator.invoke(query)

    # Add session to sessions map
    sessions[session_id] = {"generator": generator, "llm": llm, "id": session_id}
    LOG.info(f"New session with ID: {session_id} initiated. Model: {model}, Temperature: {temperature}")
    return sessions[session_id]


def create_logger():
    # Create logger
    LOG = logging.getLogger("chatbot")
    LOG.setLevel(logging.INFO)

    # Create a file handler and set its level to INFO
    file_handler = logging.FileHandler('chatbot.log')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    LOG.addHandler(file_handler)
    LOG.info("Chatbot logger initiated.")


def create_vectorstore(llm):
    # Create Chroma vector store
    data_start = "start vectorstore"
    docs = [Document(page_content=x) for x in data_start]
    vectorstore = Chroma.from_documents(documents=docs, embedding=OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY))

    memory = ConversationBufferMemory(
    llm=llm, memory_key="chat_history", return_messages=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

    return memory, retriever


def ask(query, session):
    query_completion = query + ". If an API response is provided as context and in the provided API response doesn't have this information or no context is provided, make sure that your response is 'I don't know'. Unless the user explicitly ask for commands you will not provide any. Make sure to read the entire given context before giving your response."
    LOG.info(f"User query: {query}")
    response = session['generator'].invoke(query_completion)

    print(f'######{response}', file=sys.stderr)
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt_status = client.chat.completions.create(model='gpt-3.5-turbo',
                                                   messages=[{"role": "system",
                                                              "content": "Your task is to understand the context of a text. Look for clues indicating whether the text provides information about a subject. If you come across phrases such as 'I'm sorry', 'no context', 'no information', or 'I don't know', it likely means there isn't enough information available. Similarly, if the text mentions not having access to the information, or if it offers directives without the user requesting them explicitly, the context is negative."},
                                                             {"role": "user",
                                                              "content": f"Based on the following text, check if the general context indicates that there is information about what is being asked or not. Make sure to answer only the words 'positive' if there is information, or 'negative' if there isn't. Don't answer nothing besides it.\nUser query {query}\nResponse: {response['answer']}"}])
    print(f'prompt status: {prompt_status.choices[0].message.content}', file=sys.stderr)
    if 'negative' in prompt_status.choices[0].message.content.lower():
        LOG.info("Negative response from LLM")
        feed_vectorstore(query, session)
        response = session['generator'].invoke(query)

    LOG.info(f"Chatbot response: {response['answer']}")
    return response['answer']


def feed_vectorstore(query, session):
    response = api_response(query, session)

    if response is None:
        raise Exception('API response is null')

    print(f'API response: {response}', file=sys.stderr)

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_text(response)
    docs = [Document(page_content=x) for x in all_splits]
    vectorstore = Chroma.from_documents(documents=docs, embedding=OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY))

    llm = session['llm']

    memory = ConversationBufferMemory(
    llm=llm, memory_key="chat_history", return_messages=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

    sessions[session['id']]['generator'] = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=retriever,
                memory=memory)


def set_openai_key():
    create_logger()
    try:
        global OPENAI_API_KEY
        OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
        is_api_key_valid(OPENAI_API_KEY)
    except Exception:
        raise Exception("Error while trying to set OpenAI API Key variable")
    LOG.info("API key configured")
    return True


def is_api_key_valid(key):
    try:
        client = OpenAI(api_key=key)
        _ = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "This is a test."}],
            max_tokens=5
        )
    except Exception:
        raise Exception("The provided key is not valid.")
    return True


def api_response(query, session):
    pool = "OpenStack"
    print(f'LLM defined {pool} as the API subject', file=sys.stderr)
    LOG.info(f'LLM defined {pool} as the API subject')
    if pool == "OpenStack":
        bot = openstack_request(query, OPENAI_API_KEY)
        response = openstack_request.get_API_response(bot)
    else:
        response = CLIENT_ERROR_MSG

    return response
