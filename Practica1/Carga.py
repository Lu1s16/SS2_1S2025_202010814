import mysql.connector
import pyodbc
import pandas as pd 

class BD:

    def __init__(self):
        self.cnx = pyodbc.connect(r'Driver= {SQL Server}; SERVER={DESKTOP-UCSIJH1\SQLEXPRESS}; Database= {SS2_202010814_P1}; Trusted_conection= yes;')
        self.cursor = self.cnx.cursor()
        self.cursor.execute("USE SS2_202010814_P1;")


    def mostrar_base(self):
        
        #cursor1.execute("GO")
        self.cursor.execute("SELECT name FROM sys.tables;")
        row = self.cursor.fetchall()
        print(row)

    def borrar_tablas(self):
        self.cursor.execute('DROP TABLE IF EXISTS Fact_FlightsPassengers;')
        self.cursor.execute("""
                            DROP TABLE IF EXISTS Dim_Passengers;
                            DROP TABLE IF EXISTS Dim_Airports;
                            DROP TABLE IF EXISTS Dim_AirportArrival;
                            DROP TABLE IF EXISTS Dim_Pilot;
                            DROP TABLE IF EXISTS Dim_Date;
                            DROP TABLE IF EXISTS Dim_Status;
                            """)



    def crear_modelo(self):
        query = """
CREATE TABLE Dim_Passengers (
    ID INT PRIMARY KEY IDENTITY(1,1),
    PassengerID VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Gender VARCHAR(20),
    Age INT,
    Nationality VARCHAR(100)
);
 """
        
        self.cursor.execute(query)

        query = """
CREATE TABLE Dim_Airports (
    ID INT PRIMARY KEY IDENTITY(1,1),
    AirportName VARCHAR(100) NOT NULL,
    AirportCountryCode VARCHAR(10) NOT NULL,
    CountryName VARCHAR(100) NOT NULL,
    AirportContinent VARCHAR(10),
    Continents VARCHAR(50)
);"""
        self.cursor.execute(query)

        query = """CREATE TABLE Dim_AirportArrival (
	ID INT PRIMARY KEY IDENTITY(1,1),
	ArrivalAirport VARCHAR(10) NOT NULL
);"""
        self.cursor.execute(query)

        query = """CREATE TABLE Dim_Pilot(
	ID INT PRIMARY KEY IDENTITY(1,1),
	PilotName VARCHAR(50) NOT NULL
);"""

        self.cursor.execute(query)

        query = """CREATE TABLE Dim_Date (
    ID INT PRIMARY KEY IDENTITY(1,1),
    DepartureDate DATE NOT NULL,
    Day INT NOT NULL,
    Month INT NOT NULL,
    Year INT NOT NULL
);"""

        self.cursor.execute(query)

        query = """
-- Tabla estado
CREATE TABLE Dim_Status(
	ID INT PRIMARY KEY IDENTITY(1,1),
	FlightStatus VARCHAR(50) NOT NULL
);"""

        self.cursor.execute(query)

        query = """CREATE TABLE Fact_FlightsPassengers (
    ID INT PRIMARY KEY IDENTITY(1,1),
    PassengersID INT,
    AirportsID INT,
    AirportArrivalID INT,
    PilotID INT,
    DateID INT,
    StatusID INT,
    
    FOREIGN KEY (PassengersID) REFERENCES Dim_Passengers(ID),
    FOREIGN KEY (AirportsID) REFERENCES Dim_Airports(ID),
    FOREIGN KEY (AirportArrivalID) REFERENCES Dim_AirportArrival(ID),
    FOREIGN KEY (PilotID) REFERENCES Dim_Pilot(ID),
    FOREIGN KEY (DateID) REFERENCES Dim_Date(ID),
    FOREIGN KEY (StatusID) REFERENCES Dim_Status(ID)
);"""

        self.cursor.execute(query)

    def insertar_fechas(self, fechas: pd.DataFrame):
        print("Insertando fechas...")
        print(fechas.head())
        for index, c in fechas.iterrows():
           
            query = "INSERT INTO Dim_Date (DepartureDate, Day, Month, Year) "
            query += "VALUES('" + str(c["DepartureDate"]) + "','" +  str(c["Day"]) + "','" + str(c["Month"]) + "','" + str(c["Year"]) + "');"
            self.cursor.execute(query)
        

    def insertar_pasajeros(self, pasajeros: pd.DataFrame):
        print("Insertando pasajeros...")
        for index, c in pasajeros.iterrows():
           
            query = "INSERT INTO Dim_Passengers (PassengerID, FirstName, LastName, Gender, Age, Nationality) VALUES (?, ?, ?, ?, ?, ?)"
            valores =  (c["Passenger ID"], c["First Name"], str(c["Last Name"]),  c["Gender"], str(c["Age"]), c["Nationality"] )
            self.cursor.execute(query, valores)

    def insertar_Aeropuerto(self, aeropuertos: pd.DataFrame):
        print("Insertando aeropuertos...")
        for index, c in aeropuertos.iterrows():

            query = "INSERT INTO Dim_Airports (AirportName, AirportCountryCode, CountryName, AirportContinent, Continents) VALUES ( ?, ?, ?, ?, ? )"
            valores = ( c["Airport Name"], c["Airport Country Code"], c["Country Name"], c["Airport Continent"], c["Continents"] )
            self.cursor.execute(query, valores)

    def insertar_AeropuertoLlegada(self, aeropuertosLlegada: pd.DataFrame):
        print("Insertando aeropuertos llegada...")
        for index, c in aeropuertosLlegada.iterrows():

            query = "INSERT INTO Dim_AirportArrival (ArrivalAirport) VALUES (?) "
            valores = ( c["Arrival Airport"] )
            self.cursor.execute(query, valores)


    def insertar_Piloto(self, pilotos: pd.DataFrame):
        print("Insertando pilotos...")
        for index, c in pilotos.iterrows():

            query = "INSERT INTO Dim_Pilot (PilotName) VALUES (?) "
            valores = ( c["Pilot Name"] )
            self.cursor.execute(query, valores)

    def insertar_Estado(self, estados: pd.DataFrame):
        print("Insertando estados...")
        for index, c in estados.iterrows():

            query = "INSERT INTO Dim_Status (FlightStatus) VALUES (?) "
            valores = ( c["Flight Status"] )
            self.cursor.execute(query, valores)

    
    def insertar_Hechos(self, hechos: pd.DataFrame):
        print("Insertando hechos...")
        for index, c in hechos.iterrows():

            query = "INSERT INTO Fact_FlightsPassengers (PassengersID, AirportsID, AirportArrivalID, PilotID, DateID, StatusID) VALUES (?, ?, ?, ?, ?, ?) "
            valores = ( str(c["PassengerID"]), str(c["AirportID"]), str(c["ArrivalAirportID"]), str(c["PilotID"]), str(c["DepartureDateID"]), str(c["FlightStatusID"]) )
            self.cursor.execute(query, valores)

    def select(self):

        print("Tabla pasajeros")
        query = "SELECT * FROM Dim_passengers"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

        mensaje = input("Ingrese cualquier cosa para continuar...")

        print("Tabla Aeropuertos")
        query = "SELECT * FROM Dim_Airports"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

        mensaje = input("Ingrese cualquier cosa para continuar...")

        print("Tabla aeropuerto llegada")
        query = "SELECT * FROM Dim_AirportArrival"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

        mensaje = input("Ingrese cualquier cosa para continuar...")

        print("Tabla Piloto")
        query = "SELECT * FROM Dim_Pilot"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

        mensaje = input("Ingrese cualquier cosa para continuar...")

        print("Tabla Fecha")
        query = "SELECT * FROM Dim_Date"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

        mensaje = input("Ingrese cualquier cosa para continuar...")

        print("Tabla estados")
        query = "SELECT * FROM Dim_Status;"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

        mensaje = input("Ingrese cualquier cosa para continuar...")

        print("Tabla Hecho flight passengers")
        query = "SELECT * FROM Fact_FlightsPassengers"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def porcentaje_genero(self):
        query = """SELECT 
    Gender,
    COUNT(*) AS Total_Passengers,
    (COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ()) AS Percentage
FROM Dim_Passengers
GROUP BY Gender;"""
        df = pd.read_sql(query, self.cnx)

        print(df)

    def count_vuelos(self):
        query = """SELECT 
                a.CountryName,
                COUNT(f.ID) AS Total_Flights
        FROM Fact_FlightsPassengers f
            JOIN Dim_Airports a ON f.AirportsID = a.ID
        GROUP BY a.CountryName
        ORDER BY Total_Flights DESC;
        """
        df = pd.read_sql(query, self.cnx)
        print(df)

    def top_aeropuertos(self):

        query = """SELECT TOP 5
    a.AirportName,
    a.CountryName,
    COUNT(f.PassengersID) AS Total_Passengers
FROM Fact_FlightsPassengers f
JOIN Dim_Airports a ON f.AirportsID = a.ID
GROUP BY a.AirportName, a.CountryName
ORDER BY Total_Passengers DESC;
"""

        df = pd.read_sql(query, self.cnx)
        print(df)
    
    def count_estados(self):
        query = """SELECT 
    s.FlightStatus,
    COUNT(f.ID) AS Total_Flights
    FROM Fact_FlightsPassengers f
    JOIN Dim_Status s ON f.StatusID = s.ID
    GROUP BY s.FlightStatus
    ORDER BY Total_Flights DESC;
    """
        df = pd.read_sql(query, self.cnx)
        print(df)   

    def paises_visitados(self): #listo
        query = """SELECT TOP 5
    a.CountryName AS Destination_Country,
    COUNT(f.ID) AS Total_Flights
FROM Fact_FlightsPassengers f
JOIN Dim_AirportArrival aa ON f.AirportArrivalID = aa.ID
JOIN Dim_Airports a ON aa.ArrivalAirport = a.AirportContinent
GROUP BY a.CountryName
ORDER BY Total_Flights DESC;
"""
        df = pd.read_sql(query, self.cnx)
        print(df)

    def continentes_visitados(self):

        query = """SELECT TOP 5
    a.Continents AS Destination_Continent,
    COUNT(f.ID) AS Total_Flights
FROM Fact_FlightsPassengers f
JOIN Dim_AirportArrival aa ON f.AirportArrivalID = aa.ID
JOIN Dim_Airports a ON aa.ArrivalAirport = a.AirportContinent
GROUP BY a.Continents
ORDER BY Total_Flights DESC;
"""
        df = pd.read_sql(query, self.cnx)
        print(df)

    def edades(self):
        query = """WITH AgeGenderCount AS (
            SELECT 
                p.Gender,
                p.Age,
                COUNT(f.ID) AS Total_Flights
            FROM Fact_FlightsPassengers f
            JOIN Dim_Passengers p ON f.PassengersID = p.ID
            GROUP BY p.Gender, p.Age
        )
        SELECT TOP 5
            Gender,
            Age,
            Total_Flights
        FROM AgeGenderCount
        ORDER BY Total_Flights DESC;
        """
        df = pd.read_sql(query, self.cnx)
        print(df)

    def vuelos(self):
        
        query = """SELECT 
        FORMAT(d.DepartureDate, 'MM-yyyy') AS Month_Year,
        COUNT(f.ID) AS Total_Flights
        FROM Fact_FlightsPassengers f
        JOIN Dim_Date d ON f.DateID = d.ID
        GROUP BY FORMAT(d.DepartureDate, 'MM-yyyy')
        ORDER BY MIN(d.DepartureDate) ASC;
        """
        df = pd.read_sql(query, self.cnx)
        print(df)

    def cerrar_conexion(self):
        self.cnx.close()
            
               
            

            


        