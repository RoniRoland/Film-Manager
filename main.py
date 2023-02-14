

def menuPrincipal():
    print("""============= LENGUAJES FORMALES DE PROGRAMACION B- =================
                        201212891
                    Edgar Rolando Ramirez Lopez
    ======================================================================""")
    input('      Presione cualquier tecla para continuar...       ')
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
                print('op1')
                break
            elif option == 2:
                print('op2')
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


menuPrincipal()
