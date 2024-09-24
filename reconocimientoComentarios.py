import re
import keyword
import os

# Compilar patrones al inicio
patrones = {
    "numero": re.compile(r'(?<!\w)\d+(\.\d+)?([eE][+-]?\d+)?(?!\w)'),
    "operador": re.compile(r'[+\-*/%<>=!]+'),
    "string": re.compile(r'\"[^\"]*\"|\'[^\']*\''),
    "comparacion": re.compile(r'==|!=|<=|>=|<|>'),
    "puntuacion": re.compile(r'[.,;(){}\[\]]'),
    "comentario_corto": re.compile(r'#.*'),
    "comentario_largo": re.compile(r'(\"\"\"|\'\'\')'),
}

# Leer archivo de entrada
try:
    with open("prueba_codigo.txt", "r") as archivo_entrada:
        lineas = archivo_entrada.readlines()
        contenido = "".join(lineas)
        num_caracteres = len(contenido)
except FileNotFoundError:
    print("Archivo no encontrado.")
    exit()

# Lista de palabras reservadas de Python
palabras_reservadas = keyword.kwlist

# Procesar el contenido del archivo
try:
    with open("resultado.txt", "w") as archivo_salida:
        archivo_salida.write(f"Numero de caracteres: {num_caracteres}\n\n")

        dentro_comentario = False
        for linea in lineas:
            if dentro_comentario:
                if patrones["comentario_largo"].search(linea):
                    dentro_comentario = False
                    archivo_salida.write("Token Comentario Largo\n")
                continue

            if patrones["comentario_corto"].search(linea):
                archivo_salida.write("Token Comentario Corto\n")
                continue
            elif patrones["comentario_largo"].search(linea):
                dentro_comentario = True
                continue

            # Procesar tokens en la línea
            nueva_linea = []
            palabras = linea.split()
            for palabra in palabras:
                if palabra in palabras_reservadas:
                    nueva_linea.append("PalabraReservada")
                elif patrones["comparacion"].match(palabra):
                    nueva_linea.append("TokenComparacion")
                elif patrones["operador"].match(palabra):
                    nueva_linea.append("TokenOperador")
                else:
                    for tipo, patron in patrones.items():
                        if tipo not in ["comentario_corto", "comentario_largo", "comparacion", "operador"]:
                            if patron.match(palabra):
                                nueva_linea.append(f'Token{tipo.capitalize()}')
                                break
                    else:
                        nueva_linea.append("TOKENID")

            archivo_salida.write(" ".join(nueva_linea) + "\n")

except IOError:
    print("Error escribiendo en el archivo de salida.")

# Abrir archivo procesado
archivo_path = os.path.abspath("resultado.txt")
try:
    if os.name == 'nt':  # Para Windows
        os.startfile(archivo_path)
    elif os.name == 'posix':  # Para macOS y Linux
        os.system(f'open "{archivo_path}"' if os.uname().sysname == 'Darwin' else f'xdg-open "{archivo_path}"')
except Exception as e:
    print(f"Error al intentar abrir el archivo: {e}")
