with open("prueba_codigo.txt", 'r') as archivo:
    contenido = archivo.read()

cadenas = contenido.split()
longitud = len(cadenas)
print(longitud)