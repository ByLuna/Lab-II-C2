import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset de F1
f1_data = pd.read_csv(r'C:\Users\Admin\Documents\python a3\LabII\F1  1950 -2020 Race Wins.csv')
#Enlace al Dataset https://www.kaggle.com/datasets/saiishwaram/f1-all-race-winners-19502021

# Agrupar las victorias por coche (CAR) y contar el número de victorias
victorias_por_coche = f1_data.groupby('CAR')['WINNER'].count().sort_values(ascending=False)

# Crear gráfico de barras
plt.figure(figsize=(12, 6))
victorias_por_coche.plot(kind='bar', color='skyblue')
plt.title('Número de Victorias por Equipo en Fórmula 1 (1950-2020)')
plt.xlabel('Equipo')
plt.ylabel('Número de Victorias')
plt.xticks(rotation=90)
plt.show()

# Convertir la columna de fechas a un formato datetime
f1_data['DATE'] = pd.to_datetime(f1_data['DATE'], errors='coerce')

# Extraer el año de la columna de fechas
f1_data['YEAR'] = f1_data['DATE'].dt.year

# Contar el número de carreras por año
carreras_por_ano = f1_data.groupby('YEAR')['GRAND PRIX'].count()

# Crear gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(carreras_por_ano.index, carreras_por_ano.values, marker='o', color='green')
plt.title('Número de Carreras de F1 por Año (1950-2020)')
plt.xlabel('Año')
plt.ylabel('Número de Carreras')
plt.grid(True)
plt.show()

# Contar victorias por piloto
victorias_por_piloto = f1_data['WINNER'].value_counts().head(10)  # Tomamos los 10 pilotos con más victorias

# Crear gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(victorias_por_piloto, labels=victorias_por_piloto.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Victorias por Piloto (Top 10)')
plt.axis('equal')  # Asegura que el gráfico sea circular
plt.show()

#Observacion acerca de los graficos

'''En este caso En el primer grafico que es de barras podemos ver que el numero de victorias por equipos
 es encabezado por Ferrari dándonos a entender que en este modo ellos son el equipo que mas sobresale siguiendo por atrás tenemos a
 mercedes que sigue a Ferrari no tan de cerca pero va a ala cola 

en el segundo grafico que es el de líneas podemos ver que al comienzo de la grafica ente el numero de carreras de 14 y 16 hubo una
 fluctuacion de arriba abjo luego quedando estable en 16 luego de eso comienza a tender a ir hacia arriba llegando a 20 carreras luego
   de eso cae en picada hasta menos de 8, se pudo recuperar y comenzó a subir nuevamente

Luego en la grafica de círculos tenemos en top 10 de las victorias encabezando la grafica tenemos a Lewis Hamilton detrás de el tenemos
 Michael Schumacher  y en tercer lugar tenemos a Sebastian Vettel dándonos a entender que ellos 3 encabezan el top 10 de victorias Lewis
   en primero con un 20.2% luego Michael con un 19.3% y por ultimo Sebastian con un 11.3% '''
