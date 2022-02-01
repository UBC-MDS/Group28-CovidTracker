from covid_tracker.calculate_stat_summary import calculate_stat_summary
from covid_tracker.get_covid_data import get_covid_data
import pandas as pd
import pytest


def test_calculate_stat_summary():
    """Test the calculate_stat_summary() function"""

    # data_type='cases'
    input = get_covid_data()
   
    # Test output type
    assert isinstance(calculate_stat_summary(input, 'cases'), pd.DataFrame)
    
    # Test output size
    assert calculate_stat_summary(input, 'cases').shape == (14, 12)

    # Test output column names
    assert 'date_report' in calculate_stat_summary(input, 'cases').columns
    assert 'province' in calculate_stat_summary(input, 'cases').columns
    assert 'cases' in calculate_stat_summary(input, 'cases').columns

    # data_type='mortality'
    input = get_covid_data(data_type='mortality')
    
    # Test output type
    assert isinstance(calculate_stat_summary(input, 'deaths'), pd.DataFrame)
    
    # Test output size
    assert calculate_stat_summary(input, 'deaths').shape == (14, 12)

    # Test output column names
    assert 'date_death_report' in calculate_stat_summary(input, 'deaths').columns
    assert 'province' in calculate_stat_summary(input, 'deaths').columns
    assert 'deaths' in calculate_stat_summary(input, 'deaths').columns

def test_calculate_stat_summary_errors():
    """Test that calculate_stat_summary() raises the correct errors"""

    input = get_covid_data()
    # Tests that TypeErrors are raised when arguments are not the right type
    with pytest.raises(TypeError):
        calculate_stat_summary('2021-12-31', 'cases')
        calculate_stat_summary(100, 'death')
        calculate_stat_summary(input, 2)
        calculate_stat_summary(input, 'province')

    # Tests that ValueErrors are raised when arguments are value
    with pytest.raises(ValueError):
        calculate_stat_summary(pd.DataFrame(columns=["a", "b"]), 'cases')
        calculate_stat_summary(pd.DataFrame({"a": [1], "b":[2]}), 'deaths')
        calculate_stat_summary(pd.DataFrame(input, 'new'))
        calculate_stat_summary(pd.DataFrame({"a": [1], "b":[2]}), 'a')