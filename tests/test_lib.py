from mylib.lib import (
    read_dataset,
    general_summary,
    plot_histogram,
    plot_boxplot,
    plot_crosstab,
    plot_count,
    plot_income,
    plot_age,
    plot_miles,
    plot_corr,
    plot_scatter
)

import pytest
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

@pytest.fixture
def test_mock():
    data = {
        'Product': ['TM195', 'TM195', 'TM195', 'TM498', 'TM498', 'TM798', 'TM798', 'TM798'],
        'Age': [18, 19, 19, 19, 20, 20, 21, 21],
        'Gender': ['Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
        'Education': [14, 15, 14, 12, 13, 14, 14, 13],
        'MaritalStatus': ['Single', 'Single', 'Partnered', 'Single', 'Partnered', 'Partnered', 'Partnered', 'Single'],
        'Usage': [3, 2, 4, 3, 4, 3, 3, 3],
        'Fitness': [4, 3, 3, 3, 2, 3, 3, 3],
        'Income': [29562, 31836, 30699, 32973, 35247, 32973, 35247, 32973],
        'Miles': [112, 75, 66, 85, 47, 66, 75, 85]
    }
    df = pd.DataFrame(data)
    return df

def test_read_dataset():
    path = "/workspaces/IDS706_w3_Individual_Project1/data/CardioGoodFitness.csv"
    df = read_dataset(path)
    assert(len(df) > 0)

def test_general_summary(test_mock, mocker):
    mock_print = mocker.patch("tests.test_lib.general_summary")
    general_summary(test_mock)
    mock_print.assert_called_once_with(test_mock)

def test_plot_histogram(test_mock, mocker):
    mock_hist = mocker.patch("tests.test_lib.plot_histogram")
    plot_histogram(test_mock)
    plot_histogram(test_mock, flag = True)
    assert mock_hist.call_count == 2
    mock_hist.assert_has_calls([
        mocker.call(test_mock),
        mocker.call(test_mock, flag=True)
    ])

def test_plot_boxplot(test_mock, mocker):
    mock_boxplot = mocker.patch("tests.test_lib.plot_boxplot")
    plot_boxplot(test_mock)
    plot_boxplot(test_mock, flag = True)
    assert mock_boxplot.call_count == 2
    mock_boxplot.assert_has_calls([
        mocker.call(test_mock),
        mocker.call(test_mock, flag=True)
    ])

def test_plot_crosstab(test_mock, mocker):
    mock_crosstab = mocker.patch("tests.test_lib.plot_crosstab")
    plot_crosstab(test_mock)
    mock_crosstab.assert_called_once_with(test_mock)
    

def test_plot_count(test_mock, mocker):
    mock_count = mocker.patch("tests.test_lib.plot_count")
    plot_count(test_mock)
    plot_count(test_mock, flag = True)
    assert mock_count.call_count == 2
    mock_count.assert_has_calls([
        mocker.call(test_mock),
        mocker.call(test_mock, flag=True)
    ])

def test_plot_income(test_mock, mocker):
    mock_income = mocker.patch("tests.test_lib.plot_income")
    plot_income(test_mock)
    plot_income(test_mock, flag = True)
    assert mock_income.call_count == 2
    mock_income.assert_has_calls([
        mocker.call(test_mock),
        mocker.call(test_mock, flag=True)
    ])

def test_plot_age(test_mock, mocker):
    mock_age = mocker.patch("tests.test_lib.plot_age")
    plot_age(test_mock)
    plot_age(test_mock, flag = True)
    assert mock_age.call_count == 2
    mock_age.assert_has_calls([
        mocker.call(test_mock),
        mocker.call(test_mock, flag=True)
    ])

def test_plot_miles(test_mock, mocker):
    mock_miles = mocker.patch("tests.test_lib.plot_miles")
    plot_miles(test_mock)
    mock_miles.assert_called_once_with(test_mock)
    

def test_plot_corr(test_mock, mocker):
    mock_corr = mocker.patch("tests.test_lib.plot_corr")
    plot_corr(test_mock)
    mock_corr.assert_called_once_with(test_mock)

def test_plot_scatter(test_mock, mocker):
    mock_scatter = mocker.patch("tests.test_lib.plot_scatter")
    plot_scatter(test_mock)
    mock_scatter.assert_called_once_with(test_mock)
    

# if __name__ == "__main__":
#     path = "/workspaces/IDS706_w3_Individual_Project1/data/CardioGoodFitness.csv"
#     test_read_dataset(path)
#     print("Everything passed")
