import gensim

# Ruta del archivo de FastText en español
FASTTEXT_PATH = "cc.es.300.vec"

# Cargar el modelo de FastText
print("Cargando modelo de FastText...")
model = gensim.models.KeyedVectors.load_word2vec_format(FASTTEXT_PATH, binary=False)

# Leer el archivo PHP de "El Alquimista" y extraer solo el texto
def extract_text_from_php(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    words = [word.lower() for word in text.split() if word.isalpha()]
    return words

# Ruta del archivo PHP de "El Alquimista"
ALQUIMISTA_PATH = "view.php"

# Extraer palabras del archivo
words = extract_text_from_php(ALQUIMISTA_PATH)

# Obtener embeddings de cada palabra presente en el modelo
OUTPUT_FILE = "embeddingsAlquimista.txt"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for word in words:
        if word in model:  
            embedding = ", ".join(map(str, model[word])) 
            f.write(f'"{word}": [{embedding}]\n')

print(f"Embeddings guardados en {OUTPUT_FILE}")