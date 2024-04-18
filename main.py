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

def sample(sample):
    ''
    # sample
    sample = 2

    return sample

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


col_labels = ["name", "landmass", "zone", "area", "population", "language",
                  "religion", "bars", "stripes", "colours", "red", "green", "blue",
                  "gold", "white", "black", "orange", "mainhue", "circles", "crosses",
                  "saltires", "quarters", "sunstar", "crescent", "triangle", "icon",
                  "animate", "text", "topleft", "botright"]

#print("number of column labels: " + str(len(col_labels)))

col_labels_s = pd.Series(col_labels)

with open("flag.data", "r") as flagfile:
    df0 = pd.read_csv(flagfile, header=None)
    #print("rows, cols of dataset: " + str(np.shape(df0)))
    #print(df0.dtypes)

df1 = df0.copy()
df1.columns = col_labels_s.astype(object)
#print(df1.head())

# -----------------------------------------------------------------------------
# Task #2:
# - Loops restricted / List comprehension structures restricted
# - Write 'percent_of_mean()'
#   - Input is a 1-D array of numeric values
#       - values represent the stock index for each day as a % of the
#         mean value over the period covered by the list
#   - Find mean of all values
#   - Store representation of each value as a % of the mean
# -----------------------------------------------------------------------------


#print(df1.groupby("landmass").size())
# or more specifically
print("Number in N. America: " + str(df1.groupby("landmass").size().get(1))
        + "\n")  # 31

# -----------------------------------------------------------------------------
# Task #3:
# - Loops restricted / List comprehension structures restricted
# - Write 'percent_of_mean()'
#   - Input is a 1-D array of numeric values
#       - values represent the stock index for each day as a % of the
#         mean value over the period covered by the list
#   - Find mean of all values
#   - Store representation of each value as a % of the mean
# -----------------------------------------------------------------------------

#print(len(df1.groupby("landmass").size()))
print("Using explicit loops:")
for x in range(1, len(df1.groupby("landmass").size()) + 1):
    print(str(x) + "\t " + str(df1.groupby("landmass").size().get(x)))

print("\n")
print("Without using explicit loops:\n" + str(df1.groupby("landmass").size())
      + "\n")

# -----------------------------------------------------------------------------
# Task #4:
# - Loops restricted / List comprehension structures restricted
# - Write 'percent_of_mean()'
#   - Input is a 1-D array of numeric values
#       - values represent the stock index for each day as a % of the
#         mean value over the period covered by the list
#   - Find mean of all values
#   - Store representation of each value as a % of the mean
# -----------------------------------------------------------------------------


lang_pop = df1.groupby("language")["population"].sum().sort_values(ascending=False)
print(lang_pop)
print("\n")

pop_sub50 = df1["population"] < 50
allrows_pop_sub50 = df1[pop_sub50]
#print(allrows_pop_sub50)
#print("\n")

lang_pop_sub50 = allrows_pop_sub50.groupby("language")["population"].sum().sort_values(ascending=False)
print(lang_pop_sub50)
print("\n")

# -----------------------------------------------------------------------------
# Task #5:
# - Loops restricted / List comprehension structures restricted
# - Write 'percent_of_mean()'
#   - Input is a 1-D array of numeric values
#       - values represent the stock index for each day as a % of the
#         mean value over the period covered by the list
#   - Find mean of all values
#   - Store representation of each value as a % of the mean
# -----------------------------------------------------------------------------


country_lang = df1.loc[:, "language"]
#print(country_lang)
#print("\n")

rep_lang = {"rep name": ["Max", "Jill", "Fong", "Juanita", "Nya"],
            "language": [1, 2, 5, 5, 8]}
#print(rep_lang)
#print("\n")
rep_df = pd.DataFrame(rep_lang)
#print(rep_df)
#print("\n")

#country_rep_lang = pd.merge(country_lang, rep_df, left_on="rep lang", right_on="language")
# rather than use left/right_on parameters I renamed the dictionary to have a matching label
country_rep_lang = pd.merge(country_lang, rep_df)
print("Total representative-countries: " + str(len(country_rep_lang)))  #91
print("\n")

# -----------------------------------------------------------------------------
# Task #6:
# - Loops restricted / List comprehension structures restricted
# - Write 'percent_of_mean()'
#   - Input is a 1-D array of numeric values
#       - values represent the stock index for each day as a % of the
#         mean value over the period covered by the list
#   - Find mean of all values
#   - Store representation of each value as a % of the mean
# -----------------------------------------------------------------------------

# groupby() way:
landmass_lang_are_gb = df1.groupby(["landmass", "language"])["area"].sum().unstack()

# pivot table way:
landmass_lang_area_pt = df1.pivot_table(index="landmass", columns="language",
                                        values="area", aggfunc="sum")

print(landmass_lang_area_pt)
# NaN represent combinations of landmass and language codes which do not exist
# within the dataset.

#pass