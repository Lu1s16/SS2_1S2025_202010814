from Extraccion import extraer
from Transformacion import dataFrame


def CargarRuta():

    try:
        ruta: str = input("Ingrese la ruta del .csv: ")

        df = extraer(ruta)
        return df

    except TypeError:
        print("Error al ingresar la ruta")

#C:\Users\Luis\Documents\Cursos\Semi2\Practica1\VuelosDataSet.csv

def Menu():

    salir = False
    cargar_datos = False

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
                df = CargarRuta()
                cargar_datos = True

            elif op == 4:
                if(cargar_datos):
                    data = dataFrame(df)
                    #dim_fecha = data.dimension_fecha()
                    #dim_pasajeros = data.dimension_pasajeros()
                    #dim_aeropuertos = data.dimension_aeropuerto()
                    #dim_aeropuertosLlegada = data.dimension_aeropuertoLlegada()
                    #dim_pilotos = data.dimension_piloto()
                    dim_estados = data.dimension_estados()
                else:
                    print("Aun no se han cargado datos para transformar")

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
