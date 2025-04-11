from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io

def generar_nube_palabras(entradas):
    # Texto combinado
    corpus = " ".join([item["content"] for item in entradas])

    # Lista extendida de stopwords en español
    palabras_vacias = {
        "el", "la", "los", "las", "de", "del", "al", "en", "y", "o", "u", "es", "un", "una", "unos", "unas",
        "con", "por", "para", "se", "su", "sus", "a", "que", "como", "más", "menos", "ya", "no", "sí", "lo",
        "esto", "eso", "esa", "ese", "estos", "estas", "este", "cuando", "quien", "cual", "cuales", "también", "muy", "entre", "sobre", "todo", "nada",
        "hay", "haber", "fue", "fueron", "ser", "era", "han", "ha", "he", "tiene", "tener", "cada", "durante",
        "desde", "hasta"
    }

    # Crear la nube de palabras
    nube = WordCloud(
        width=800,
        height=400,
        background_color="white",
        stopwords=palabras_vacias
    ).generate(corpus)

    # Guardar imagen en objeto BytesIO
    buffer_img = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(nube, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(buffer_img, format="png")
    buffer_img.seek(0)

    return buffer_img
