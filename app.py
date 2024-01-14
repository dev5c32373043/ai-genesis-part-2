"""Awesome chat module"""
import chainlit as cl

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores.qdrant import Qdrant
from langchain.embeddings import OllamaEmbeddings
from langchain.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Load & prepare context for LLM
loader = PyPDFLoader('data/test.pdf')
pages = loader.load()

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)

# Create our splits from the PDF
docs = r_splitter.split_documents(pages)
print(docs)

PROMPT_TEMPLATE = """[INST] Make a joke from the following text:
{text}
[/INST]
"""

# Define the prompt
prompt = PromptTemplate(input_variables=["text"], template=PROMPT_TEMPLATE)

# Set up Ollama Embeddings
embeddings = OllamaEmbeddings(model='mistral:instruct')

# Set up Qdrant database
qdrant = Qdrant.from_documents(
  docs,
  embeddings,
  location=":memory:",  # Local mode with in-memory storage only
  collection_name="test",
)

# Initialize chat model
llm = ChatOllama(model="mistral:instruct", temperature=1)

def init_qa_chain():
    """Init of question-answering chain"""
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    qa = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=qdrant.as_retriever(),
        memory=memory
    )

    return qa

@cl.on_chat_start
async def session_start():
    """Startup of the chat session"""
    qa_chain = init_qa_chain()
    cl.user_session.set("qa_chain", qa_chain)

@cl.on_message
async def main(message: cl.Message):
    """Incoming message handling"""
    try:
        qa_chain = cl.user_session.get("qa_chain")
        cb = cl.AsyncLangchainCallbackHandler(
          stream_final_answer=True,
          answer_prefix_tokens=["FINAL", "ANSWER"]
        )

        print(f"question: {message.content}")

        complete_message = prompt.format(text=message.content)
        response = await qa_chain.acall(complete_message, callbacks=[cb])
        answer = response["answer"]

        print(f"answer: {answer}")

        await cl.Message(content=answer).send()
    except Exception as ex:
        print(f"Exception: {ex}")
        await cl.Message(content="Oops... Our Bot needs some rest. Please try again later 👨‍🔧").send()
