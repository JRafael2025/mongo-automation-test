from fastapi import FastAPI
import pymongo
import os

app = FastAPI()

# Conectar ao MongoDB
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client["news_db"]
collection = db["news_collection"]

@app.get("/")  # 👈 Adiciona a rota para evitar erro 404
def home():
    return {"message": "API de Notícias funcionando! Acesse /news para ver as notícias."}

@app.get("/news")
def get_news():
    news = list(collection.find({}, {"_id": 0}).sort("published", -1).limit(10))
    return {"news": news}
