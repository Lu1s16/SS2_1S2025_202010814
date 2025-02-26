USE SS2_202010814_P1;
GO


-- Tabla pasajeros
CREATE TABLE Dim_Passengers (
    ID INT PRIMARY KEY IDENTITY(1,1),
    PassengerID VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Gender VARCHAR(20),
    Age INT,
    Nationality VARCHAR(20)
);


-- Tabla aeropuerto
CREATE TABLE Dim_Airports (
    ID INT PRIMARY KEY IDENTITY(1,1),
    AirportName VARCHAR(50) NOT NULL,
    AirportCountryCode VARCHAR(10) NOT NULL,
    CountryName VARCHAR(50) NOT NULL,
    AirportContinent VARCHAR(10),
    Continents VARCHAR(50)
);

-- Tabla aeropuerto destino
CREATE TABLE Dim_AirportArrival (
	ID INT PRIMARY KEY IDENTITY(1,1),
	ArrivalAirport VARCHAR(10) NOT NULL
);


-- Tabla piloto
CREATE TABLE Dim_Pilot(
	ID INT PRIMARY KEY IDENTITY(1,1),
	PilotName VARCHAR(50) NOT NULL
);


-- Tabla fecha
CREATE TABLE Dim_Date (
    ID INT PRIMARY KEY IDENTITY(1,1),
    DepartureDate DATE NOT NULL,
    Day INT NOT NULL,
    Month INT NOT NULL,
    Year INT NOT NULL
);

-- Tabla estado
CREATE TABLE Dim_Status(
	ID INT PRIMARY KEY IDENTITY(1,1),
	FlightStatus VARCHAR(50) NOT NULL
);


-- Tabla hechos
CREATE TABLE Fact_FlightsPassengers (
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
);
