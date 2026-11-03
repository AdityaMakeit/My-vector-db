from sentence_transformers import SentenceTransformer

class Embedding_model:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def encode_text(self, text: str):
        return self.model.encode(text)
    
    def encode_texts(self, texts: list):
        return self.model.encode(texts)
    

    

