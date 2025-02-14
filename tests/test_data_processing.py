import unittest
import pandas as pd
from src.data_processing import load_data, preprocess_data

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        # self.file_path_csv = 'path/to/sample_data.csv'
        self.file_path_excel = 'data/RUN_H_25C-50bar.xlsx'
        self.d_cm = 0.1
        self.qN2_mlmin = 8.0

    # def test_load_data_csv(self):
    #     df = load_data(self.file_path_csv)
    #     self.assertIsInstance(df, pd.DataFrame)

    def test_load_data_excel(self):
        df = load_data(self.file_path_excel)
        self.assertIsInstance(df, pd.DataFrame)

    def test_preprocess_data(self):
        df = pd.DataFrame({
            't / s': [0, 1, 2, 3, 4],
            'y_CO2 / ppm': [400, 410, 420, 430, 440],
            'P_cell / barg': [1, 1, 1, 1, 1],
            'T / °C': [25, 25, 25, 25, 25]
        })
        preprocessed_df = preprocess_data(df, self.d_cm, self.qN2_mlmin)
        self.assertIn('flux / cm^3(STP) cm^-2 s^-1', preprocessed_df.columns)
        self.assertIn('cumulative flux / cm^3(STP) cm^-2', preprocessed_df.columns)

if __name__ == '__main__':
    unittest.main()
