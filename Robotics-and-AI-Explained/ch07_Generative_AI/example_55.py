# Bag-of-words vectors and cosine similarity
import numpy as np
from sklearn.feature_extraction import text as fx

sentences = ["the robot picks up the red box",
             "a robot lifts a red box",
             "the cat sleeps on the sofa"]
vec = fx.CountVectorizer(stop_words="english")
X = vec.fit_transform(sentences).toarray()

def cosine(a, b):
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))

print("1 vs 2:", round(cosine(X[0], X[1]), 2))
print("1 vs 3:", round(cosine(X[0], X[2]), 2))
print("vocabulary size:", len(vec.vocabulary_))
