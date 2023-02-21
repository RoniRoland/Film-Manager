from Peliculas import *
import os
ListaPeliculas = []

# Funcion que verifica si el archivo existe o no, se utilizo la libreria OS


def elegirArchivo():
    # Leemos la ruta/nombre del archivo a leer por consola
    archivo = str(input("Escribe el nombre o ruta del archivo para cargar: "))
    while not os.path.isfile(archivo):  # Comprobamos que el archivo existe
        print("\nERROR: No se encontró el archivo\n")
        # Volvemos a leer la ruta/nombre del archivo
        archivo = str(
            input("Escribe el nombre o ruta del archivo para cargar: "))
    else:
        return archivo  # Si el archivo existe, devuelve la ruta/nombre

# Funcion que carga el archivo a la ListaPeliculas


def cargarArchivo(lista):
    nombres = []
    archivo = elegirArchivo()
    # Se verifica si el archivo no esta vacio para que se prosiga con la lectura
    if archivo != None:
        fichero = open(archivo, 'r')
    # en este for itera todo el archivo separando cada linea con el limitador ';' y con eso crea una lista de elementos de nuestra clase peliculas
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
        input('\nIngrese el numero de la pelicula donde desea ver los actores: ')) - 1

    actor = registro_peliculas[opcion_peli].actores
    print("\nActores de {0}: {1}".format(
        registro_peliculas[opcion_peli].nombre, actor))


def gestionarPeliculas():
    print("""\n===========GESTION PELICULAS====================\n
        a. Mostrar Peliculas 
        b. Mostrar actores
        c. Regresar al menu principal
\n================================================\n""")
    while True:
        try:
            option = input("Ingrese una opcion: ")
            print('\n')
            if option == "a":
                if ListaPeliculas == []:
                    print(
                        '\n****No tiene ninguna pelicula registrada. Cargue un archivo para mostrar el listado de peliculas.****')
                else:
                    print('===============LISTADO PELICULAS================\n')
                    for i in ListaPeliculas:
                        i.mostrar_infopeli()
                gestionarPeliculas()
                break
            elif option == "b":
                if ListaPeliculas == []:
                    print(
                        '\n****No tiene ninguna pelicula registrada. Cargue un archivo para mostrar el listado de actores.****')
                else:
                    print('================MOSTRAR ACTORES=================\n')
                    mostrarNombres(ListaPeliculas)
                gestionarPeliculas()
                break
            elif option == 'c':
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
        print("\nEl actor", actor, "no se encuentra en ninguna pelicula. \n")
    else:
        print("\nEl actor", actor, "aparece en las siguientes peliculas: \n")
        for pelicula in peliculas_con_actor:
            print("-", pelicula)


def buscar_anio(lista_peliculas, anio):
    filtrado_anio = []
    for pelicula in lista_peliculas:
        if pelicula.anio == anio:
            filtrado_anio.append([pelicula.nombre, pelicula.genero])
    if filtrado_anio == []:
        print('\nNo hay peliculas en ese año.\n')
    else:
        print('\nLas peliculas del', anio, 'son: \n')
        for pelicula in filtrado_anio:
            print("-", pelicula)


def buscar_genero(lista_peliculas, genero):
    peliculas_con_genero = []
    for pelicula in lista_peliculas:
        if genero.upper() in pelicula.genero.upper():
            peliculas_con_genero.append(pelicula.nombre)
    if len(peliculas_con_genero) == 0:
        print("\nEl genero", genero, "no se encuentra en ninguna pelicula.\n")
    else:
        print("\nEl genero", genero, "aparece en las siguientes peliculas:\n")
        for pelicula in peliculas_con_genero:
            print("-", pelicula)


def filtrado():
    print("""\n===================FILTRADO=====================\n
        a. Filtrado por actor
        b. Filtrado por año
        c. Filtrado por genero
        d. Regresar al menu principal
\n================================================""")
    while True:
        try:
            option = input("\nIngrese una opcion: ")
            if option == "a":
                if ListaPeliculas == []:
                    print(
                        '\n****No tiene ninguna pelicula registrada. Cargue un archivo para filtrar por actor.****')
                else:
                    print('\n===============FILTRAR POR ACTOR================\n')
                    nomActor = input('Ingrese el nombre del actor: ')
                    buscar_actor(ListaPeliculas, nomActor)
                filtrado()
                break
            elif option == "b":
                if ListaPeliculas == []:
                    print(
                        '\n****No tiene ninguna pelicula registrada. Cargue un archivo para filtrar por año.****')
                else:
                    print('\n================FILTRAR POR AÑO=================\n')
                    opcAnio = input("Ingrese el año para ver las peliculas: ")
                    buscar_anio(ListaPeliculas, opcAnio)
                filtrado()
                break
            elif option == "c":
                if ListaPeliculas == []:
                    print(
                        '\n****No tiene ninguna pelicula registrada. Cargue un archivo para filtrar por genero.****')
                else:
                    print('\n===============FILTRAR POR GENERO===============\n')
                    opcGenero = input("Ingrese el genero de la pelicula: ")
                    buscar_genero(ListaPeliculas, opcGenero)
                filtrado()
                break
            elif option == 'd':
                menuPrincipal()
                break
            else:
                print("Opcion incorrecta")
        except ValueError:
            print("Opcion incorrecta")
    exit

