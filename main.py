import streamlit as st
from dotenv import load_dotenv

from Modulos.busqueda import buscar_informacion
from Modulos.rm import generar_resumen
from Modulos.wc import crear_wordcloud

# Cargar variables de entorno (como API Keys)
load_dotenv()

# Configuración inicial de la app
st.set_page_config(page_title="Asistente de Investigación", layout="wide")
st.title("Asistente de Investigación Digital")

# Entrada del usuario
tema = st.text_input("Ingresa un tema de investigación:")

# Si se ingresó un tema, iniciar flujo
if tema:
    with st.spinner("Buscando información en fuentes confiables..."):
        resultados = buscar_informacion(tema)

    if resultados:
        st.subheader("Resultados encontrados")
        for resultado in resultados[:3]:
            with st.expander(resultado["title"]):
                st.markdown(f"**Contenido:** {resultado['content'][:500]}...")
                st.markdown(f"[Enlace al artículo original]({resultado['url']})")

        # Mostrar resumen ejecutivo
        st.subheader("Resumen ejecutivo")
        resumen = generar_resumen(resultados)
        st.success(resumen)

        # Mostrar nube de palabras
        st.subheader("☁️ Nube de palabras clave")
        imagen_wordcloud = crear_wordcloud(resultados)
        st.image(imagen_wordcloud, use_container_width=True)

    else:
        st.warning("No se encontraron resultados para este tema. Intenta con otro término.")
