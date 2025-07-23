# from langchain.document_loaders import TextLoader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import FAISS
# # from langchain.embeddings import OpenAIEmbeddings
# from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings

# def load_vectorstore(file_path: str = "faq_data.txt"):
#     loader = TextLoader(file_path)
#     docs = loader.load()
#     splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     split_docs = splitter.split_documents(docs)

#     # embedding = OpenAIEmbeddings(openai_api_key="use you API key")
#     embedding = HuggingFaceInferenceAPIEmbeddings(api_key =" use you API_key",model_name="sentence-transformers/all-MiniLM-L6-v2")
#     vectorstore = FAISS.from_documents(split_docs, embedding)
#     return vectorstore

###########################################################below code are working
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings  # ✅ NEW import
from dotenv import load_dotenv
import os

load_dotenv()

def load_vectorstore(file_path: str = "faq_data.txt"):
    loader = TextLoader(file_path)
    docs = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    # ✅ Use updated embedding class
    embedding = HuggingFaceEndpointEmbeddings(

        model = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        huggingfacehub_api_token= os.getenv("huggingfacehub_api_token") # 🔐 Replace with real token
    )

    vectorstore = FAISS.from_documents(split_docs, embedding)
    return vectorstore
