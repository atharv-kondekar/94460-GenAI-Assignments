from langchain.embeddings import init_embeddings
import numpy as np 

llm = init_embeddings(
    model="text-embedding-all-minilm-l6-v2-embedding",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not needed",
    check_embedding_ctx_length=False
)

def cosine_sim(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b) )

sentences =[
    "I like Artificial Intelligence",
    "Generative AI is magnificant",
    "World is amazing"
]

embeddings = llm.embed_documents(sentences)

for vtr in embeddings:
    print(f"Length {len(vtr)} --> {embeddings[:4]} ")

print("Senetnce 1 vs Sentence 2 : ",cosine_sim(embeddings[0] , embeddings [1]))
print("Senetnce 1 vs Sentence 3 : ",cosine_sim(embeddings[0] , embeddings [2]))