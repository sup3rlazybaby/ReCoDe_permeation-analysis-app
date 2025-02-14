import unittest
import matplotlib.pyplot as plt

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.util import set_plot_style, update_ticks

class TestUtil(unittest.TestCase):

    def test_set_plot_style(self):
        set_plot_style()
        self.assertEqual(plt.rcParams['font.size'], 10)
        self.assertEqual(plt.rcParams['font.family'], 'sans-serif')

    def test_update_ticks(self):
        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1])
        x_lim, y_lim = update_ticks(ax, x_lo=0, y_lo=0)
        self.assertEqual(x_lim[0], 0)
        self.assertEqual(y_lim[0], 0)
        plt.close()

if __name__ == '__main__':
    unittest.main()
