from Peliculas import *
import os
ListaPeliculas = []


def elegirArchivo():
    # Leemos la ruta/nombre del archivo a leer por consola
    archivo = str(input("Introduzca el nombre/ruta del archivo a leer: "))
    while not os.path.isfile(archivo):  # Comprobamos que el archivo existe
        print("\nERROR: No se encontró el archivo\n")
        # Volvemos a leer la ruta/nombre del archivo
        archivo = str(input("Introduzca el nombre/ruta del archivo a leer: "))
    else:
        return archivo  # Si el archivo existe, devuelve la ruta/nombre


def cargarArchivo(lista):
    nombres = []
    archivo = elegirArchivo()
    if archivo != None:
        fichero = open(archivo, 'r')
    for linea in fichero:
        separador = linea.split(";")
        tmp_nombre = None
        tmp_actores = None
        tmp_anio = None
        tmp_genero = None
        for i in range(len(separador)):
            if i == 0:
                tmp_nombre = separador[i].strip()
            elif i == 1:
                tmp_actores = separador[i].strip()
            elif i == 2:
                tmp_anio = separador[i].strip()
            elif i == 3:
                tmp_genero = separador[i].strip()

        if tmp_nombre not in nombres:
            peli = peliculas(tmp_nombre, tmp_actores, tmp_anio, tmp_genero)
            lista.append(peli)
            nombres.append(tmp_nombre)


def mostrarNombres(registro_peliculas):
    num_pelis = 0
    for pelicula in registro_peliculas:
        num_pelis += 1
        print(num_pelis, ".", pelicula.nombre)
    opcion_peli = int(
        input('Ingrese el numero de la pelicula donde desea ver los actores: ')) - 1

    actor = registro_peliculas[opcion_peli].actores
    print("Actores de {0}: {1}".format(
        registro_peliculas[opcion_peli].nombre, actor))


def gestionarPeliculas():
    print("""===========GESTION PELICULAS========
        a. Mostrar Peliculas 
        b. Mostrar actores
        c. Regresar al menu principal
        ======================================""")
    while True:
        try:
            option = input("Ingrese una opcion: ")
            if option == "a":
                for i in ListaPeliculas:
                    i.mostrar_infopeli()
                gestionarPeliculas()
                break
            elif option == "b":
                mostrarNombres(ListaPeliculas)
                gestionarPeliculas()
                break
            elif option == "c":
                menuPrincipal()
                break
            else:
                print("Opcion incorrecta")
        except ValueError:
            print("Opcion incorrecta")
    exit


def buscar_actor(lista_peliculas, actor):
    peliculas_con_actor = []
    for pelicula in lista_peliculas:
        if actor.upper() in pelicula.actores.upper():
            peliculas_con_actor.append(pelicula.nombre)
    if len(peliculas_con_actor) == 0:
        print("El actor", actor, "no se encuentra en ninguna pelicula.")
    else:
        print("El actor", actor, "aparece en las siguientes peliculas:")
        for pelicula in peliculas_con_actor:
            print("-", pelicula)


def buscar_anio(lista_peliculas, anio):
    filtrado_anio = []
    for pelicula in lista_peliculas:
        if pelicula.anio == anio:
            filtrado_anio.append([pelicula.nombre, pelicula.genero])
    if filtrado_anio == []:
        print('No existen peliculas')
    else:
        print('Las peliculas del', anio, 'son: ')
        for pelicula in filtrado_anio:
            print("-", pelicula)


def filtrado():
    print("""===========FILTRADO========
        a. Filtrado por actor
        b. Filtrado por año
        c. Filtrado por genero
========================================""")
    while True:
        try:
            option = input("Ingrese una opcion: ")
            if option == "a":
                nomActor = input('Ingrese el nombre del actor: ')
                buscar_actor(ListaPeliculas, nomActor)
                filtrado()
                break
            elif option == "b":
                opcAnio = input("Ingrese el año para ver las peliculas: ")
                buscar_anio(ListaPeliculas, opcAnio)
                filtrado()
                break
            elif option == "c":

                break
            else:
                print("Opcion incorrecta")
        except ValueError:
            print("Opcion incorrecta")
    exit


def menuPrincipal():
    print("""===========MENU PRINCIPAL=============
        1.- Cargar Archivo de entrada
        2.- Gestionar peliculas
        3.- Filtrado
        4.- Grafica
        0.- Salir
        =========================================""")
    while True:
        try:
            option = int(input("Ingrese una opcion: "))
            if option == 1:
                print('========Carga de Archivo========')
                cargarArchivo(ListaPeliculas)
                print("CARGO EXITOSAMENTE\n")
                input('Presione enter para continuar...')
                menuPrincipal()
                break
            elif option == 2:
                gestionarPeliculas()
                break
            elif option == 3:
                filtrado()
                break
            elif option == 4:
                print('op4')
                break
            elif option == 0:
                break
            else:
                print("Opcion incorrecta")
                menuPrincipal()
        except ValueError:
            print("Opcion incorrecta")
    exit


print("""============= LENGUAJES FORMALES DE PROGRAMACION B- =================
                        201212891
                    Edgar Rolando Ramirez Lopez
    ======================================================================""")
input('      Presione cualquier tecla para continuar...       ')
menuPrincipal()
