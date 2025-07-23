# # rag_chain.py
#from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from data_loader import load_vectorstore
# from model_loader_ import load_model

# def get_rag_chain(query: str):
#     vectorstore = load_vectorstore()
#     retriever = vectorstore.as_retriever()

# # Define the prompt template
#     prompt_template = PromptTemplate(
#         input_variables=["context", "question"],
#         template=(
#             "Use the following context to answer the question as accurately as possible.\n\n"
#             "Context:\n{context}\n\n"
#             "Question:\n{question}\n\n"
#             "Answer:"
#         )
#     )

#     llm = load_model()  # Don't pass query or history here

#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever,
#         chain_type_kwargs={"prompt": prompt_template},
#         return_source_documents=True
#     )

#     result = qa_chain(query)  # Now returns a dict with answer and source_documents
#     return result


################################################# both are working above is  without page content and below is giving all data with 
# rag_chain.py
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from Data_loader import load_vectorstore
from Model_loader import load_model

def get_rag_chain(query: str):
    # Load vector store and retriever
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever()

    # 🔍 Manually retrieve documents and build context
    retrieved_docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    # 🧠 Prompt template
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "Use the following context to answer the question as accurately as possible.\n\n"
            "Context:\n{context}\n\n"
            "Question:\n{question}\n\n"
            "Answer:"
        )
    )

    # Load model (your CustomChatLLM or similar)
    llm = load_model()

    # 🔗 Build LLMChain with prompt
    chain = LLMChain(llm=llm, prompt=prompt_template)
 
    # Invoke the chain
    answer = chain.invoke({"context": context, "question": query})

    return {
        "answer": answer["text"],
        "source_documents": retrieved_docs  # Optional for tracing/debugging
    }
