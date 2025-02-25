export async function GET(req) {
  try {
    console.log("🔍 Buscando notícias da API do Render...");

    const response = await fetch("https://mongo-automation-test.onrender.com/news", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0", // Evita bloqueios por bots
      },
    });

    if (!response.ok) {
      throw new Error(`Erro na API do Render: ${response.status} - ${response.statusText}`);
    }

    const news = await response.json();

    console.log("✅ Dados recebidos da API do Render:", news);
    return Response.json(news);
  } catch (error) {
    console.error("❌ Erro ao buscar notícias:", error);
    return Response.json({ 
      error: "Erro ao buscar notícias", 
      details: error.message 
    }, { status: 500 });
  }
}
