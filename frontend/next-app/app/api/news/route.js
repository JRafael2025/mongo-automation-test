import { MongoClient } from "mongodb";
import { NextResponse } from "next/server";

export async function GET() {
  try {
    const client = new MongoClient(process.env.MONGO_URI);
    await client.connect();
    const db = client.db("news_db");
    const collection = db.collection("news_collection");

    const news = await collection.find().sort({ published: -1 }).limit(10).toArray();
    await client.close();

    return NextResponse.json(news);
  } catch (error) {
    console.error("❌ ERRO AO BUSCAR NOTÍCIAS:", error);
    return NextResponse.json({ message: "Erro ao buscar notícias", error }, { status: 500 });
  }
}
