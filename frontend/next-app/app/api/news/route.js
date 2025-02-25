export default async function handler(req, res) {
  try {
    const response = await fetch("https://meu-bot-de-noticias.onrender.com/news");
    const news = await response.json();
    
    res.status(200).json(news);
  } catch (error) {
    console.error("Erro ao buscar notícias:", error);
    res.status(500).json({ error: "Erro ao buscar notícias" });
  }
}
