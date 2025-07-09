# -----------------------------
# Análisis descriptivo de variables
# -----------------------------

# Distribución de clases objetivo (status: phishing vs legitimate)
conteo_clases = data['status'].value_counts()
conteo_clases.plot(kind='bar')
plt.title('Distribución de clases - Phishing vs Legitimate')
plt.xlabel('Clase')
plt.ylabel('Número de instancias')
plt.xticks(rotation=0)
plt.show()

print("Porcentaje de la clase Phishing:", (conteo_clases['phishing'] / sum(conteo_clases)) * 100, "%")
print("Porcentaje de la clase Legitimate:", (conteo_clases['legitimate'] / sum(conteo_clases)) * 100, "%")

# -----------------------------
# Estadísticas para length_url
# -----------------------------

variable = 'length_url'
sns.set(style="whitegrid")
sns.histplot(data[variable], kde=True)
plt.title(f'Distribución de la variable {variable}')
plt.xlabel(variable)
plt.ylabel('Frecuencia')
plt.xlim(0, 325)
plt.show()

print(f"Media de {variable}:", data[variable].mean())
print(f"Mediana de {variable}:", data[variable].median())
print(f"Moda de {variable}:", data[variable].mode()[0])
print(f"Desviación estándar de {variable}:", data[variable].std())

# -----------------------------
# Estadísticas para length_hostname
# -----------------------------

variable = 'length_hostname'
sns.set(style="whitegrid")
sns.histplot(data[variable], kde=True)
plt.title(f'Distribución de la variable {variable}')
plt.xlabel(variable)
plt.ylabel('Frecuencia')
plt.xlim(0, 100)
plt.show()

print(f"Media de {variable}:", data[variable].mean())
print(f"Mediana de {variable}:", data[variable].median())
print(f"Moda de {variable}:", data[variable].mode()[0])
print(f"Desviación estándar de {variable}:", data[variable].std())

# -----------------------------
# Estadísticas para domain_age
# -----------------------------

variable = 'domain_age'
sns.set(style="whitegrid")
sns.histplot(data[variable], kde=True)
plt.title(f'Distribución de la variable {variable}')
plt.xlabel(variable)
plt.ylabel('Frecuencia')
plt.xlim(0, 12000)
plt.show()

print(f"Media de {variable}:", data[variable].mean())
print(f"Mediana de {variable}:", data[variable].median())
print(f"Moda de {variable}:", data[variable].mode()[0])
print(f"Desviación estándar de {variable}:", data[variable].std())

# -----------------------------
# Estadísticas y boxplot de avg_word_host
# -----------------------------

media = data['avg_word_host'].mean()
mediana = data['avg_word_host'].median()
moda = data['avg_word_host'].mode()[0]

print(f"Media de 'avg_word_host': {media}")
print(f"Mediana de 'avg_word_host': {mediana}")
print(f"Moda de 'avg_word_host': {moda}")

plt.figure(figsize=(10, 6))
sns.boxplot(x='status', y='avg_word_host', data=data)
plt.title("Box plot de 'avg_word_host' según el 'status'")
plt.xlabel('Status')
plt.ylabel('Promedio de palabras en el host')
plt.show()

# -----------------------------
# Análisis de variable categórica domain_with_copyright
# -----------------------------

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.countplot(x='domain_with_copyright', hue='status', data=data)
plt.title('Frecuencia de copyright por status del dominio')
plt.xlabel('Domain With Copyright')
plt.ylabel('Frecuencia')
plt.legend(title='Status')
plt.xticks([0, 1], ['Ausente', 'Presente'])
plt.show()
