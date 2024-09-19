import keyword
import re

# Leer palabras reservadas y constantes desde archivo
with open("palabras.txt", 'r') as archivo:
    palabras = archivo.read().split(',')

# Obtener palabras reservadas de Python
palabras_reservadas = keyword.kwlist

# Crear patrones de sustitución
def crear_patron_sustitucion():
    patrones = {
        'TokenNumero': re.compile(r'(?<!\w)\d+(?!\w)'),
        'TokenOperador': re.compile(r'[+\-*/%<>=!]+'),
        'TokenString': re.compile(r'\".*?\"|\'[^\']*\''),
        'TokenComparacion': re.compile(r'==|!=|<=|>=|<|>'),
        'TokenPuntuacion': re.compile(r'[.,;]'),
        'TokenConstante': re.compile(r'\bNone\b|\bTrue\b|\bFalse\b')
    }
    return patrones

# Función para reemplazar palabras reservadas
def reemplazar_palabras_reservadas(codigo, palabras_reservadas):
    for palabra in palabras_reservadas:
        codigo = re.sub(r'\b{}\b'.format(palabra), 'TokenPalabraReservada', codigo)
    return codigo

# Función para procesar identificadores, excluyendo aquellos que empiezan por 'token'
def reemplazar_identificadores(codigo):
    # Usamos la expresión regular corregida
    return re.sub(r'\b(?!token\b)[_a-zA-Z][_a-zA-Z0-9]*\b', 'TokenID', codigo)


# Función para procesar el archivo y reemplazar los elementos por nombres de tokens
def analizar_codigo(archivo_entrada, archivo_salida):
    # Leer el archivo de entrada
    with open(archivo_entrada, 'r') as archivo:
        codigo = archivo.read()

    # Aplicar los patrones de sustitución
    patrones = crear_patron_sustitucion()

    for token_nombre, patron in patrones.items():
        codigo = patron.sub(token_nombre, codigo)

    # Reemplazar palabras reservadas por su nombre de token
    codigo = reemplazar_palabras_reservadas(codigo, palabras_reservadas)

    # Reemplazar identificadores por su nombre de token (solo después de las palabras reservadas)
    codigo = reemplazar_identificadores(codigo)

    # Reemplazar constantes por su nombre de token
    for constante in palabras:
        codigo = re.sub(r'\b{}\b'.format(constante.strip()), 'TokenConstante', codigo)

    # Guardar el resultado en el archivo de salida
    with open(archivo_salida, 'w') as archivo:
        archivo.write(codigo)

# Archivo de entrada con el código
archivo_entrada = "codigo_texto.txt"

# Archivo de salida donde se guardarán los tokens categorizados
archivo_salida = "tokens_reemplazados.txt"

# Llamada a la función para analizar el código
analizar_codigo(archivo_entrada, archivo_salida)

