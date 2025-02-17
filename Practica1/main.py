import cargaArchivo as ca



def extraerModelo():

    try:
        ruta: str = input("Ingrese la ruta del .csv: ")

        carga = ca.CargaArchivo(ruta)
        carga.extraer()

    except TypeError:
        print("Error al ingresar la ruta")



def Menu():

    salir = False

    while not salir:


        print("---------Menu----------")
        print("1. Borrar modelo")
        print("2. Crear modelo")
        print("3. Extraer modelo")
        print("4. Cargar informacion")
        print("5. Realizar consultas")
        print("6. Salir")
        print("-------------------------")
        print("Seleccione una opcion: ")

        

        try:
            op = int(input())
    
            if op == 1:
                pass

            elif op == 2:
                pass

            elif op == 3:
                extraerModelo()

            elif op == 4:
                pass

            elif op == 5:
                pass

            elif op == 6:
                salir = True

            else:
                print("Opcion invalida \n")

        except ValueError:
            print("Error: Debe ingresar solo numeros \n")



if __name__ == '__main__':
    Menu()
