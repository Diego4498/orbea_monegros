import pandas as pd
import matplotlib.pyplot as plt


def minutes_002040(time):
    """
    Agrupa un tiempo en formato hh:mm:ss en franjas de 20 minutos.
    Args:
        time (str): Tiempo en formato hh:mm:ss.
    Returns:
        str: Tiempo agrupado en formato hh:mm (minutos en 00, 20 o 40).
    """
    h, m, _ = map(int, time.split(':'))
    if m < 20:
        m = '00'
    elif m < 40:
        m = '20'
    else:
        m = '40'
    return f"{h:02}:{m}"


def group_and_plot_histogram(df):
    """
    Agrupa los tiempos en franjas de 20 minutos y genera un histograma.
    Args:
        df (pd.DataFrame): DataFrame con la columna 'time'.
    Returns:
        pd.DataFrame: DataFrame con los grupos y el número de ciclistas en cada franja.
    """
    df['time_grouped'] = df['time'].apply(minutes_002040)
    grouped = df.groupby('time_grouped').size().reset_index(name='count')

    # Crear el histograma
    plt.bar(grouped['time_grouped'], grouped['count'])
    plt.xlabel('Tiempos agrupados')
    plt.ylabel('Número de ciclistas')
    plt.title('Histograma de tiempos agrupados')
    plt.xticks(rotation=45)
    plt.savefig('img/histograma.png')
    plt.close()

    return grouped


if __name__ == "__main__":
    # Ruta al dataset
    filepath = "data/dataset.csv"

    # Cargar el dataset
    print("Cargando dataset desde:", filepath)
    try:
        df = pd.read_csv(filepath, delimiter=';')
        print("Dataset cargado correctamente.\n")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {filepath}.")
        exit()

    # Agrupar tiempos en franjas de 20 minutos
    print("Agrupando tiempos en franjas de 20 minutos...")
    df['time_grouped'] = df['time'].apply(minutes_002040)
    print("Primeros 15 registros con tiempos agrupados:")
    print(df[['time', 'time_grouped']].head(15))

    # Generar y guardar el histograma
    print("\nGenerando histograma de tiempos agrupados...")
    grouped = group_and_plot_histogram(df)
    print("Histograma guardado en 'img/histograma.png'.")
    print("\nDatos agrupados:")
    print(grouped)
