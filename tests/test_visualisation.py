import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.visualisation import plot_time_lag_analysis, plot_concentration_location_profile, plot_flux_over_time, plot_concentration_profile

class TestVisualisation(unittest.TestCase):

    def setUp(self):
        # Create sample data for testing
        self.df = pd.DataFrame({
            't / s': np.linspace(0, 1000, 100),
            'cumulative flux / cm^3(STP) cm^-2': np.cumsum(np.random.rand(100)),
            'flux / cm^3(STP) cm^-2 s^-1': np.random.rand(100)
        })
        self.C_profile = np.random.rand(100, 50)
        self.L = 0.1
        self.T = 1000
        self.flux = np.random.rand(100)
        self.stabilisation_time_s = 200
        self.slope = 0.01
        self.intercept = 0.5

    def test_plot_time_lag_analysis(self):
        plot_time_lag_analysis(self.df, self.stabilisation_time_s, self.slope, self.intercept)
        plt.close()

    def test_plot_concentration_location_profile(self):
        plot_concentration_location_profile(self.C_profile, self.L, self.T)
        plt.close()

    def test_plot_flux_over_time(self):
        plot_flux_over_time(self.flux, self.df, self.T)
        plt.close()

    def test_plot_concentration_profile(self):
        plot_concentration_profile(self.C_profile, self.L, self.T)
        plt.close()

if __name__ == '__main__':
    unittest.main()
