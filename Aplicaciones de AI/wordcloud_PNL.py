"""
Didier Irias Méndez
Aplicaciones de la Inteligencia Artifial
Entregable 3
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords

texto = """
 Este algortimo también es conocido como distancia de edición. La similaridad entre dos cadenas de texto A y B se 
basa en el conjunto mínimo de operaciones de edición necesarias para transformar A en B, o viceversa. Hay tres operaciones de edición, 
las cuales son destrucción, inserción y substitución. Entre más cerca de cero es la distancia de Levenshtein más parecidas son las hileras.
"""


nltk.download('stopwords')

stopwords = set(stopwords.words('spanish'))

palabras = texto.lower().split()
palabras = [palabra for palabra in palabras if palabra not in stopwords]
texto_procesado = " ".join(palabras)

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(texto_procesado)

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()