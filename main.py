from Peliculas import *

ListaPeliculas = []


def cargarArchivo(lista):
    nombres = []
    ruta = input("Escriba la ruta del archivo a leer: ")
    archivo = open(ruta, 'r')
    lineas = archivo.readlines()

    for i in lineas:
        i = i.split(";")
        count = 1
        tmp_nombre = None
        tmp_actores = None
        tmp_anio = None
        tmp_genero = None
        for j in i:
            if count == 1:
                tmp_nombre = j
            elif count == 2:
                j = j.split(",")
                tmp_actores = j
            elif count == 3:
                tmp_anio = j
            elif count == 4:
                tmp_genero = j
            count += 1

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
    print('Los actores de la película seleccionada son: %s' % ','.join(actor))


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
                break
            elif option == "c":
                menuPrincipal()
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
                print('op3')
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
