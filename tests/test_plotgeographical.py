from covid_tracker.plot_geographical import plot_geographical
from covid_tracker.get_covid_data import get_covid_data 
from pytest import raises
import pandas as pd
import matplotlib as plt

# import importlib.resources as pkg_resources
# from . import shape_files 

def test_plot_geographical():
    """
    Tests the plot_geographical function to make sure the outputs are correct.
    
    Returns
    -------
    None
        The test should pass and no asserts should be displayed.
    """
    #Calling helper function to create data
    covid_df = get_covid_data()
    covid_df_test = get_covid_data('testing')
    
    # Test that Exceptions are correctly raised when the type of
    # arguments are wrong
    with raises(Exception) as e:
        plot_geographical('', 'cases')
    assert str(e.value) == "The value of the argument 'covid_df' " \
                           "must be of type dataframe."

    with raises(Exception) as e:
        plot_geographical(covid_df, 3 )
    assert str(e.value) == "The value of the argument 'metric' must be " \
                           "of type string"
    
    # Test that ValueErrors are correctly raised when the value of
    # arguments are wrong
    with raises(ValueError) as e:
        plot_geographical(covid_df, 'deaths')
    assert str(e.value) == f"Chosen metric must be a column in the dataframe."\
                            f"\nPlease choose one from: {list(covid_df.columns)}"
    
    with raises(ValueError) as e:
        plot_geographical(covid_df, 'province')
    assert str(e.value) == "Chosen metric must not be date or province column."


    with raises(ValueError) as e:
        plot_geographical(covid_df_test, 'testing_info')
    assert str(e.value) == "Please choose a different metric with non null values."

    
    # Test the plot attributes
    plot = plot_geographical(covid_df,'cases')
    plot_cm =plot_geographical(covid_df,'cumulative_cases')
    
    assert isinstance(plot, plt.figure.Figure)
    assert isinstance(plot_cm, plt.figure.Figure)
    assert hasattr(plot,"colorbar")
    assert hasattr(plot_cm,"colorbar")
    assert hasattr(plot,"axes")
    assert hasattr(plot_cm,"axes")
    
