import streamlit as st
from dotenv import load_dotenv
from Modulos.busqueda import buscar_informacion
from Modulos.rm import generar_resumen
from Modulos.wc import crear_wordcloud

load_dotenv()

st.set_page_config(page_title="Asistente de Investigación", layout="wide")
st.title("Asistente de Investigación Digital")

