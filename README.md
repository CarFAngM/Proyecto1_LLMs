Descripción del proyecto:

El presente proyecto consiste en una aplicación web interactiva que tiene la capacidad de ejecutar acciones de un asistente de investigación digital.Esta herramienta tiene la capacidad de buscar información en la web y llevar a cabo un análisis de lo encontrado mediante Tavily y además presentará una nube de palabras relevantes relacionadas a la búsqueda del usuario.

Instrucciones para ejecutar la aplicación:
A nivel general, para la ejecución de esta aplicación es necesario crear un entorno virtual 
(1), instalar las dependencias con pip install 
(2), agregar las API keys 
(3) y finalmente llevar a cabo la ejecución del programa(4) donde tras ingresar el código se abrirá automáticamente una pestaña en el buscador de preferencia con la aplicación.


Descripción de los módulos:

Modulos/wc

Este módulo está diseñado para generar una visualización en forma de word cloud (nube de palabras) a partir de una lista de resultados textuales. Su objetivo es representar gráficamente la frecuencia de aparición de las palabras más relevantes dentro de un conjunto de textos, excluyendo palabras comunes o poco informativas (stopwords) en inglés y español.

Modulos/rm

Este módulo se encarga de generar un resumen conciso y en español de aproximadamente 200 palabras a partir de un conjunto de textos. Está diseñado para facilitar la comprensión rápida de grandes volúmenes de información textual mediante el uso de modelos de lenguaje avanzados.

Modulos/bq

Este módulo permite realizar búsquedas automáticas en la web a partir de un tema dado y devuelve los resultados más relevantes de forma estructurada. Utiliza la herramienta TavilySearchResults, integrada con LangChain, para acceder a fuentes confiables en tiempo real.

main.py

Es la interfaz gráfica del proyecto (construida con Streamlit).


Reflexión sobre el uso de IA para buscar y procesar información:

La aparición de inteligencias artificiales abiertas al público, ha sido un hito en la historia de la humanidad, ya que representa un antes y un después en cómo somos capaces de acceder a la información. El uso de una inteligencia artificial para buscar y seleccionar información para que nosotros como usuarios la podamos observar y analizar, es algo sumamente positivo y enriquecedor para cualquier tipo de actividad, tanto doméstica como a nivel de trabajo. Por lo que por ese lado, todo parece perfecto.
Sin embargo, a la hora de hablar del uso de una inteligencia artificial para procesar información, ya nos topamos con distintas posiciones respecto a la ética para el uso de IA en este ámbito. Ya que tiene muchas capas el analizar esto, desde estudiar bajo qué criterios la IA va a clasificar información como ética o no ética de analizar hasta las fuentes de las cuales extrae la información, debido a que al tratarse de una inteligencia artificial y una persona, el sesgo que puede presentar no es del todo evidente.
En base a lo planteado, la aparición de la IA es una herramienta que puede acelerar exponencialmente la eficiencia de trabajo en cualquier ámbito, sin embargo, puede que en el futuro existan regulaciones éticas para su uso.
