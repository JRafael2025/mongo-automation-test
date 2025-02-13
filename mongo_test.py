import os
import pymongo

# Pega a string de conexão do GitHub Secrets
MONGO_URI = os.getenv("MONGO_URI")

def test_mongo_connection():
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client["test_db"]
        collection = db["test_collection"]

        # Inserir um documento de teste
        test_data = {"name": "GitHub Actions", "status": "Success"}
        result = collection.insert_one(test_data)

        # Buscar o documento inserido
        inserted_doc = collection.find_one({"_id": result.inserted_id})

        print("✅ Conexão bem-sucedida! Documento inserido:", inserted_doc)

    except Exception as e:
        print("❌ Erro na conexão com o MongoDB:", e)

if __name__ == "__main__":
    test_mongo_connection()
