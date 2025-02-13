import os
import pymongo
import feedparser
from bs4 import BeautifulSoup
import requests

# Conexão com o MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client["news_db"]
collection = db["news_collection"]

# Lista de fontes RSS
rss_feeds = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://feeds.bbci.co.uk/news/rss.xml",
]

def fetch_rss_news():
    for url in rss_feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            news_item = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "source": url
            }
            collection.update_one({"link": entry.link}, {"$set": news_item}, upsert=True)

def fetch_web_scraping_news():
    url = "https://example.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")
    for article in articles:
        title = article.find("h2").text
        link = article.find("a")["href"]

        news_item = {
            "title": title,
            "link": link,
            "published": "Desconhecido",
            "source": "Scraped Website"
        }
        collection.update_one({"link": link}, {"$set": news_item}, upsert=True)

if __name__ == "__main__":
    fetch_rss_news()
    fetch_web_scraping_news()
    print("✅ Notícias capturadas e armazenadas!")
