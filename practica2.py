import random
import os

def crear():
    nombre_archivo = input("Ingresa el nombre del archivo>>> ")
    cantidad_valores = int(input("Ingresa la cantidad de valores aleatorios a generar>>> "))
    with open(nombre_archivo, 'w') as archivo:
        for _ in range(cantidad_valores):
            valor_aleatorio = random.randint(0, 10000)
            archivo.write(f"{valor_aleatorio}\n")

    ruta_completa = os.path.join(os.getcwd(), nombre_archivo)
    print(f"Archivo '{nombre_archivo}' creado en {ruta_completa}")

    abrir = input("Desea ver el contenido del archivo? (1=Si, 2=No)>>> ")
    if abrir == "1":
        leer(ruta_completa)


def leer(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
    print(f"Contenido del archivo '{ruta_archivo}'>>>")
    print(contenido)


def main():
    elije = input("Elija qué desea hacer: 1 para crear un archivo | 2 para mostrar el contenido de un archivo>>> ")
    if elije == "1":
        crear()
    elif elije == "2":
        nombre = input("Ingresa el nombre del archivo que deseas recuperar>>> ")
        ruta_completa = os.path.join(os.getcwd(), nombre)
        leer(ruta_completa)
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")


if _name_ == "_main_":
    main()