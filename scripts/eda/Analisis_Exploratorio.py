# Tipos de variables

# Conteo de la cantidad de instancias de cada clase
conteo_clases = data['status'].value_counts()

# Visualiza la distribución de las clases en un gráfico de barras
conteo_clases.plot(kind='bar')
plt.title('Distribución de clases - Phishing vs Legitimate')
plt.xlabel('Clase')
plt.ylabel('Número de instancias')
plt.xticks(rotation=0)  # Rotación de las etiquetas del eje X para mejor legibilidad
plt.show()

# Si deseas un detalle porcentual para mejor análisis:
print("Porcentaje de la clase Phishing:", (conteo_clases['phishing'] / sum(conteo_clases)) * 100, "%")
print("Porcentaje de la clase Legitimate:", (conteo_clases['legitimate'] / sum(conteo_clases)) * 100, "%")



variable = 'length_url'
# Establece un estilo estético para los gráficos
sns.set(style="whitegrid")

# Crea el histograma para la variable seleccionada con una línea de densidad de kernel
sns.histplot(data[variable], kde=True)
plt.title(f'Distribución de la variable {variable}')
plt.xlabel(variable)
plt.ylabel('Frecuencia')
min_value = 0
max_value = 325
plt.xlim(min_value, max_value)
# Muestra el gráfico
plt.show()

# Calcula la media (promedio)
media = data[variable].mean()
print(f"Media de {variable}:", media)

# Calcula la mediana (el valor central)
mediana = data[variable].median()
print(f"Mediana de {variable}:", mediana)

# Calcula la moda (el valor más frecuente)
moda = data[variable].mode()
print(f"Moda de {variable}:", moda[0])

# Calcula la desviación estándar
desviacion_estandar = data[variable].std()
print(f"Desviación estándar de {variable}:", desviacion_estandar)



variable = 'length_hostname'
# Establece un estilo estético para los gráficos
sns.set(style="whitegrid")

# Crea el histograma para la variable seleccionada con una línea de densidad de kernel
sns.histplot(data[variable], kde=True)
plt.title(f'Distribución de la variable {variable}')
plt.xlabel(variable)
plt.ylabel('Frecuencia')
min_value = 0
max_value = 100
plt.xlim(min_value, max_value)
# Muestra el gráfico
plt.show()

# Calcula la media (promedio)
media = data[variable].mean()
print(f"Media de {variable}:", media)

# Calcula la mediana (el valor central)
mediana = data[variable].median()
print(f"Mediana de {variable}:", mediana)

# Calcula la moda (el valor más frecuente)
moda = data[variable].mode()
print(f"Moda de {variable}:", moda[0])

# Calcula la desviación estándar
desviacion_estandar = data[variable].std()
print(f"Desviación estándar de {variable}:", desviacion_estandar)



variable = 'domain_age'
# Establece un estilo estético para los gráficos
sns.set(style="whitegrid")

# Crea el histograma para la variable seleccionada con una línea de densidad de kernel
sns.histplot(data[variable], kde=True)
plt.title(f'Distribución de la variable {variable}')
plt.xlabel(variable)
plt.ylabel('Frecuencia')
min_value = 0
max_value = 12000
plt.xlim(min_value, max_value)
# Muestra el gráfico
plt.show()

# Calcula la media (promedio)
media = data[variable].mean()
print(f"Media de {variable}:", media)

# Calcula la mediana (el valor central)
mediana = data[variable].median()
print(f"Mediana de {variable}:", mediana)

# Calcula la moda (el valor más frecuente)
moda = data[variable].mode()
print(f"Moda de {variable}:", moda[0])

# Calcula la desviación estándar
desviacion_estandar = data[variable].std()
print(f"Desviación estándar de {variable}:", desviacion_estandar)



# Cálculo de estadísticas descriptivas para la variable 'avg_word_host'
media = data['avg_word_host'].mean()
mediana = data['avg_word_host'].median()
moda = data['avg_word_host'].mode()[0]

print(f"Media de 'avg_word_host': {media}")
print(f"Mediana de 'avg_word_host': {mediana}")
print(f"Moda de 'avg_word_host': {moda}")

# Creación del box plot usando seaborn
plt.figure(figsize=(10, 6))
sns.boxplot(x='status', y='avg_word_host', data=data)
plt.title("Box plot de 'avg_word_host' según el 'status'")
plt.xlabel('Status')
plt.ylabel('Promedio de palabras en el host')
plt.show()


# Establecer el estilo para los gráficos
sns.set(style="whitegrid")

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(x='domain_with_copyright', hue='status', data=data)
plt.title('Frecuencia de copyright por status del dominio')
plt.xlabel('Domain With Copyright')
plt.ylabel('Frecuencia')
plt.legend(title='Status')
plt.xticks([0, 1], ['Ausente', 'Presente'])  # Asume que 0 es ausente y 1 es presente

# Mostrar la gráfica
plt.show()





