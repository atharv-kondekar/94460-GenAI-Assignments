from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings

llm = init_embeddings(
    model="text-embedding-all-minilm-l6-v2-embedding",
    provider="openai", # Langchain openai
    base_url="http://127.0.0.1:1234/v1",
    api_key="not needed",
    check_embedding_ctx_length=False
)

def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load() # returns the list of the documents

    content = ""

    for page in docs :
        content = content + page.page_content
    
    metadata = {
        "source":pdf_path,
        "page_count":len(docs)
    }

    return content , metadata


path =r"D:/Intrenship/94460-GenAI-Assignments/Day 08/resume-003.pdf"



resume_text ,  resume_info = load_pdf(path)
print("The Metadata : ➡️",resume_info)
print("The Actual Data ✅: ",resume_text)


resume_embeddings = llm.embed_documents([resume_text])
for vect in resume_embeddings :
    print(f"Len :{len(vect)} --> {resume_embeddings[:4]} ")