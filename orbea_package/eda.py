import pandas as pd
from faker import Faker


def importar_dataset(filepath):
    """
    Importa un archivo CSV en un DataFrame de Pandas.
    Args:
        filepath (str): Ruta al archivo CSV.
    Returns:
        pd.DataFrame: DataFrame con los datos del archivo.
    """
    return pd.read_csv(filepath, delimiter=';')


def mostrar_5_primeros(df):
    """
    Muestra los 5 primeros valores de un DataFrame.
    Args:
        df (pd.DataFrame): DataFrame a analizar.
    Returns:
        pd.DataFrame: Primeros 5 registros del DataFrame.
    """
    return df.head()


def contar_ciclistas(df):
    """
    Cuenta el número de ciclistas en el DataFrame.
    Args:
        df (pd.DataFrame): DataFrame a analizar.
    Returns:
        int: Número total de ciclistas.
    """
    return len(df)


def obtener_columnas(df):
    """
    Obtiene las columnas de un DataFrame.
    Args:
        df (pd.DataFrame): DataFrame a analizar.
    Returns:
        list: Lista de nombres de columnas.
    """
    return df.columns.tolist()


def name_surname(df):
    """
    Anonimiza los nombres de los ciclistas usando la librería Faker.
    Args:
        df (pd.DataFrame): DataFrame con la columna 'biker'.
    Returns:
        pd.DataFrame: DataFrame con los nombres anonimizados.
    """
    fake = Faker()
    df['biker'] = df['biker'].apply(lambda _: f"{fake.first_name()} {fake.last_name()}")
    return df


def remove_non_participants(df):
    """
    Elimina los ciclistas con tiempo '00:00:00'.
    Args:
        df (pd.DataFrame): DataFrame a limpiar.
    Returns:
        pd.DataFrame: DataFrame sin ciclistas no participantes.
    """
    return df[df['time'] != '00:00:00']

def get_cyclist_by_dorsal(df, dorsal):
    """
    Recupera los datos de un ciclista por su dorsal.
    Args:
        df (pd.DataFrame): DataFrame a analizar.
        dorsal (int): Dorsal del ciclista.
    Returns:
        pd.Series: Registro del ciclista con el dorsal especificado.
    """
    return df[df['dorsal'] == dorsal]


if __name__ == "__main__":
    # Ruta al dataset
    filepath = "data/dataset.csv"

    # Cargar el dataset
    print("Cargando dataset desde:", filepath)
    try:
        df = importar_dataset(filepath)
        print("Dataset cargado correctamente.\n")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {filepath}.")
        exit()

    # Mostrar los 5 primeros registros
    print("Mostrando los 5 primeros registros:")
    print(mostrar_5_primeros(df))

    # Contar ciclistas
    print(f"\nNúmero total de ciclistas: {contar_ciclistas(df)}")

    # Mostrar columnas
    print("\nColumnas del dataset:")
    print(obtener_columnas(df))

    # Anonimizar nombres
    print("\nAnonimizando nombres de los ciclistas...")
    df = name_surname(df)
    print("Primeros 5 registros después de anonimizar:")
    print(mostrar_5_primeros(df))

    # Eliminar ciclistas no participantes
    print("\nEliminando ciclistas no participantes...")
    df = remove_non_participants(df)
    print(f"Ciclistas restantes: {contar_ciclistas(df)}")

    # Recuperar datos del ciclista con dorsal=1000
    print("\nRecuperando datos del ciclista con dorsal=1000...")
    cyclist = get_cyclist_by_dorsal(df, 1000)
    if not cyclist.empty:
        print(cyclist)
    else:
        print("No se encontró un ciclista con el dorsal 1000.")
