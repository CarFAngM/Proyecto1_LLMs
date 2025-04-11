from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

def crear_resumen_ejecutivo(entradas):
    texto_fuente = "\n".join([entrada["content"][:1000] for entrada in entradas])
    

    plantilla_prompt = ChatPromptTemplate.from_template(
        "Elabora un resumen ejecutivo en español de no más de 200 palabras "
        "basado en el siguiente contenido:\n\n{informacion}\n\nResumen:"
    )

    # Inicialización del modelo de lenguaje
    modelo_llm = ChatOpenAI(
        temperature=0.2,
        model="gpt-3.5-turbp",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    resumen_generador = plantilla_prompt | modelo_llm

    respuesta = resumen_generador.invoke({"informacion": texto_fuente})

    return respuesta.content
