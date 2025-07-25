"""
Neuro Analyst OS - An open-source EEG analysis operating system.

This package provides tools for EEG data processing, analysis, and visualization,
designed to democratize neuroscience research and brain-computer interface development.
"""

__version__ = "0.1.0"
__author__ = "Neuro Analyst OS Team"

# Import main modules for easy access
from .clean import clean_eeg_data

__all__ = ["clean_eeg_data"]
