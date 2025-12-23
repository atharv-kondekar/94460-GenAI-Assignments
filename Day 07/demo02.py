from langchain_openai import OpenAIEmbeddings
import numpy as np

def cosine_sim(a,b):
    return np.dot(a,b) / ( np.linalg.norm(a) * np.linalg.norm(b) )

embedding_model = OpenAIEmbeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummy",
    check_embedding_ctx_length=False
)

sentences = [
    "I love to play cricekt ",
    "I Love all sports",
    "I Love football",
    "I hate football"
]


embeddings = embedding_model.embed_documents(sentences)

for vect in embeddings:
    print(" Len  : ",len(vect),"-->",vect[:4])

print("Sentence 1 & 2 similarity:", cosine_sim(embeddings[0], embeddings[1]))
print("Sentence 1 & 3 similarity:", cosine_sim(embeddings[0], embeddings[2]))
print("Sentence 1 & 4 similarity:", cosine_sim(embeddings[0], embeddings[3]))
print("Sentence 3 & 4 similarity:", cosine_sim(embeddings[2], embeddings[3]))