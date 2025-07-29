# **Neuro-Analyst OS**

An open-source Python toolkit to make brain data analysis simple, beautiful, and reproducible for everyone.

## **Overview & Philosophy**

Neuroscience is drowning in data but starving for insight. Researchers spend up to **80% of their time on "data janitor" work**—loading complex files, cleaning noisy signals, and wrestling with plotting libraries. This slows down the pace of discovery.

Our philosophy is simple: **a scientist's time is better spent on asking big questions, not on data wrangling.**

Neuro-Analyst OS is an **opinionated** toolkit that automates the most common and frustrating parts of EEG/BCI analysis. It provides a clean, elegant, high-level API that handles the messy details for you, letting you get from raw data to clean insight in seconds, not weeks.

-----

## **Installation**

Get the latest stable release from PyPI:

```bash
pip install neuro-analyst-os
```

-----

## **Quick Start: The 5-Minute Analysis**

Here’s how to load a raw EEG file, apply a best-practice cleaning pipeline, and generate a publication-quality visualization in just three lines of code.

```python
import neuro_analyst_os as na

# 1. Load the raw, noisy data from any common format
raw_data = na.load('path/to/your_experiment_data.edf')

# 2. Automatically clean the data using our smart, opinionated pipeline
cleaned_data = na.clean(raw_data)

# 3. Visualize the power spectral density across the scalp
na.plot(cleaned_data, plot_type='psd_topomap')
```

This simple workflow is the core of Neuro-Analyst OS.

-----

## **API Reference**

This section details the core functions of the v0.1 library.

### `na.load()`

Loads brain signal data from a specified file path into a Neuro-Analyst data object. It automatically detects the file type and handles the parsing in the background.

  * **Parameters:**
      * `filepath` (str): The path to the data file. Supported formats: `.edf`, `.bdf`, `.gdf`, OpenBCI `.txt`.
  * **Returns:**
      * A `Raw` data object ready for analysis.

### `na.clean()`

Applies a pre-configured, best-practice cleaning pipeline to a `Raw` data object. This is the "magic" of the library.

The default pipeline includes:

1.  Bandpass filtering (1-50 Hz).
2.  A notch filter for electrical grid noise (50 Hz or 60 Hz).
3.  Automated artifact rejection using ICA to remove signals from eye blinks and muscle movements.

<!-- end list -->

  * **Parameters:**
      * `raw_data` (Raw): The data object returned by `na.load()`.
      * `artifacts` (list, optional): A list of specific artifact types to target. Defaults to `['blinks', 'muscle']`.
  * **Returns:**
      * A `Cleaned` data object.

### `na.plot()`

Creates a high-quality, publication-ready visualization of your data.

  * **Parameters:**
      * `data` (Raw or Cleaned): The data object you want to visualize.
      * `plot_type` (str): The type of plot to generate. Options include:
          * `'raw'`: A simple plot of the signal over time.
          * `'psd_topomap'`: A topographical map of power spectral density across the scalp.
          * `'psd'`: A standard power spectral density plot per channel.
  * **Returns:**
      * A Matplotlib figure object for further customization or saving.

-----

## **Contributing**

This project is built for the community. If you find a bug or have an idea for a new feature, please check our **GitHub Issues** page to see if it's already being discussed. We welcome all contributions\!

-----

## **Citation**

If you use Neuro-Analyst OS in your academic research, please cite it as follows:

> Raval, S. (2025). Neuro-Analyst OS: A Python toolkit for simplified EEG analysis (Version 0.1). GitHub. [https://github.com/sirajraval/neuro-analyst-os](https://www.google.com/search?q=https://github.com/sirajraval/neuro-analyst-os)
