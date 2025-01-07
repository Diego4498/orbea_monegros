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