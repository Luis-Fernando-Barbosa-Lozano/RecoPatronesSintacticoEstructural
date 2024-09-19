import re
import os

def ReconocimientoDeComentarios():
    # Abre el archivo y lee su contenido línea por línea
    with open("codigo_prueba.txt", 'r') as archivo:
        lineas = archivo.readlines()

    # Define las expresiones regulares para identificar comentarios cortos y bloques de comentarios largos (tanto con comillas dobles como simples)
    patron_corto = r"#.*"
    patron_largo = r"\"\"\"[\s\S]*?\"\"\""
    patrondos_largo = r"\'\'\'[\s\S]*?\'\'\'"

    # Abre el archivo de salida donde se guardarán los resultados
    with open("C:\\Users\\rico_\\OneDrive\\Escritorio\\tareas UnU\\RPSE\\RecoPatronesSintacticoEstructural\\comentarios.txt", 'w') as archivo_salida:
        dentro_comentario_largo = False
        dentro_comentario_largodos = False

        for linea in lineas:
            # Verifica si la línea contiene un comentario corto
            if re.match(patron_corto, linea):
                archivo_salida.write("Token Comentario Corto\n")
            # Verifica si estamos dentro o al final de un bloque de comentario largo (comillas dobles)
            elif re.match(patron_largo, linea) or dentro_comentario_largo:
                archivo_salida.write("Token Comentario Largo\n")
                if '"""' in linea:
                    dentro_comentario_largo = not dentro_comentario_largo
            # Verifica si estamos dentro o al final de un bloque de comentario largo (comillas simples)
            elif re.match(patrondos_largo, linea) or dentro_comentario_largodos:
                archivo_salida.write("Token Comentario Largo\n")
                if "'''" in linea:
                    dentro_comentario_largodos = not dentro_comentario_largodos
            else:
                # Escribe la línea sin modificaciones si no es un comentario
                archivo_salida.write(linea)

    print(f"El archivo ha sido procesado y guardado en 'comentarios.txt'.")

    # Ruta al archivo que quieres abrir
    archivo_path = "C:\\Users\\rico_\\OneDrive\\Escritorio\\tareas UnU\\RPSE\\RecoPatronesSintacticoEstructural\\comentarios.txt"

    # Abre el archivo en la aplicación predeterminada del sistema
    os.startfile(archivo_path)

# Llamada a la función
ReconocimientoDeComentarios()
