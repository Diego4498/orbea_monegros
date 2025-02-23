import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt
import re
from orbea_package.eda import (
    importar_dataset,
    mostrar_5_primeros,
    contar_ciclistas,
    obtener_columnas,
    name_surname,
    remove_non_participants,
    get_cyclist_by_dorsal,
)
from orbea_package.grouping import minutes_002040, group_and_plot_histogram
from orbea_package.clubs import clean_club, process_clubs, analyze_ucsc


def importar_dataset(filepath):
    return pd.read_csv(filepath, delimiter=';')


def mostrar_5_primeros(df):
    return df.head()


def contar_ciclistas(df):
    return len(df)


def obtener_columnas(df):
    return df.columns.tolist()


def name_surname(df):
    fake = Faker()
    df['biker'] = df['biker'].apply(lambda _: f"{fake.first_name()} {fake.last_name()}")
    return df


def remove_non_participants(df):
    return df[df['time'] != '00:00:00']


def get_cyclist_by_dorsal(df, dorsal):
    return df[df['dorsal'] == dorsal]


def minutes_002040(time):
    h, m, _ = map(int, time.split(':'))
    if m < 20:
        m = '00'
    elif m < 40:
        m = '20'
    else:
        m = '40'
    return f"{h:02}:{m}"


def group_and_plot_histogram(df):
    df['time_grouped'] = df['time'].apply(minutes_002040)
    grouped = df.groupby('time_grouped').size().reset_index(name='count')
    plt.bar(grouped['time_grouped'], grouped['count'])
    plt.xlabel('Tiempos agrupados')
    plt.ylabel('Número de ciclistas')
    plt.title('Histograma de tiempos agrupados')
    plt.xticks(rotation=45)
    plt.savefig('img/histograma.png')
    plt.close()
    return grouped


def clean_club(club):
    club = club.upper()
    replacements = [
        'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ',
        'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ', 'CLUB CICLISTA ', 'CLUB '
    ]
    for r in replacements:
        club = club.replace(r, '')

    club = re.sub(r'^(C\.C\.|C\.C|CC|C\.D\.|C\.D|CD|A\.C\.|A\.C|AC|A\.D\.|A\.D|AD|A\.E\.|A\.E|AE|E\.C\.|E\.C|EC|S\.C\.|S\.C|SC|S\.D\.|S\.D|SD)\s+', '', club)
    club = re.sub(r'\s+(T\.T\.|T\.T|TT|T\.E\.|T\.E|TE|C\.C\.|C\.C|CC|C\.D\.|C\.D|CD|A\.D\.|A\.D|AD|A\.C\.|A\.C|AC)$', '', club)
    return club.strip()


def process_clubs(df):
    df['club_clean'] = df['club'].apply(clean_club)
    grouped_clubs = df.groupby('club_clean').size().reset_index(name='count').sort_values(by='count', ascending=False)
    return grouped_clubs


def analyze_ucsc(df):
    ucsc_cyclists = df[df['club_clean'] == 'UCSC']
    best_time = ucsc_cyclists['time'].min()
    best_cyclist = ucsc_cyclists[ucsc_cyclists['time'] == best_time]
    total_cyclists = len(df)
    best_position = df['time'].sort_values().reset_index(drop=True).tolist().index(best_time) + 1
    percentage = (best_position / total_cyclists) * 100
    return ucsc_cyclists, best_cyclist, best_position, percentage


def main():
    filepath = "data/dataset.csv"
    df = None

    while True:
        print("\nSeleccione una opción:")
        print("1. Importar dataset")
        print("2. Mostrar los 5 primeros registros")
        print("3. Contar ciclistas participantes")
        print("4. Mostrar columnas del dataset")
        print("5. Anonimizar nombres de los ciclistas")
        print("6. Eliminar ciclistas no participantes")
        print("7. Recuperar datos del ciclista con dorsal=1000")
        print("8. Agrupar tiempos en franjas de 20 minutos y generar histograma")
        print("9. Limpiar nombres de clubes")
        print("10. Analizar datos del club UCSC")
        print("0. Salir")

        opcion = input("Introduce el número de la opción: ")

        if opcion == "1":
            print("Cargando datos de Orbea Monegros 2024...")
            df = importar_dataset(filepath)
            print("Dataset cargado correctamente.")

        elif opcion == "2" and df is not None:
            print("Mostrando los 5 primeros registros:")
            print(mostrar_5_primeros(df))

        elif opcion == "3" and df is not None:
            print(f"Número de ciclistas participantes: {contar_ciclistas(df)}")

        elif opcion == "4" and df is not None:
            print("Columnas del dataset:")
            print(obtener_columnas(df))

        elif opcion == "5" and df is not None:
            print("Anonimizando nombres de los ciclistas...")
            df = name_surname(df)
            print("Primeros 5 valores después de anonimizar:")
            print(mostrar_5_primeros(df))

        elif opcion == "6" and df is not None:
            print("Eliminando ciclistas no participantes...")
            df = remove_non_participants(df)
            print(f"Ciclistas restantes después de la limpieza: {contar_ciclistas(df)}")

        elif opcion == "7" and df is not None:
            print("Recuperando datos del ciclista con dorsal=1000...")
            cyclist = get_cyclist_by_dorsal(df, 1000)
            print(cyclist)

        elif opcion == "8" and df is not None:
            print("Agrupando tiempos en franjas de 20 minutos y generando histograma...")
            grouped = group_and_plot_histogram(df)
            print(grouped)

        elif opcion == "9" and df is not None:
            print("Limpiando nombres de clubes...")
            grouped_clubs = process_clubs(df)
            print("15 primeros valores de los clubes limpios:")
            print(grouped_clubs.head(15))

        elif opcion == "10" and df is not None:
            print("Analizando datos del club UCSC...")
            ucsc_cyclists, best_cyclist, best_position, percentage = analyze_ucsc(df)
            print("Ciclistas de UCSC:")
            print(ucsc_cyclists)
            print("Mejor ciclista de UCSC:")
            print(best_cyclist)
            print(f"Posición: {best_position}, Porcentaje: {percentage:.2f}%")

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print(opcion)
            print("Por favor, selecciona una opción válida o asegúrate de haber importado el dataset.")


if __name__ == "__main__":
    main()