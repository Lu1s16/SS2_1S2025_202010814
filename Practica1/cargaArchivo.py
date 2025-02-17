import pandas as pd

class CargaArchivo:

    def __init__(self, ruta: str):
        self.ruta = ruta

    def extraer(self):

        try:

            #Listado de registros
            df = pd.read_csv(self.ruta)
            print(df.head())
            print(df.tail())
            return df
        
        except Exception as e:
            print("Error al leer el archivo")
            print(e)
            return 


