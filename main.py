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

import pandas as pd


# --> Methods:

def template(sample):
    '''
    A template for creating methods
    :param sample:
    :return:
    '''
    # sample description of instance var or associated statements
    sample = 2

    return sample


# --> Main:

# -----------------------------------------------------------------------------
# Task #1:
# - Read in the data file and save its contents as a DataFrame object
#       -Label the columns appropriately
# -----------------------------------------------------------------------------

# create a list of strings that represent the label of each column in the dataset
col_labels = ["name", "landmass", "zone", "area", "population", "language",
              "religion", "bars", "stripes", "colours", "red", "green", "blue",
              "gold", "white", "black", "orange", "mainhue", "circles", "crosses",
              "saltires", "quarters", "sunstar", "crescent", "triangle", "icon",
              "animate", "text", "topleft", "botright"]

# print("number of column labels: " + str(len(col_labels)))

# convert list to pandas object: Series
col_labels_s = pd.Series(col_labels)

# open file, "flag.data", assign to variable
with open("flag.data", "r") as flagfile:
    # read to dataframe object, clear column labels
    df0 = pd.read_csv(flagfile, header=None)

    # print("rows, cols of dataset: " + str(np.shape(df0)))
    # print(df0.dtypes)

# create copy dataframe
df1 = df0.copy()
# assign series that contain column labels as column labels to df1
df1.columns = col_labels_s.astype(object)

# print(df1.head())

# -----------------------------------------------------------------------------
# Task #2:
# - Print out how many countries in the dataset are in North America
# -----------------------------------------------------------------------------


# print(df1.groupby("landmass").size())

print("*** Task 2 ***")
# group and count all the elements in landmass col that == 1
print("Number in N. America: " + str(df1.groupby("landmass").size().get(1))
      + "\n")  # should be: 31

# -----------------------------------------------------------------------------
# Task #3:
# - Print out how many countries are in each of the landmasses
# - Do this once using explicit loops to go through the data items
#   (i.e., without using the testing and aggregation capabilities of DataFrames)
#       and once without using explicit loops
# -----------------------------------------------------------------------------


print("*** Task 3 ***")
# print(len(df1.groupby("landmass").size()))
print("Using explicit loops:")

# iterate from 1 to the total # of elements in landmass
for x in range(1, len(df1.groupby("landmass").size()) + 1):
    # iterate variable x to print total occurrences of each single int code
    print(str(x) + "\t " + str(df1.groupby("landmass").size().get(x)))

print("---")
# get and print ALL int codes and their total occurrences in column landmass
print("Without using explicit loops:\n" + str(df1.groupby("landmass").size())
      + "\n")

# -----------------------------------------------------------------------------
# Task #4:
# - Print out the total population (in millions) of the countries that speaks
#   each language
# - Print out the total population (in millions) of the countries that speak
#   each language whose national populations are less than 50 million
# - In both cases, print in decreasing order of total population
# - Any conclusions you can make from the different charts?
# -----------------------------------------------------------------------------

'''
pd.groupby() creates a new shallow dataframe which groups a field within a dataframe
by a specified label. Then by attaching an index notation we can essentially add a 
second field of associated values to compare, indexed with the first groupby() method
parameter. We then call the .sum() method which will add all values specified by the
index notation parameter and group the results by the specified groupby() method parameter.
We then call the .sort_values() method with an acending=False argument to sort the
resulting values highest to lowest.
'''
lang_pop = df1.groupby("language")["population"].sum().sort_values(ascending=False)
print("*** Task 4 ***")
print(lang_pop)
print("---")

# create a boolean mask of all entries in population column that are less than 50
pop_sub50 = df1["population"] < 50
# apply boolean mask to full dataframe to filter out all rows that do not meet condition
allrows_pop_sub50 = df1[pop_sub50]
# print(allrows_pop_sub50)
# print("\n")

# use the previous groupby() method combination from lang_pop against a dataframe which
# only contain the values of rows/countries whose population is below 50 (million)
lang_pop_sub50 = allrows_pop_sub50.groupby("language")["population"].sum().sort_values(ascending=False)
print(lang_pop_sub50)
print("\n")

'''
Any conclusions you can make from the different charts?
-English is not spoken in THAT many countries.
-The majority of countries with populations below 50 million
    do not speak any of the major languages on the list and 
    must speak their own indigenous languages.
'''

# -----------------------------------------------------------------------------
# Task #5:
# - Create a merged DataFrame object that is the intersection of the flags
#   dataset and the given employee dataset
# - Print out the total number of "representative-countries" the sales team
#   covers based on language spoken
#   - Each country whose language a sales representative can speak counts
#       as a "representative-country"
# -----------------------------------------------------------------------------

# assign to variable a series object whose values are all the values in language
country_lang = df1.loc[:, "language"]
# print(country_lang)
# print("\n")

# make dictionary of two lists, keys will be index labels, values will be entries
rep_lang = {"rep name": ["Max", "Jill", "Fong", "Juanita", "Nya"],
            "language": [1, 2, 5, 5, 8]}
# print(rep_lang)
# print("\n")

# convert dictionary to pandas dataframe
rep_df = pd.DataFrame(rep_lang)

# print(rep_df)
# print("\n")

# country_rep_lang = pd.merge(country_lang, rep_df, left_on="rep lang", right_on="language")

# rather than use left/right_on parameters I renamed the dictionary to have a matching label
country_rep_lang = pd.merge(country_lang, rep_df)  # merge "language" and dict dataframe

print("*** Task 5 ***")
# print the total number of rows/countries that are covered/paired
print("Total representative-countries: " + str(len(country_rep_lang)))  # should be: 91
print("\n")

# -----------------------------------------------------------------------------
# Task #6:
# - Print a table showing the total area of countries for each possible
#   combination of landmass and language.
# - What do the NaN values mean in that table?
# -----------------------------------------------------------------------------

# groupby() way:
# placing a list of args into the groupby() parameter allows for "match" comparison
landmass_lang_are_gb = df1.groupby(["landmass", "language"])["area"].sum().unstack()
# print(landmass_lang_are_gb)

# pivot table way:
'''
the pandas.pivot_table() method allows us to neatly specify any fields within our df1
dataframe as index/column labels/fields to be compared. We then are able to specify
which value to associate from these labels, then specify an operation to perform on 
these values, whose results will be groups as specified by the label arguments.
For this task, we are comparing which landmass int codes match up with which
language int codes, then summing their area values if a match is found.
'''
landmass_lang_area_pt = df1.pivot_table(index="landmass", columns="language",
                                        values="area", aggfunc="sum")
print("*** Task 6 ***")


# print the created pivot table, result should be identical to groupby() way
print(landmass_lang_area_pt)
'''
What do the NaN values mean in that table?
-NaN represent combinations of landmass and language codes which do not exist within 
    the dataset. Or in other words, that the selected languages are not spoken inside 
    the specified land masses.
'''

# End of File T-T #
