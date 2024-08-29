import re
import os

# Abre el archivo y lee su contenido
with open("C:\\Users\\iroba\\OneDrive\\Escritorio\\1000.txt", 'r') as archivo:
    contenido = archivo.read()

    # Define una expresión regular para identificar comentarios en Python
    patron = r"#.*"

    # Encuentra todas las coincidencias que sigan el patrón
    comentarios = re.findall(patron, contenido)

    # Diferencia entre comentarios cortos y largos
    comentarios_cortos = [comentario for comentario in comentarios if len(comentario) < 40]
    comentarios_largos = [comentario for comentario in comentarios if len(comentario) >= 40]

    # Guarda los comentarios cortos y largos en un solo archivo
    with open("C:\\Users\\iroba\\OneDrive\\Escritorio\\comentarios.txt", 'w') as archivo:
        archivo.write("Comentarios Cortos:\n")
        for comentario in comentarios_cortos:
            archivo.write(comentario + '\n')

        archivo.write("\nComentarios Largos:\n")
        for comentario in comentarios_largos:
            archivo.write(comentario + '\n')

    print(
        f"Se han guardado {len(comentarios_cortos)} comentarios cortos y {len(comentarios_largos)} comentarios largos en el archivo 'comentarios.txt'.")

    # Ruta al archivo que quieres abrir
    archivo_path = "C:\\Users\\iroba\\OneDrive\\Escritorio\\comentarios.txt"

    # Abre el archivo en la aplicación predeterminada del sistema
    os.startfile(archivo_path)
