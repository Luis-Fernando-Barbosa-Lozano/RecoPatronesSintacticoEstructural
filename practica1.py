with open("C:\\Users\\iroba\\OneDrive\\Escritorio\\1000.txt", 'r') as archivo:
    contenido = archivo.read()

cadenas = contenido.split()
longitud = len(cadenas)
print(longitud)

print("Tenshi")