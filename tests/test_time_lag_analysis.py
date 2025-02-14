import unittest
import os
from src.time_lag_analysis import time_lag_analysis_workflow

class TestTimeLagAnalysis(unittest.TestCase):

    def setUp(self):
        self.datapath = 'data/RUN_H_25C-50bar.xlsx'
        self.L_cm = 0.1
        self.d_cm = 1.0
        self.qN2_mlmin = 8.0
        self.stablisation_time_range = (None, None)
        self.display_plot = True
        self.save_plot = False
        self.save_data = False
        self.output_dir = '.'

    def test_time_lag_analysis_workflow(self):
        results = time_lag_analysis_workflow(
            self.datapath, self.L_cm, self.d_cm, self.qN2_mlmin,
            self.stablisation_time_range, self.display_plot, self.save_plot,
            self.save_data, self.output_dir
        )
        self.assertIn('time_lag', results)
        self.assertIn('diffusion_coefficient', results)
        self.assertIn('permeability', results)
        self.assertIn('solubility_coefficient', results)
        self.assertIn('slope', results)
        self.assertIn('intercept', results)

if __name__ == '__main__':
    unittest.main()
