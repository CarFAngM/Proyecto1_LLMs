from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os


def hacer_resumen(resultados):
    content = "\n".join([res["content"][:1000] for res in resultados])

    prompt_template = ChatPromptTemplate.from_template(
        "Genera un resumen en español de 200 palabras"
        "basado en esta información:\n\n{texto}\n\nResumen:"
    )

    llm = ChatOpenAI(
        temperature=0.5,
        model="gpt-4o-mini",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    chain = prompt_template | llm
    return chain.invoke({"texto": content}).content