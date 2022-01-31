from covidtracker.get_covid_data import get_covid_data 
import pandas as pd
import pytest


def test_get_covid_data():
    """Test the get_covid_data() function"""

    # Tests that the function returns the correct data for given arguments
    test_df = pd.DataFrame({'cases': [698], 'cumulative_cases': [161969], 'date_report': ['25-08-2021'], 'province': ['BC']})
    assert get_covid_data('cases', 'BC', date = '25-08-2021').equals(test_df)

    # Tests that the function returns a DataFrame of correct size 
    assert isinstance(get_covid_data(), pd.DataFrame)
    assert get_covid_data('cases', date = '22-11-2021').shape == (14, 4)


def test_get_covid_data_errors():
    """Test that get_covid_data() raises the correct errors"""

    # Tests that ValueErrors are raised when arguments are of right type but inappropriate value
    with pytest.raises(ValueError):
        get_covid_data(date = '33-22-1997')
        get_covid_data('deaths')
        get_covid_data(loc = "HK")