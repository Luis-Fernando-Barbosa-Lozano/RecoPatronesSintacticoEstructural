import re
import os


def ReconocimientoDeComentarios():
    # Abre el archivo y lee su contenido línea por línea
    with open("puropinshipython.txt", 'r') as archivo:
        lineas = archivo.readlines()

    # Define las expresiones regulares para identificar comentarios cortos y bloques de comentarios largos (tanto con comillas dobles como simples)
    patron_corto = r"#.*"
    patron_largo_inicio = r"\"\"\""
    patron_largo_final = r"\"\"\""
    patron_largo_dos_inicio = r"\'\'\'"
    patron_largo_dos_final = r"\'\'\'"

    # Abre el archivo de salida donde se guardarán los resultados
    with open(
            "C:\\Users\\rico_\\OneDrive\\Escritorio\\tareas UnU\\RPSE\\RecoPatronesSintacticoEstructural\\comentarios.txt",
            'w') as archivo_salida:
        #por si hay comentarios dentro de los comentarios
        dentro_comentario_largo = False
        dentro_comentario_largodos = False

        for linea in lineas:
            # Verifica si la línea contiene un comentario corto
            if re.match(patron_corto, linea) and not dentro_comentario_largo and not dentro_comentario_largodos:
                archivo_salida.write("Token Comentario Corto\n")

            # Manejo de comentarios largos con comillas dobles
            elif re.search(patron_largo_inicio, linea) and not dentro_comentario_largo:
                archivo_salida.write("Token Comentario Largo\n")
                dentro_comentario_largo = True
                if re.search(patron_largo_final, linea) and linea.count('"""') == 2:
                    dentro_comentario_largo = False  # Cierra el comentario si empieza y termina en la misma línea

                if re.search(patron_largo_final, linea):
                    dentro_comentario_largo = False  # Cierra el bloque si encuentra el final de comillas triples

            # Manejo de comentarios largos con comillas simples
            elif re.search(patron_largo_dos_inicio, linea) and not dentro_comentario_largodos:
                archivo_salida.write("Token Comentario Largo\n")
                dentro_comentario_largodos = True
                if re.search(patron_largo_dos_final, linea) and linea.count("'''") == 2:
                    dentro_comentario_largodos = False  # Cierra el comentario si empieza y termina en la misma línea

                if re.search(patron_largo_dos_final, linea):
                    dentro_comentario_largodos = False  # Cierra el bloque si encuentra el final de comillas simples

            # Escribe la línea sin modificaciones si no es un comentario
            else:
                archivo_salida.write(linea)

    print(f"El archivo ha sido procesado y guardado en 'comentarios.txt'.")

    # Ruta al archivo que quieres abrir
    archivo_path = "C:\\Users\\rico_\\OneDrive\\Escritorio\\tareas UnU\\RPSE\\RecoPatronesSintacticoEstructural\\comentarios.txt"

    # Abre el archivo en la aplicación predeterminada del sistema
    os.startfile(archivo_path)


# Llamada a la función
ReconocimientoDeComentarios()
