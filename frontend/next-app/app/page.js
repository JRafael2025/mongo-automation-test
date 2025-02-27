"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    fetch("/api/news")
      .then(res => res.json())
      .then(data => setNews(data))
      .catch(() => setNews([]));
  }, []);

  return (
    <div>
      <h1>📰 Últimas Notícias</h1>
      <ul>
        {news.length > 0 ? (
          news.map((item, index) => (
            <li key={index}>
              <a href={item.link} target="_blank" rel="noopener noreferrer">
                {item.title}
              </a>
            </li>
          ))
        ) : (
          <p>⚠️ Nenhuma notícia encontrada.</p>
        )}
      </ul>
    </div>
  );
}
