import os
import re

# Abre el archivo y lee su contenido
with open("prueba_codigo.txt", 'r') as archivo:
    contenido = archivo.read()

with open("C:\\Users\\iroba\\OneDrive\\Escritorio\\1000.txt", 'r') as archivo:
    res = archivo.read()

# Define una expresión regular para identificar nombres de variables (asumiendo que siguen las convenciones de Python)
patron = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'

# Encuentra todas las coincidencias que sigan el patrón
cadenas = re.findall(patron, contenido)

# Filtra las coincidencias para eliminar palabras clave de Python u otras no deseadas (opcional)
palabras_clave = res.split(",")
variables = [cadena for cadena in cadenas if cadena not in palabras_clave]

# Muestra la longitud y las variables encontradas
print(f"Cantidad de variables: {len(variables)}")

# Abre un nuevo archivo en modo escritura para guardar las variables
with open("C:\\Users\\iroba\\OneDrive\\Escritorio\\variables.txt", 'w') as archivo_salida:
    for variable in variables:
        archivo_salida.write(variable + '\n')

print(f"Se han guardado {len(variables)} variables en el archivo 'variables.txt'.")

# Ruta al archivo que quieres abrir
archivo_path = "C:\\Users\\iroba\\OneDrive\\Escritorio\\variables.txt"

# Abre el archivo en la aplicación predeterminada del sistema
os.startfile(archivo_path)
