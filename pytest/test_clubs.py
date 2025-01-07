
import pytest
import pandas as pd
from orbea_package.clubs import clean_club, process_clubs, analyze_ucsc

@pytest.fixture
def sample_dataframe():
    data = {
        "club": ["C.C. Huesca", "Club Ciclista Sari\u00f1ena", "UCSC", "C.C. Oscense"],
        "time": ["01:30:00", "02:00:00", "00:45:00", "03:15:00"],
        "club_clean": ["Huesca", "Sari\u00f1ena", "UCSC", "Oscense"]
    }
    return pd.DataFrame(data)

def test_clean_club():
    assert clean_club("C.C. Huesca") == "HUESCA"
    assert clean_club("Club Ciclista Sari\u00f1ena") == "SARI\u00d1ENA"
    assert clean_club("UCSC") == "UCSC"

def test_process_clubs(sample_dataframe):
    df = sample_dataframe.drop(columns=["club_clean"])
    grouped_clubs = process_clubs(df)
    assert "club_clean" in grouped_clubs.columns
    assert "count" in grouped_clubs.columns
    assert grouped_clubs.loc[grouped_clubs["club_clean"] == "UCSC", "count"].iloc[0] == 1

def test_analyze_ucsc(sample_dataframe):
    ucsc_cyclists, best_cyclist, best_position, percentage = analyze_ucsc(sample_dataframe)
    assert len(ucsc_cyclists) == 1  # Solo un ciclista de UCSC
    assert best_cyclist.iloc[0]['time'] == "00:45:00"
    assert best_position == 1
    assert percentage > 0
