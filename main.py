import streamlit as st
from dotenv import load_dotenv 

from Modulos.bq import generar_informacion
from Modulos.rm import hacer_resumen
from Modulos.wc import hacer_wordcloud

load_dotenv()

st.set_page_config(page_title="Asistente", layout="wide")
st.title("Asistente de Investigación")


tema = st.text_input("Ingresa un tema para investigar:")
if tema:
    with st.spinner("Buscando información..."):
        resultados = generar_informacion(tema)

    if resultados:
        st.subheader("Resultados encontrados")

        for i, resultado in enumerate(resultados[:5]):
            if isinstance(resultado, dict) and "title" in resultado:
                with st.expander(resultado["title"]):
                    contenido = resultado.get("content", "Sin contenido disponible.")
                    url = resultado.get("url", "#")
                    st.markdown(f"Contenido: {contenido[:500]}...")
                    st.markdown(f"Enlace al artículo original {url} ")
            else:
                st.warning(f"Resultado {i+1} no tiene título.")


        st.subheader("Resumen")
        resumen = hacer_resumen(resultados)
        st.success(resumen)


        st.subheader("Nube")
        imagen_wordcloud = hacer_wordcloud(resultados)
        st.image(imagen_wordcloud, use_container_width=True)

    else:
        st.warning("No se encontraron resultados para este tema.")
