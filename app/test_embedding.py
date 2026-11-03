from app.embedding import Embedding_model
from app.db import VectorDB

model = Embedding_model()
db = VectorDB()

texts = [
    "I love you",
    "I like you",
    "I play cricket",
    "Artificial intelligence is amazing"
]

# add data
for t in texts:
    vec = model.encode_text(t)
    db.add(vec, t)

# search
query = "I admire you"
q_vec = model.encode_text(query)

results = db.search(q_vec, k=2)

print("Query:", query)
print("Results:", results)