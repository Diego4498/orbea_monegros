
import pytest
import pandas as pd
from orbea_package.grouping import minutes_002040, group_and_plot_histogram

@pytest.fixture
def sample_dataframe():
    data = {
        "time": ["01:15:00", "01:35:00", "02:50:00", "03:10:00"]
    }
    return pd.DataFrame(data)

def test_minutes_002040():
    assert minutes_002040("01:15:00") == "01:00"
    assert minutes_002040("01:35:00") == "01:20"
    assert minutes_002040("02:50:00") == "02:40"
    assert minutes_002040("03:10:00") == "03:00"

def test_group_and_plot_histogram(sample_dataframe):
    grouped = group_and_plot_histogram(sample_dataframe)
    assert "time_grouped" in grouped.columns
    assert "count" in grouped.columns
    assert len(grouped) > 0
