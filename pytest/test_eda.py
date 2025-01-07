
import pytest
import pandas as pd
from orbea_package.eda import (
    importar_dataset,
    mostrar_5_primeros,
    contar_ciclistas,
    obtener_columnas,
    name_surname,
    remove_non_participants,
    get_cyclist_by_dorsal
)

@pytest.fixture
def sample_dataframe():
    data = {
        "dorsal": [1, 2, 3, 4],
        "biker": ["Ciclista 1", "Ciclista 2", "Ciclista 3", "Ciclista 4"],
        "club": ["Club A", "Club B", "Independiente", "Club C"],
        "time": ["01:20:00", "00:00:00", "02:30:00", "00:00:00"]
    }
    return pd.DataFrame(data)

def test_importar_dataset():
    df = importar_dataset("/mnt/data/dataset.csv")
    assert isinstance(df, pd.DataFrame)
    assert df.shape[1] == 4  # Asegurarse de que tiene 4 columnas

def test_mostrar_5_primeros(sample_dataframe):
    result = mostrar_5_primeros(sample_dataframe)
    assert len(result) <= 5
    assert result.iloc[0]["biker"] == "Ciclista 1"

def test_contar_ciclistas(sample_dataframe):
    assert contar_ciclistas(sample_dataframe) == 4

def test_obtener_columnas(sample_dataframe):
    expected_columns = ["dorsal", "biker", "club", "time"]
    assert obtener_columnas(sample_dataframe) == expected_columns

def test_name_surname(sample_dataframe):
    df = name_surname(sample_dataframe)
    assert not df['biker'].isin(["Ciclista 1", "Ciclista 2", "Ciclista 3", "Ciclista 4"]).any()

def test_remove_non_participants(sample_dataframe):
    df = remove_non_participants(sample_dataframe)
    assert len(df) == 2  # Solo dos ciclistas tienen tiempos válidos
    assert "00:00:00" not in df["time"].values

def test_get_cyclist_by_dorsal(sample_dataframe):
    cyclist = get_cyclist_by_dorsal(sample_dataframe, 2)
    assert cyclist.iloc[0]['biker'] == "Ciclista 2"
    assert cyclist.iloc[0]['club'] == "Club B"
