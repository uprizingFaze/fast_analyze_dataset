import pandas as pd
import sys

def analizar_csv(ruta_csv):
    # Cargar el archivo CSV en un DataFrame de Pandas
    datos = pd.read_csv(ruta_csv)

    # Mostrar información básica sobre el DataFrame
    print("Información básica del DataFrame:")
    print("Número de filas:", datos.shape[0])
    print("Número de columnas:", datos.shape[1])
    print("\n")

    # Realizar análisis adicional
    print("Algunos resultados generales:")
    # Por ejemplo, mostrar los primeros registros
    print("Primeros registros del DataFrame:")
    print(datos.head())
    print("\n")

    # Calcular estadísticas descriptivas para columnas numéricas
    print("Estadísticas descriptivas para columnas numéricas:")
    print(datos.describe())
    print("\n")

    # Contar valores únicos en cada columna
    print("Valores únicos en cada columna:")
    for columna in datos.columns:
        print(columna + ":", datos[columna].nunique())
    print("\n")

    # Realizar más análisis según sea necesario

# Ruta al archivo CSV
ruta_archivo = "ejemplo.csv"  # Reemplaza "ejemplo.csv" con tu ruta de archivo real

# Llamar a la función para analizar el CSV
analizar_csv(ruta_archivo)


def main():
    if len(sys.argv) != 2:
        print("Uso: fast-analice-dataset <ruta_csv>")
        sys.exit(1)
    
    ruta_csv = sys.argv[1]
    analizar_csv(ruta_csv)

if __name__ == "__main__":
    main()
