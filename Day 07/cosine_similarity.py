import numpy as np

def cosine_sim(a,b):
    return np.dot(a,b)/ ( np.linalg.norm(a) * np.linalg.norm(b) )


cat = np.array([0.17,0.45,0.1])
dog = np.array([0.20,0.46,0.2])
car = np.array([1.4,-0.50,-0.1])

print("cat vs dog : ",cosine_sim(cat,dog))
print("dog vs car : ",cosine_sim(dog,car))
