import pandas as pd
import re


def clean_club(club):
    """
    Limpia el nombre de un club ciclista según reglas predefinidas.
    Args:
        club (str): Nombre del club.
    Returns:
        str: Nombre del club limpio.
    """
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
    """
    Crea una nueva columna 'club_clean' con los nombres de los clubs limpios.
    Args:
        df (pd.DataFrame): DataFrame con la columna 'club'.
    Returns:
        pd.DataFrame: DataFrame con la nueva columna 'club_clean'.
    """
    df['club_clean'] = df['club'].apply(clean_club)
    grouped_clubs = df.groupby('club_clean').size().reset_index(name='count').sort_values(by='count', ascending=False)
    return grouped_clubs


def analyze_ucsc(df):
    """
    Analiza los datos del club UCSC (Unió Ciclista Sant Cugat).
    Args:
        df (pd.DataFrame): DataFrame con la columna 'club_clean'.
    Returns:
        tuple: Ciclistas de UCSC, mejor ciclista, posición del mejor ciclista, porcentaje sobre el total.
    """
    ucsc_cyclists = df[df['club_clean'] == 'UCSC']
    best_time = ucsc_cyclists['time'].min()
    best_cyclist = ucsc_cyclists[ucsc_cyclists['time'] == best_time]
    total_cyclists = len(df)
    best_position = df['time'].sort_values().reset_index(drop=True).tolist().index(best_time) + 1
    percentage = (best_position / total_cyclists) * 100
    return ucsc_cyclists, best_cyclist, best_position, percentage