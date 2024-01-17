import PyPDFLoader, DirectoryLoader
import PromptTemplate
import HuggingFaceEmbeddings
import FAISS
import CTransformers
import RetrievalQA

DB_FAISS_PATH = 'vectorstore/db_faiss'

custom_prompt_template = """Read the pdf's in two page sections and convert them into your own knowledge corpus and provide the reasonable suggestions/solutions if available based on the given context/rulesets.

Context: {context}
Question: {question}

"""

def set_custom_prompt():
    prompt = PromptTemplate(template=custom_prompt_template,input_variables=['context', 'question'])
    return prompt

def generate_text(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(llm=llm,chain_type='stuff',retriever=db.as_retriever(search_kwargs={'k': 2}),return_source_documents=True,chain_type_kwargs={'prompt': prompt})
    return qa_chain

def load_llm():
    llm = CTransformers(
        model = "TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.5
    )
    return llm

def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)

    return qa

def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response