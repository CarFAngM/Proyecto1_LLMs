from langchain_community.tools.tavily_search import TavilySearchResults
import os

def obtener_resultados_busqueda(consulta):
    
    clave_api = os.getenv("TAVILY_API_KEY")
    
    
    buscador = TavilySearchResults(tavily_api_key=clave_api, max_results=10)
    
    
    resultados = buscador.invoke({"query": consulta})
    
   
    lista_resultados = []
    for item in resultados:
        info = {
            "titulo": item.get("title"),
            "descripcion": item.get("content"),
            "enlace": item.get("url")
        }
        lista_resultados.append(info)

    return lista_resultados
