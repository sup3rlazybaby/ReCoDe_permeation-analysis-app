# Time Lag Analysis Application

This application provides a graphical user interface (GUI) for performing time lag analysis on gas permeation data. It allows users to load data from Excel files, specify experimental parameters, run the analysis, and visualize the results.

## Features

-   **Data Input**: Load gas permeation data from `.xlsx` files.
-   **Parameter Setting**: Set experimental parameters such as diameter, thickness, and flow rate.
-   **Stabilisation Time**: Option to auto-detect stabilization time or manually set a custom range.
-   **Analysis Execution**: Run time lag analysis with specified parameters.
-   **Result Display**: Display calculated parameters such as time lag, diffusion coefficient, permeability, and solubility coefficient.
-   **Visualization**: Generate and display plots of the analysis results, including time lag analysis, flux over time, and concentration profiles.
-   **Plot Saving**: Save generated plots in `.png` or `.svg` formats.
-   **UI Scaling**: Adjust the scaling of the user interface.
-   **Plot Label Scaling**: Adjust the size of plot labels for better readability.

## Getting Started

### Prerequisites

- Anaconda or Miniconda installed on your system
- Git (optional, for cloning the repository)

### Installation

1. Clone or download the repository:
```bash
git clone [repository URL]
cd [project directory]
```

2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate time-lag-analysis
```

3. Run the application:
```bash
python src/app.py
```