# Funcion que me guarda en una lista los actores de todas las peliculas sin repetir


def mostrar_actores(list_peliculas):
    actores = []
    for pelicula in list_peliculas:
        for actor in pelicula.actores.split(","):
            if actor.strip() not in actores:
                actores.append(actor.strip())
    return actores

# Funcion para mostrar grafica


def grafica_peliculas(lista_peliculas):
    # Aqui se guardan todos los actores
    acts = mostrar_actores(lista_peliculas)
    archivoDOT = open("imagen.dot", "w")
    archivoDOT.write("digraph { \n")
    archivoDOT.write('rankdir = LR \n')
    archivoDOT.write(
        'node[shape=record, fontname="Arial Black", fontsize=16] \n')
    # recorre la lista para generar el nodo donde se guardara el nombre de la pelicula, año y genero
    for pelicula in lista_peliculas:
        archivoDOT.write(pelicula.nombre.replace(" ", "") +
                         '[color=green, style=filled, label=<\n')
        archivoDOT.write('<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">\n')
        archivoDOT.write('<TR><TD BGCOLOR="red" COLSPAN="2">' +
                         pelicula.nombre + '</TD></TR>\n')
        archivoDOT.write('<TR><TD BGCOLOR="blue">' +
                         pelicula.anio + '</TD> + <TD BGCOLOR="yellow">' +
                         pelicula.genero + '</TD> </TR>\n')
        archivoDOT.write('</TABLE>\n')
        archivoDOT.write('>]')
        '''archivoDOT.write(pelicula.nombre.replace(" ", "")+'[color=green, style=filled, label="' +
                         pelicula.nombre + '|' + '{' + pelicula.anio + '|' + pelicula.genero + '}' + '"]\n')'''
        # recorre los actores y se separa con ',' ya que en una pelicula puede haber mas de 1 actor, y se enlaza con el nodo anterior
        for actor in pelicula.actores.split(","):
            archivoDOT.write(pelicula.nombre.replace(
                " ", "")+'->' + actor.strip().replace(
                " ", "") + "\n")

    # Se crean los nodos de actores
    for a in acts:
        archivoDOT.write(a.replace(" ", "")+'[color=yellow, style=filled, label="' +
                         a + '"]\n')

    archivoDOT.write("} \n")
    archivoDOT.close()

    os.system("dot.exe -Tpng imagen.dot -o  ReporteGrafico.png")
    os.startfile("ReporteGrafico.png")


def menuPrincipal():
    print("""\n================MENU PRINCIPAL===================\n
        1.- Cargar Archivo de entrada
        2.- Gestionar peliculas
        3.- Filtrado
        4.- Grafica
        0.- Salir
\n================================================\n""")
    while True:
        try:
            option = int(input("Ingrese una opcion: "))
            if option == 1:
                print('\n============CARGA DE ARCHIVO==============\n')
                cargarArchivo(ListaPeliculas)
                print(
                    "\n********************ARCHIVO CARGADO EXITOSAMENTE*****************\n")
                input('\nPresione enter para continuar...')
                menuPrincipal()
                break
            elif option == 2:
                gestionarPeliculas()
                break
            elif option == 3:
                filtrado()
                break
            elif option == 4:
                grafica_peliculas(ListaPeliculas)
                menuPrincipal()
                break
            elif option == 0:
                break
            else:
                print("Opcion incorrecta")
        except ValueError:
            print("Opcion incorrecta")
    exit


print("""\n============= LENGUAJES FORMALES DE PROGRAMACION B- ====================
                        201212891
                    Edgar Rolando Ramirez Lopez
========================================================================\n""")
input('\n      Presione cualquier tecla para continuar...       ')
menuPrincipal()
