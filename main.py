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
import pandas as pd

# --> Methods:

def percent_of_mean(one_d):
    ''
    # sample
    mean_array = np.where(as_array > 0, (as_array / mean) * 100, error_fill)

    return mean_array

# --> Main:

with open("flag.data", "r") as flagfile:


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

    col_labels = [str("name"), "landmass", "zone", "area", "population", "language",
                  "religion", "bars", "stripes", "colours", "red", "green", "blue",
                  "gold", "white", "black", "orange", "mainhue", "circles", "crosses",
                  "saltires", "quarters", "sunstar", "crescent", "triangle", "icon",
                  "animate", "text", "topleft", "botright"]

    print("number of column labels: " + str(len(col_labels)))

    col_labels_s = pd.Series(col_labels)
    print("\n")
    print(col_labels_s)

    df0 = pd.read_csv(flagfile, header=None)
    print("rows, cols of dataset: " + str(np.shape(df0)))
    print(df0.dtypes)
    print("\n")

    df1 = df0.copy()
    df1.columns = col_labels_s.astype(object)
    print(df1)
