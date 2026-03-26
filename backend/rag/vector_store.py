import numpy as np
from .embedding import get_embedding

class SimpleVectorStore:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, nodes):
        for i,node in  enumerate( nodes):
            print(f"processing node {i}")
            emb = get_embedding(node.text)

            if emb is node:
                print("embeding failed!")

            self.vectors.append(emb)
            self.texts.append(node.text)

    def search(self, query, top_k=3):
        query_emb= get_embedding(query)

        similarities = []

        for i, vec in enumerate(self.vectors):
            score = np.dot(query_emb, vec) / (np.linalg.norm(query_emb)*np.linalg.norm(vec))
            similarities.append(score, self.texts[i])
        similarities.sort(reverse=True)
        return [text for _, text in similarities[:top_k]]