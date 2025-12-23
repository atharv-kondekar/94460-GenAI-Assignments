import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_sim(a,b):
    return np.dot(a,b)/ ( np.linalg.norm(a) * np.linalg.norm(b) )

model = SentenceTransformer('all-MiniLM-L6-v2')
sentences = [
    "I love Football",
    "I love cricket",
    "I hate football",
    "I drive the car"
]

embedding = model.encode(sentences)
print(" 1st vs 2nd : ",cosine_sim(embedding[0],embedding[1]))
print(" 1st vs 3rd : ",cosine_sim(embedding[0],embedding[2]))
print(" 1st vs 4th : ",cosine_sim(embedding[0],embedding[3]))