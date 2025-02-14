import unittest
import sys
import pandas as pd
import numpy as np
# Append the path of the src directory to sys.path
sys.path.append('../')

from ..src.calculations import time_lag_analysis, flux_pde_const_D

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            't / s': np.linspace(0, 1000, 100),
            'cumulative flux / cm^3(STP) cm^-2': np.cumsum(np.random.rand(100)),
            'P_cell / bar': np.random.rand(100) + 1
        })
        self.stabilisation_time_s = 200
        self.thickness = 0.1
        self.D = 1e-5
        self.C_eq = 1.0
        self.L = 0.1
        self.T = 1000
        self.dt = 1
        self.dx = 0.01

    def test_time_lag_analysis(self):
        results = time_lag_analysis(self.df, self.stabilisation_time_s, self.thickness)
        self.assertEqual(len(results), 8)
        self.assertIsInstance(results, tuple)

    def test_flux_pde_const_D(self):
        C_profile, flux, df_C, df_flux = flux_pde_const_D(self.D, self.C_eq, self.L, self.T, self.dt, self.dx)
        self.assertEqual(C_profile.shape, (int(self.T / self.dt) + 1, int(self.L / self.dx) + 1))
        self.assertEqual(len(flux), int(self.T / self.dt) + 1)
        self.assertIsInstance(df_C, pd.DataFrame)
        self.assertIsInstance(df_flux, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
