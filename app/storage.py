import sqlite3


class MetadataStorage:
    def __init__(self, db_path="data/metadata.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
        """)

        self.conn.commit()

    def add_document(self, text):
        self.cursor.execute(
            "INSERT INTO documents (text) VALUES (?)",
            (text,)
        )

        self.conn.commit()

        return self.cursor.lastrowid

    def get_document(self, doc_id):
        self.cursor.execute(
            "SELECT text FROM documents WHERE id=?",
            (doc_id,)
        )

        result = self.cursor.fetchone()

        if result:
            return result[0]

        return None