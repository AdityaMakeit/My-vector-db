from app.embedding import Embedding_model
from app.db import VectorDB
from app.storage import MetadataStorage

model = Embedding_model()

db = VectorDB()

storage = MetadataStorage()

texts = [
    "I love artificial intelligence",
    "Cricket is amazing",
    "Vector databases are powerful"
]

# store documents
for text in texts:
    vec = model.encode_text(text)

    doc_id = storage.add_document(text)

    db.add(vec, doc_id)

# save FAISS
db.save()

# search
query = "AI systems"

q_vec = model.encode_text(query)

ids = db.search(q_vec)

print("Query:", query)

for doc_id in ids:
    doc = storage.get_document(int(doc_id))
    print(doc)