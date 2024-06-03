# school_data.py
# AUTHOR NAME
# Rick Zhang
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here


# You may add your own additional classes, functions, variables, etc.


def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    L = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])
    full_data_arry = np.array([np.resize(a,(20,3)) for a in L])
    
    #print(full_data_array)

    print("Shape of full data array: ", full_data_arry.shape)
    print("Dimensions of full data array: ", full_data_arry.ndim)

    # Prompt for user input
    school = input("Please enter the high school name or school code: ")
    print(school)

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    print("School Name: ", ", School Code: ")

    print("Mean enrollment for Grade 10: ")
    print("Mean enrollment for Grade 11: ")
    print("Mean enrollment for Grade 12: ")

    print("Hightest enrollement for a single grade: ")
    print("Lowest enrollement for a single grade: ")

    print("Total enrollment for 2013: ")




    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

