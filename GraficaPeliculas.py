import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset de Netflix desde la ruta local
netflix_data = pd.read_csv(r'C:\Users\Admin\Documents\python a3\LabII\netflix_titles.csv')
#Link de Descarga del Dataset: https://www.kaggle.com/datasets/shivamb/netflix-shows

# Convertir la columna 'release_year' a formato numérico y eliminar filas con valores nulos en 'release_year'
netflix_data['release_year'] = pd.to_numeric(netflix_data['release_year'], errors='coerce')
netflix_data = netflix_data.dropna(subset=['release_year'])

# Filtrar el dataset para incluir solo años válidos (entre 1900 y 2024)
netflix_data = netflix_data[(netflix_data['release_year'] >= 1900) & (netflix_data['release_year'] <= 2024)]

# 1. Gráfico de barras: Contar la cantidad de películas y series por año
content_count = netflix_data.groupby(['release_year', 'type']).size().unstack(fill_value=0)
content_count.plot(kind='bar', figsize=(14, 7), color=['skyblue', 'salmon'])
plt.title('Número de Películas y Series en Netflix por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.legend(title='Tipo de Contenido')
plt.show()

# 2. Gráfico de líneas: Contar el número total de títulos añadidos por año
titles_per_year = netflix_data.groupby('release_year')['title'].count()
plt.figure(figsize=(10, 6))
plt.plot(titles_per_year.index, titles_per_year.values, marker='o', color='green')
plt.title('Número Total de Títulos en Netflix por Año')
plt.xlabel('Año')
plt.ylabel('Número de Títulos')
plt.grid(True)
plt.show()

# 3. Gráfico circular: Mostrar la distribución del contenido en Netflix según tipo (Películas vs Series)
content_distribution = netflix_data['type'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(content_distribution, labels=content_distribution.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'salmon'])
plt.title('Distribución de Contenido en Netflix (Películas vs Series)')
plt.axis('equal')  # Asegura que el gráfico sea circular
plt.show()

#Observacion acerca de los graficos
'''En la primera grafica podemos ver que desde 1925 a 1975 siempre hubo poca actividad y eran pocos los que veían peliculas a partir
de 1985 comienza a aumentar la tendiacia de las peliculas y comienza a ir en incremento teniendo su punto máximo en los años 2017 y 2018
llegando a mas de 750 peliculas en cambio con las series están comenzaron a generar popularidad desde los 2000 en adelante teniendo su 
punto máximo en 2020.

En la segunda Grafica podemos ver como la linea tiende a ir por bajo hasta el año 2000 que comienzan a ser mas populares las 
peliculas llegando a su punto mas alto cerca de los 2020 ósea entre 2017 y 2020

En la Tercera Grafica podemos ver lo que las personas suelen preferir en este casos serian mas las peliculas que las series 
teniendo las peliculas un 69.6% y las series un 30.4%
'''
 