import { MongoClient } from "mongodb";

export default async function handler(req, res) {
  if (req.method !== "GET") {
    return res.status(405).json({ message: "Método não permitido" });
  }

  try {
    const client = new MongoClient(process.env.MONGO_URI);
    await client.connect();
    const db = client.db("news_db");
    const collection = db.collection("news_collection");

    const news = await collection.find().sort({ published: -1 }).limit(10).toArray();
    await client.close();

    res.status(200).json(news);
  } catch (error) {
    console.error("❌ ERRO AO BUSCAR NOTÍCIAS:", error);
    res.status(500).json({ message: "Erro ao buscar notícias", error });
  }
}
