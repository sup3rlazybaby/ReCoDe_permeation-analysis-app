import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.visualisation import plot_time_lag_analysis, plot_flux_over_time, plot_concentration_location_profile, plot_concentration_profile

@pytest.fixture
def sample_data():
    t = np.linspace(0, 1000, 1001)
    cumulative_flux = 1e-6 * t - 5e-3 + np.random.normal(0, 1e-7, len(t))
    flux = np.ones_like(t) * 1e-6
    
    return pd.DataFrame({
        't / s': t,
        'cumulative flux / cm^3(STP) cm^-2': cumulative_flux,
        'flux / cm^3(STP) cm^-2 s^-1': flux
    })

@pytest.fixture
def concentration_profile():
    x_points = 51
    t_points = 1001
    C = np.zeros((t_points, x_points))
    C[:, 0] = 1.0  # Boundary condition at x = 0
    return C

def test_plot_time_lag_analysis(sample_data):
    fig, ax = plt.subplots()
    plot_time_lag_analysis(sample_data, 500, 1e-6, -5e-3, fig, ax)
    assert len(ax.lines) == 3  # Data line, steady-state fit, extrapolated fit
    plt.close(fig)

def test_plot_flux_over_time(sample_data):
    fig, ax = plt.subplots()
    flux = np.ones(1001) * 1e-6
    plot_flux_over_time(flux, sample_data, 1000, fig, ax)
    assert len(ax.lines) == 2  # Model line and measurement line
    plt.close(fig)

def test_plot_concentration_location_profile(concentration_profile):
    fig, ax = plt.subplots()
    plot_concentration_location_profile(concentration_profile, 0.1, 1000, fig, ax)
    assert len(ax.lines) == 6  # One line for each time point
    plt.close(fig)

def test_plot_concentration_profile(concentration_profile):
    fig, ax = plt.subplots()
    plot_concentration_profile(concentration_profile, 0.1, 1000, fig, ax)
    assert len(ax.images) == 1  # One imshow plot
    plt.close(fig)
