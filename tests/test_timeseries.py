from CovidTracker.get_covid_data import get_covid_data
from CovidTracker.plot_time_series import plot_ts
from pytest import raises
import pandas as pd
import matplotlib as plt
import pytest


def test_plot_ts():
    """
    Tests if the plot_time_series function gives the corret output.
    
    Returns
    -------
    None
        The test should pass and no asserts should be displayed.
    """
    # Generate test data
    df = get_covid_data("testing")
    test_plot = plot_ts(df, "testing", start = '2020-03-17', end = '2020-04-17')
    
    assert test_plot.encoding.x.field == 'date_testing', 'x_axis is not mapped correctly'
    assert test_plot.encoding.y.field == 'testing', 'y_axis is not mapped correctly'
    assert test_plot.mark == 'line', 'mark should be a line'
    assert test_plot.encoding.x.type == 'temporal', "x-axis has wrong data type"
    
    
def test_plot_ts():
    """
    Tests if the plot_time_series function raises errors correctly
    
    Returns
    -------
    None
        The test should pass and no asserts should be displayed.
    """
    with pytest.raises(ValueError):
        plot_ts(df = df, metric = 10)
        plot_ts(df = [1, 2, 3], "testing")
        plot_ts(start = '20-12-10')
        plot_ts(start = '1900-12-10')
        
        