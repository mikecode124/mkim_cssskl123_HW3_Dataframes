# =============================================================================
# Project:      HW3 - SERIES & DATAFRAMES
# Student:      Michael Kim
# Class:        CSSSKL 123
# Section:      A, Spring 2024
#
#
# In this assignment, we are tasked with reading from a .data file and
# utilizing/manipulating the dataset within. The dataset will represent
# different configurations of flags, in terms of boolean or int values.
# Ultimately, we will be expected to display the resulting data via
# console print, which should match a sample.
#
# **Comments that specify each numbered task are in, "--> Main:", which begins
# after the Import and Methods sections below**
# =============================================================================

# --> Import module:

import numpy as np
import data
import pandas as pd

# --> Methods:

def percent_of_mean(one_d):
    ''
    # sample
    mean_array = np.where(as_array > 0, (as_array / mean) * 100, error_fill)

    return mean_array

# --> Main:

# -----------------------------------------------------------------------------
# Task #1:
# - Loops restricted / List comprehension structures restricted
# - Write 'percent_of_mean()'
#   - Input is a 1-D array of numeric values
#       - values represent the stock index for each day as a % of the
#         mean value over the period covered by the list
#   - Find mean of all values
#   - Store representation of each value as a % of the mean
# -----------------------------------------------------------------------------