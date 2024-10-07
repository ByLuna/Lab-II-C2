import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset de Moto GP con la ruta correcta
moto_data = pd.read_csv(r"C:\Users\Admin\Documents\python a3\LabII\grand-prix-race-winners.csv")
#Link de Descarga del Dataset: https://www.kaggle.com/datasets/alrizacelk/moto-gp-world-championship19492022

# Agrupar las victorias por piloto (Rider) y contar el número de victorias
victorias_por_piloto = moto_data.groupby('Rider')['Season'].count().sort_values(ascending=False)

# Seleccionar solo los 50 pilotos con más victorias
top_50_pilotos = victorias_por_piloto.head(50)

# Crear gráfico de barras
plt.figure(figsize=(12, 6))
top_50_pilotos.plot(kind='bar', color='skyblue')
plt.title('Número de Victorias por Piloto en Moto GP (Top 50)')
plt.xlabel('Piloto')
plt.ylabel('Número de Victorias')
plt.xticks(rotation=90)
plt.show()



# Contar el número de carreras por año
carreras_por_ano = moto_data.groupby('Season')['Circuit'].count()

# Crear gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(carreras_por_ano.index, carreras_por_ano.values, marker='o', color='green')
plt.title('Número de Carreras de Moto GP por Año')
plt.xlabel('Año')
plt.ylabel('Número de Carreras')
plt.grid(True)
plt.show()



# Contar victorias por fabricante (Constructor)
victorias_por_fabricante = moto_data['Constructor'].value_counts().head(10)  # Tomamos los 10 fabricantes con más victorias

# Crear gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(victorias_por_fabricante, labels=victorias_por_fabricante.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Victorias por Fabricante (Top 10)')
plt.axis('equal')  # Asegura que el gráfico sea circular
plt.show()

#Observacion acerca de los graficos 
'''En la Grafica de barras tenemos al primer piloto que es Giacomo Agostini que encabeza el numero de victorias con un total de 120 victorias,
 en segundo lugar tenemos a Valentino Rossi con un poco mas de 100 victorias encabeza el segundo lugar, luego tenemos a Angel Nieto en tercer
 lugar con 90 victorias llevando este el tercer lugar.

En el grafico de Lineas tenemos el numero de carreras de moto, del año 1950 a 1960 vemos que tuvo varios bajones luego de 1960 a 1970
 comenzó a elevarse el numero de carreras llegando a su punto mas alto entre los años 2010 y 2020.

En la Grafica Circular tenemos la Distribución de Victorias por Fabricante teniendo mas porcentaje honda con un 30.7%
 y en segundo lugar tenemos ah Yamaha con un 21.1% seguidamente tenemos a Aprilia con un 11.4% y a MV Agusta con un 10.0%'''
