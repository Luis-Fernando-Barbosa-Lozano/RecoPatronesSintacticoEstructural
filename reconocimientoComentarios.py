import re
import os

# Abre el archivo y lee su contenido
with open("prueba_codigo.txt", 'r') as archivo:
    contenido = archivo.read()

    # Define la expresión regular para identificar comentarios largos
    patron_largo = r"\"\"\"[\s\S]*?\"\"\""  # Captura todo el contenido dentro de comillas triples

    # Encuentra y cuenta los comentarios largos
    comentarios_largos = re.findall(patron_largo, contenido)

    # Elimina los comentarios largos del contenido para evitar contar comentarios cortos dentro de ellos
    contenido_sin_largos = re.sub(patron_largo, "", contenido)

    # Define la expresión regular para identificar comentarios cortos que no estén dentro de bloques largos
    patron_corto = r"#.*(?!(\"\"\"))"  # Captura comentarios cortos que no están en comentarios largos

    # Encuentra y cuenta los comentarios cortos en el contenido sin comentarios largos
    comentarios_cortos = re.findall(patron_corto, contenido_sin_largos)

    # Guarda el conteo de comentarios en un archivo
    with open("C:\\Users\\iroba\\OneDrive\\Escritorio\\comentarios.txt", 'w') as archivo:
        archivo.write(f"comentarios cortos = {len(comentarios_cortos)}\n")
        archivo.write(f"comentarios largos = {len(comentarios_largos)}\n")

    print("El conteo de comentarios ha sido guardado en el archivo 'comentarios.txt'.")


# Ruta al archivo que quieres abrir
    archivo_path = "C:\\Users\\iroba\\OneDrive\\Escritorio\\comentarios.txt"

# Abre el archivo en la aplicación predeterminada del sistema
os.startfile(archivo_path)
