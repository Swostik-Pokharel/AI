

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

texts = [input("Enter first phrase: "), input("Enter second phrase: ")]
vecs = TfidfVectorizer().fit_transform(texts)
sim = cosine_similarity(vecs)
print(f"Similarity: {sim[0,1] * 100:.2f}%")
