from fastapi import FastAPI, HTTPException
import pymongo
import os

app = FastAPI()

# Verificar se MONGO_URI está definido
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("❌ ERRO: A variável de ambiente MONGO_URI não está definida!")

# Conectar ao MongoDB Atlas
try:
    client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client["news_db"]
    collection = db["news_collection"]
    client.server_info()  # Testa a conexão
except pymongo.errors.ServerSelectionTimeoutError:
    raise ValueError("❌ ERRO: Não foi possível conectar ao MongoDB Atlas!")

@app.get("/")
def home():
    return {"message": "API de Notícias funcionando! Acesse /news para ver as notícias."}

@app.get("/news")
def get_news():
    try:
        news = list(collection.find({}, {"_id": 0}).sort("published", -1).limit(10))
        return {"news": news}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
