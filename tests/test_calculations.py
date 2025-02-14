import pytest
import pandas as pd
import numpy as np
from src.calculations import time_lag_analysis, flux_pde_const_D

@pytest.fixture
def sample_steady_state_data():
    t = np.linspace(0, 1000, 1001)
    # Create data that follows y = mx + c
    m = 1e-6  # slope
    c = -5e-3  # intercept
    cumulative_flux = m * t + c + np.random.normal(0, 1e-7, len(t))
    
    return pd.DataFrame({
        't / s': t,
        'cumulative flux / cm^3(STP) cm^-2': cumulative_flux,
        'P_cell / bar': np.ones_like(t) * 50,
        'flux / cm^3(STP) cm^-2 s^-1': np.ones_like(t) * m
    })

def test_time_lag_analysis(sample_steady_state_data):
    stabilisation_time = 500  # seconds
    thickness = 0.1  # cm
    
    result = time_lag_analysis(
        sample_steady_state_data, 
        stabilisation_time, 
        thickness
    )
    
    time_lag, D, P, S, pressure, solubility, slope, intercept = result
    
    assert isinstance(time_lag, float)
    assert isinstance(D, float)
    assert isinstance(P, float)
    assert isinstance(S, float)
    assert isinstance(pressure, float)
    assert isinstance(solubility, float)
    assert isinstance(slope, float)
    assert isinstance(intercept, float)
    
    assert time_lag > 0
    assert D > 0
    assert P > 0
    assert S > 0
    assert pressure > 0
    assert solubility > 0

def test_flux_pde_const_D():
    D = 1e-7  # cm^2/s
    C_eq = 1.0  # cm^3(STP)/cm^3
    L = 0.1  # cm
    T = 1000  # s
    dt = 1  # s
    dx = L/50  # cm
    
    C_profile, flux, df_C, df_flux = flux_pde_const_D(D, C_eq, L, T, dt, dx)
    
    assert isinstance(C_profile, np.ndarray)
    assert isinstance(flux, list)
    assert isinstance(df_C, pd.DataFrame)
    assert isinstance(df_flux, pd.DataFrame)
    
    assert C_profile.shape[1] == 51  # Number of spatial points (L/dx + 1)
    assert len(flux) == 1001  # Number of time points (T/dt + 1)
    
    # Check boundary conditions
    assert np.allclose(C_profile[:, 0], C_eq)  # x = 0
    assert np.allclose(C_profile[:, -1], 0)    # x = L
    
    # Check initial condition
    assert np.allclose(C_profile[0, 1:], 0)    # t = 0, x > 0

def test_flux_pde_const_D_stability():
    D = 1e-7  # cm^2/s
    C_eq = 1.0  # cm^3(STP)/cm^3
    L = 0.1  # cm
    T = 1000  # s
    dt = 10  # s (violates stability condition)
    dx = L/50  # cm
    
    # Should raise assertion error due to stability condition violation
    with pytest.raises(AssertionError):
        flux_pde_const_D(D, C_eq, L, T, dt, dx)
