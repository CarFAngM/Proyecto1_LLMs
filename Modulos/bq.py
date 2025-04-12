from langchain_community.tools.tavily_search import TavilySearchResults
import os


def generar_informacion(topic):
    TAVILY_KEY = os.getenv("TAVILY_API_KEY")

    search = TavilySearchResults(tavily_api_key=TAVILY_KEY, max_results=10)

    resultados = search.invoke({"query": topic})

    return [{
        "title": res["title"],
        "content": res["content"],
        "url": res["url"]
    } for res in resultados]