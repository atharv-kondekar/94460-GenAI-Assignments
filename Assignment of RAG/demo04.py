from  langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

llm = init_embeddings(
     model="text-embedding-all-minilm-l6-v2-embedding",
     provider="openai",
     base_url = "http://127.0.0.1:1234/v1",
     api_key = "not needed",
     check_embedding_ctx_length=False
)

def load_pdf(path):
    loader = PyPDFLoader(path)
    resume = loader.load()

    content=""

    for page in resume :
        content = content+page.page_content
    
    metadata={
        "source":path,
        "page-count":len(resume)
    }

    return resume , metadata

path =r"D:/Intrenship/94460-GenAI-Assignments/Day 08/resume-003.pdf"

resume_data , resume_info = load_pdf(path)

print("The Resume Metadata ",resume_info)
print("The Resume Data : ",resume_data)

text_splitter = RecursiveCharacterTextSplitter(chunk_size =300 , chunk_overlap = 30 , separators = [" ","\n","\n\n"] )

# chunks = text_splitter.create_documents(resume_data)

chunks = text_splitter.split_documents(resume_data)
print("Total Chunks : ",len(chunks))

vector_store=FAISS.from_documents(
    documents = chunks,
    embedding = llm
)

query = "What is the Programming language does the Candidate know ?"
k = 3 

docs  = vector_store.similarity_search(query,k)

for i,doc in enumerate(docs):
    print(f"\nResult {i+1} --->\n{doc.page_content}")