from Extraccion import extraer
from Transformacion import dataFrame
from Carga import BD

database = BD()


def CargarRuta():

    try:
        ruta: str = input("Ingrese la ruta del .csv: ")

        df = extraer(ruta)
        return df

    except TypeError:
        print("Error al ingresar la ruta")

#C:\Users\Luis\Documents\Cursos\Semi2\Practica1\VuelosDataSet.csv

#Copia
#C:\Users\Luis\Documents\Cursos\Semi2\Practica1\copia\VuelosDataSet.csv

#C:\Users\Ale Garcia\Desktop\VuelosDataSet.csv


def Menu_consultas():

    

    salir = False
    while not salir:

        print("---------Menu de consultas----------")
        print("1. Select")
        print("2. Porcentaje de pasajeros por género.")
        print("3. Nacionalidades con su mes año de mayor fecha de salida.  ")
        print("4. COUNT de vuelos por país.")
        print("5. Top 5 aeropuertos con mayor número de pasajeros.")
        print("6. COUNT dividido por estado de vuelo.  ")
        print("7. Top 5 de los países más visitados. ")
        print("8. Top 5 de los continentes más visitados.  ")
        print("9. Top 5 de edades divido por género que más viajan.")
        print("10. COUNT de vuelos por MM-YYYY.")
        print("-------------------------")
        print("Seleccione una opcion: ")

        try:
            op = int(input())
    
            if op == 1:
                database.select()
                

            elif op == 2:
                database.porcentaje_genero()
                
            elif op == 3:
                pass

            elif op == 4:
                database.count_vuelos()

            elif op == 5:
                database.top_aeropuertos()

            elif op == 6:
                database.count_estados()

            elif op == 7:
                database.paises_visitados()

            elif op == 8:
                database.continentes_visitados()

            elif op == 9:
                database.edades()

            elif op == 10:
                database.vuelos()

            elif op == 11:
                salir = True

            else:
                print("Opcion invalida \n")

        except ValueError:
            print("Error: Debe ingresar solo numeros \n")


def Menu():

    database.mostrar_base()

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

                database.borrar_tablas()
                cargar_datos = False
                print("Tablas borradas correctamente.")
                database.mostrar_base()

            elif op == 2:
                
                database.crear_modelo()
                print("Modelo creado correctamente")
                database.mostrar_base()


            elif op == 3:
                df = CargarRuta()
                cargar_datos = True
                print("Datos extraidos")

            elif op == 4:
                if(cargar_datos):
                    data = dataFrame(df)
                    dim_fecha = data.dimension_fecha()
                    dim_pasajeros = data.dimension_pasajeros()
                    dim_aeropuertos = data.dimension_aeropuerto()
                    dim_aeropuertosLlegada = data.dimension_aeropuertoLlegada()
                    dim_pilotos = data.dimension_piloto()
                    dim_estados = data.dimension_estados()
                    fact = data.tabla_hechos(
                        dim_fecha, 
                        dim_pasajeros, 
                        dim_aeropuertos, 
                        dim_aeropuertosLlegada,
                        dim_pilotos, 
                        dim_estados)
                    
                    #Realizar carga 
                    database.insertar_fechas(dim_fecha)
                    database.insertar_pasajeros(dim_pasajeros)
                    database.insertar_Aeropuerto(dim_aeropuertos)
                    database.insertar_AeropuertoLlegada(dim_aeropuertosLlegada)
                    database.insertar_Piloto(dim_pilotos)
                    database.insertar_Estado(dim_estados)
                    database.insertar_Hechos(fact)
                    hacer_consultas = True            


                else:
                    print("Aun no se han cargado datos para transformar")

                pass

            elif op == 5:     
                Menu_consultas()


            elif op == 6:
                database.cerrar_conexion()
                salir = True

            else:
                print("Opcion invalida \n")

        except ValueError:
            print("Error: Debe ingresar solo numeros \n")



if __name__ == '__main__':
    Menu()
