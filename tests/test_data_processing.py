import pytest
import pandas as pd
import numpy as np
from src.data_processing import load_data, correct_baseline, calculate_pressure, calculate_flux, calculate_cumulative_flux, identify_stabilisation_time, preprocess_data

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        't / s': np.linspace(0, 100, 101),
        'y_CO2 / ppm': np.random.normal(100, 10, 101),
        'P_cell / barg': np.ones(101) * 50,
        'T / °C': np.ones(101) * 25,
        'qN2 / ml min^-1': np.ones(101) * 8.0
    })

def test_correct_baseline(sample_data):
    result = correct_baseline(sample_data, baseline=50)
    assert isinstance(result, pd.Series)
    assert len(result) == len(sample_data)
    assert all(result == sample_data['y_CO2 / ppm'] - 50)

def test_calculate_pressure(sample_data):
    result = calculate_pressure(sample_data)
    assert isinstance(result, pd.Series)
    assert len(result) == len(sample_data)
    assert all(abs(result - (sample_data['P_cell / barg'] + 1.01325)) < 1e-10)

def test_calculate_flux(sample_data):
    result = calculate_flux(sample_data, d_cm=1.0, qN2_mlmin=8.0)
    assert isinstance(result, pd.Series)
    assert len(result) == len(sample_data)
    assert all(result >= 0)  # Flux should be positive

def test_calculate_cumulative_flux(sample_data):
    sample_data['flux / cm^3(STP) cm^-2 s^-1'] = calculate_flux(sample_data, d_cm=1.0)
    result = calculate_cumulative_flux(sample_data)
    assert isinstance(result, pd.Series)
    assert len(result) == len(sample_data)
    assert result.is_monotonic_increasing  # Cumulative flux should be monotonically increasing

def test_identify_stabilisation_time(sample_data):
    # Create sample data with known stabilisation point
    t = np.linspace(0, 100, 101)
    y = np.where(t < 50, t**2, 50*t)
    df = pd.DataFrame({
        't / s': t,
        'cumulative flux / cm^3(STP) cm^-2': y
    })
    
    result = identify_stabilisation_time(df, column='cumulative flux / cm^3(STP) cm^-2')
    assert isinstance(result, float)
    assert result > 0
    assert result < df['t / s'].max()

def test_preprocess_data(sample_data):
    result = preprocess_data(sample_data, d_cm=1.0, qN2_mlmin=8.0)
    required_columns = [
        't / s', 
        'P_cell / bar', 
        'T / °C', 
        'y_CO2 / ppm', 
        'y_CO2_bl / ppm',
        'flux / cm^3(STP) cm^-2 s^-1', 
        'cumulative flux / cm^3(STP) cm^-2'
    ]
    
    assert isinstance(result, pd.DataFrame)
    assert all(col in result.columns for col in required_columns)
    assert len(result) == len(sample_data)
