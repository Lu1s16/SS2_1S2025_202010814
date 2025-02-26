import pandas as pd 

class dataFrame():

    def __init__(self, df: pd.DataFrame):
        self.df = df


    def dimension_fecha(self):
        print("Procesando fechas...")

        def convertir_dates(date_str):
            
            for fmt in ('%m/%d/%Y', '%m-%d-%Y'):
                try:
                    return pd.to_datetime(date_str, format=fmt)

                except ValueError:
                    continue 

            return pd.Nat


        #Normalizamos las fechas de la columna "departure Date"
        #Nombre de la columna del archivo
        self.df["DepartureDate"] = self.df['Departure Date'].apply(convertir_dates)

        #Eliminar duplicados de columnas para tener valores unicos

        dim_fecha = self.df[["DepartureDate"]].drop_duplicates()
        #Asignar id a cada valor
        dim_fecha["ID"] = range(1, len(dim_fecha) + 1)

        #Desglosar fecha en año, mes y dia
        dim_fecha["Year"] = dim_fecha["DepartureDate"].dt.year
        dim_fecha["Month"] = dim_fecha["DepartureDate"].dt.month
        dim_fecha["Day"] = dim_fecha["DepartureDate"].dt.day 

        print("Dimension fecha:")
        print(dim_fecha.head())

        return dim_fecha


    def dimension_pasajeros(self):
        print("Procesando pasajeros...")

        #Passenger ID
        #First Name
        #Last Name
        #Gender
        #Age
        #Nationality
        try:
            

            dim_pasajeros = self.df[["Passenger ID", "First Name", "Last Name", "Gender", "Age", "Nationality"]].drop_duplicates()

            dim_pasajeros["ID"] = range(1, len(dim_pasajeros) + 1)

            print("Dimension Pasajeros:")
            print(dim_pasajeros.head())

            return dim_pasajeros
        
        except Exception as e:
            print("Error al procesar pasajeros")
            print(e)
            return 
        
    def dimension_aeropuerto(self):
        print("Procesando aeropuertos...")

        #Airport Name
        #Airport Country Code 
        #Airport Continent
        #Continents
        #Coldfoot Airport

        try:

            def Convertir_mayuscula(cadena):
                if isinstance(cadena, str):
                    return cadena.upper()

            self.df["Airport Country Code"] = self.df["Airport Country Code"].apply(Convertir_mayuscula)
            self.df["Airport Continent"] = self.df["Airport Continent"].apply(Convertir_mayuscula)

            dim_aeropuertos = self.df[["Airport Name", "Airport Country Code", "Airport Continent", "Continents"]].drop_duplicates()
            dim_aeropuertos["ID"] = range(1, len(dim_aeropuertos) + 1)

            print("Dimension aeropuertos:")
            print(dim_aeropuertos.head())

            return dim_aeropuertos

        except Exception as e:
            print("Error al procesar pasajeros.")
            print(e)
            
            return


    def dimension_aeropuertoLlegada(self):
        print("Procesando aeropuertos llegadas...")
        #Arrival Airport

        try:
            def Convertir_mayuscula(cadena):
                if isinstance(cadena, str):
                    return cadena.upper()
                
            self.df["Arrival Airport"] = self.df["Arrival Airport"].apply(Convertir_mayuscula)

            dim_aeropuertoLlegada = self.df[["Arrival Airport"]].drop_duplicates()
            dim_aeropuertoLlegada["ID"] = range(1, len(dim_aeropuertoLlegada) + 1)

            print("Dimension aeropuerto llegada:")
            print(dim_aeropuertoLlegada.head())

            return dim_aeropuertoLlegada

        
        except Exception as e:
            print("Error al procesar aeropuertos llegadas")
            print(e)

    def dimension_piloto(self):
        print("Procesando pilotos...")

        #Pilot Name
        try:

            dim_pilotos = self.df[["Pilot Name"]].drop_duplicates()
            dim_pilotos["ID"] = range(1, len(dim_pilotos) + 1)

            print("Dimension pilotos:")
            print(dim_pilotos.head())

            return dim_pilotos

        except Exception as e:
            print("Error al procesar pilotos")
            print(e)
            return
        
    def dimension_estados(self):
        print("Procesando estados...")

        #Flight Status
        try:

            dim_estados = self.df[["Flight Status"]].drop_duplicates()
            dim_estados["ID"] = range(1, len(dim_estados)+ 1)

            print("Dimension estados:")
            print(dim_estados.head())

            return dim_estados

        except Exception as e:
            print("Error al procesar estados")
            print(e)
            return 