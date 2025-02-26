import pandas as pd 


def extraer(ruta):

    try:
            

        #Listado de registros
        df = pd.read_csv(ruta)
        print("Numero de registros: ", len(df))
        print("Primeras 5 filas:")
        print(df.head())
        print("ultimas 5 filas")
        print(df.tail())
        print(type(df))
        return df
        
    except Exception as e:
        print("Error al leer el archivo")
        print(e)
        return 0
        
