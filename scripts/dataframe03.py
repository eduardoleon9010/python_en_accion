import pandas as pd

# Series de datos individuales
tiempos = pd.Series([9.58, 9.69, 9.72, 9.74, 9.77])
atletas = pd.Series(["Usain Bolt", "Usain Bolt", "Usain Bolt", "Asafa Powell", "Asafa Powell"])
paises = pd.Series(["Jamaica", "Jamaica", "Jamaica", "Jamaica", "Jamaica"])
fechas = pd.Series(["16/08/2009", "16/09/2008", "31/05/2008", "9/09/2007", "18/08/2006"])
ciudades = pd.Series(["Berlin", "Beijing", "New York", "Rieti", "Zurich"])

# Creación del diccionario de series
datos_series = {
    "tiempo": tiempos,
    "atleta": atletas,
    "pais": paises,
    "fecha": fechas,
    "ciudad": ciudades
}

# Creación del DataFrame a partir del diccionario de series
df_records3 = pd.DataFrame(datos_series)

# Muestra el DataFrame
print(df_records3)
