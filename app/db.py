import faiss
import numpy as np
import os


class VectorDB:
    def __init__(self, dim=384):
        self.dim = dim

        self.index_path = "data/faiss_index.bin"

        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
        else:
            self.index = faiss.IndexIDMap(
                faiss.IndexFlatL2(dim)
            )

    def add(self, vector, doc_id):
        vector = np.array([vector]).astype("float32")

        ids = np.array([doc_id], dtype=np.int64)

        self.index.add_with_ids(vector, ids)

    def search(self, query_vector, k=3):
        query_vector = np.array([query_vector]).astype("float32")

        distances, ids = self.index.search(query_vector, k)

        return ids[0]

    def save(self):
        faiss.write_index(self.index, self.index_path)