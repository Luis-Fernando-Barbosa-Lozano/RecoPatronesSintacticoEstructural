import re
import keyword
import os

# Compilar patrones al inicio
patrones = {
    "numero": re.compile(r'(?<!\w)\d+(?!\w)'),
    "operador": re.compile(r'[+\-*/%<>=!]+'),
    "string": re.compile(r'\"[^\"]*\"|\'[^\']*\''),
    "comparacion": re.compile(r'==|!=|<=|>=|<|>'),
    "puntuacion": re.compile(r'[.,;(){}\[\]]'),  # Agregado [] como puntuación
    "comentario_corto": re.compile(r'#.*'),
    "comentario_largo": re.compile(r'(\"\"\"|\'\'\')'),
}

# Leer el archivo de entrada
with open("puropinshipython.txt", "r") as archivo_entrada:
    lineas = archivo_entrada.readlines()
    contenido = "".join(lineas)
    num_caracteres = len(contenido)

# Lista de palabras reservadas de Python
palabras_reservadas = keyword.kwlist

# Procesar línea por línea y hacer los reemplazos
with open("resultado.txt", "w") as archivo_salida:
    # Escribir el número de caracteres en el encabezado
    archivo_salida.write(f"Numero de caracteres: {num_caracteres}\n\n")

    # Verificar si todo el contenido es un comentario largo
    if patrones["comentario_largo"].match(contenido.strip()):
        archivo_salida.write("Token Comentario Largo\n")
    else:
        dentro_comentario = False

        for linea in lineas:
            # Verificar si hay comentarios
            if dentro_comentario:
                if patrones["comentario_largo"].search(linea):
                    dentro_comentario = False
                    archivo_salida.write("Token Comentario Largo\n")
                continue

            # Manejo de comentarios cortos y largos
            if patrones["comentario_corto"].search(linea):
                archivo_salida.write("Token Comentario Corto\n")
                continue
            elif patrones["comentario_largo"].search(linea):
                dentro_comentario = True
                continue

            # Manejo de tokens
            palabras = linea.split()
            nueva_linea = []
            for palabra in palabras:
                if palabra in palabras_reservadas:
                    nueva_linea.append("PalabrasReservadas")
                else:
                    # Verificar primero si es un comparador
                    if patrones["comparacion"].match(palabra):
                        nueva_linea.append('TokenComparacion')
                    elif patrones["operador"].match(palabra):
                        nueva_linea.append('TokenOperador')
                    else:
                        for tipo, patron in patrones.items():
                            if tipo not in ["comentario_corto", "comentario_largo", "comparacion", "operador"]:
                                if patron.match(palabra):
                                    nueva_linea.append(f'Token{tipo.capitalize()}')
                                    break
                        else:
                            nueva_linea.append('TOKENID')

            archivo_salida.write(" ".join(nueva_linea) + "\n")

# Abrir archivo procesado
archivo_path = os.path.abspath("resultado.txt")

try:
    os.startfile(archivo_path)  # Solo en Windows
except AttributeError:
    os.system(f'open "{archivo_path}"')  # macOS
    # Para Linux, podrías usar:
    # os.system(f'xdg-open "{archivo_path}"')
