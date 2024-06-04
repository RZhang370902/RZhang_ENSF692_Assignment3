# school_data.py
# AUTHOR NAME
# Rick Zhang
# A terminal-based application for computing and printing statistics based on given input.
# To use the program, first run the code, then input school code or school name.
# e.g. James Folwer High School         or          9823
# If input invalid, program will ask for input again until a valid input is detected.
# Enter 0 to stop the program
# main is at line 320~
# line 27 to line 168 contain hards codes to create numpy arrays required by functions
# line 172 to line 319 contain functions
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

# Create a 3-dimensional array using the provided high school enrollment data.
L = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])
full_data_arry = np.array([np.resize(a,(20,3)) for a in L])


# Create a structred arrary similar to the provided Assignment3Data.csv.
# The goal is to get the same result as using Pandas to read the csv file.
# Assignment3Data.csv is for reference only, so it's not allowed to use Pandas
# to read it.
# Shape of the final array:
# [Year, School Name,    School Code,    Grade10 Data,   Grade11 Data,   Grade 12 Data]
# [20xx  xxx school      98xx            123             123             123          ]
# [...   ...             ...             ...             ...             ...          ]
# [...   ...             ...             ...             ...             ...          ]

# Create grade_array that contains data of each year. Shape (3, 200), row for grade, col for data
grade_array = full_data_arry.reshape(200,3)
grade_array = np.array(grade_array.transpose())

# Create year_array that contains each year. e.g [2013, 2014...2022]
year_array = np.array(range(2013, 2023))

# Cretea school_array that contains all school names. Shape (20,)
school_array = np.array(['Centennial High School', 
                         'Robert Thirsk School', 
                         'Louise Dean School', 
                         'Queen Elizabeth High School', 
                         'Forest Lawn High School', 
                         'Crescent Heights High School', 
                         'Western Canada High School', 
                         'Central Memorial High School', 
                         'James Fowler High School', 
                         'Ernest Manning High School', 
                         'William Aberhart High School', 
                         'National Sport School', 
                         'Henry Wise Wood High School', 
                         'Bowness High School', 
                         'Lord Beaverbrook High School', 
                         'Jack James High School', 
                         'Sir Winston Churchill High School', 
                         'Dr. E. P. Scarlett High School', 
                         'John G Diefenbaker High School', 
                         'Lester B. Pearson High School'])

# Create school_code_array that contains all school codes. Shape (20,)
school_code_array = np.array([1224, 
                              1679, 
                              9626, 
                              9806, 
                              9813, 
                              9815, 
                              9816, 
                              9823, 
                              9825, 
                              9826, 
                              9829, 
                              9830, 
                              9836, 
                              9847, 
                              9850, 
                              9856, 
                              9857, 
                              9858, 
                              9860, 
                              9865])


#name_code_array = np.zeros(school_code_array.shape, dtype= [('school_code', school_code_array.dtype), 
#                                                     ('school_name', school_array.dtype)])

#name_code_array['school_code'] = school_code_array
#name_code_array['school_name'] = school_array

'''
name_code_dic = {'Centennial High School':1224, 
                         'Robert Thirsk School':1679, 
                         'Louise Dean School':9626, 
                         'Queen Elizabeth High School':9806, 
                         'Forest Lawn High School':9813, 
                         'Crescent Heights High School':9815, 
                         'Western Canada High School':9816, 
                         'Central Memorial High School':9823, 
                         'James Fowler High School':9825, 
                         'Ernest Manning High School':9826, 
                         'William Aberhart High School':9829, 
                         'National Sport School':9830, 
                         'Henry Wise Wood High School':9836, 
                         'Bowness High School':9847, 
                         'Lord Beaverbrook High School':9850, 
                         'Jack James High School':9856, 
                         'Sir Winston Churchill High School':9857, 
                         'Dr. E. P. Scarlett High School':9858, 
                         'John G Diefenbaker High School':9860, 
                         'Lester B. Pearson High School':9865}
'''
# Size of array created above:
# grade_array (3, 200)
# school_array (20, )
# school_code_array (20, )
# year_array (10, ) Need to stratch the last 3 arrays to match grade_array
school_array = np.tile(school_array, 10) # Stretch school_array from (20,) to (200,) to matach grade array(3, 200)
school_code_array = np.tile(school_code_array, 10) # Stretch school_code_array from (20,) to (200,) to matach grade array(3, 200)
year_array = np.repeat(year_array, 20) # Stretch year_array from (20,) to (200,) to matach grade array(3, 200)
year_array = year_array.reshape((1,200)) # Reshpae year_array

# Create a structured array to merge grade_array, school_array, school_code_array, and year_array
all_data_array = np.zeros(year_array.shape, dtype=[('school_year', year_array.dtype), 
                                                   ('school_name', school_array.dtype), 
                                                   ('school_code', school_code_array.dtype), 
                                                   ('grade10', full_data_arry.dtype),
                                                   ('grade11', full_data_arry.dtype), 
                                                   ('grade12', full_data_arry.dtype)])

# assign grade_array, school_array, school_code_array, and year_array to structured array
all_data_array['school_year'] = year_array
all_data_array['school_name'] = school_array
all_data_array['school_code'] = school_code_array
all_data_array['grade10'] = grade_array[0:1, :] # Subarray
all_data_array['grade11'] = grade_array[1:2, :]
all_data_array['grade12'] = grade_array[2:3, :]
# Shape of the final array:
# [Year, School Name,    School Code,    Grade10 Data,   Grade11 Data,   Grade 12 Data]
# [20xx  xxx school      98xx            123             123             123          ]
# [...   ...             ...             ...             ...             ...          ]
# [...   ...             ...             ...             ...             ...          ]

# Create a dictional index: school name, value: school code
name_code_dic = {'Centennial High School':1224, 
                         'Robert Thirsk School':1679, 
                         'Louise Dean School':9626, 
                         'Queen Elizabeth High School':9806, 
                         'Forest Lawn High School':9813, 
                         'Crescent Heights High School':9815, 
                         'Western Canada High School':9816, 
                         'Central Memorial High School':9823, 
                         'James Fowler High School':9825, 
                         'Ernest Manning High School':9826, 
                         'William Aberhart High School':9829, 
                         'National Sport School':9830, 
                         'Henry Wise Wood High School':9836, 
                         'Bowness High School':9847, 
                         'Lord Beaverbrook High School':9850, 
                         'Jack James High School':9856, 
                         'Sir Winston Churchill High School':9857, 
                         'Dr. E. P. Scarlett High School':9858, 
                         'John G Diefenbaker High School':9860, 
                         'Lester B. Pearson High School':9865}

# You may add your own additional classes, functions, variables, etc.

# If school name is entered, retrive school code from name_code_dic.
# Use to school code to call function print_school_specific_statistics_from_school_code().
def print_school_specific_statistics_from_school_name(school_name):
    """print_school_specific_statistics_from_school_name:
        If school name is entered, retrive school code from name_code_dic.
        Use to school code to call function print_school_specific_statistics_from_school_code().

    Args:
        school_name ('str'): String value represents school name

    Returns:
        None
    """
    x = name_code_dic[school_name]
    print_school_specific_statistics_from_school_code(x)


# Take school code entered by user.
# Calculate and print school specific statistics .
def print_school_specific_statistics_from_school_code(school_code):
    """print_school_specific_statistics_from_school_code:
        If school code is entered. Do the following calculation and print out the ressults
        ---1. The school name and school code
        ---2. Mean enrollment for Grade 10 across all years
        ---3. Mean enrollment for Grade 11 across all years
        ---4. Mean enrollment for Grade 12 across all years
        ---5. Highest enrollment for a single grade within the entire time period
        ---6. Lowest enrollment for a single grade within the entire time period
        ---7. Total enrollment for each year from 2013 to 2022
        ---8. Total ten year enrollment
        ---9. Mean total yearly enrollment over 10 years
        ---10. Education planners want to better understand the impact 
            of large-scale classes in high schools. Determine if any enrollment numbers were over 500.
            If not, print “No enrollments over 500.” If yes, print the median value of the >500 enrollments.

    Args:
        school_code ('int'): Int value represents school code

    Returns:
        None
    """

    # ---1. Print school name and school code entered by user
    school_name = all_data_array['school_name'][all_data_array['school_code'] == school_code][0]
    print("School name: ", school_name, ", School Code: ", school_code, sep='')
    
    # ---2. Mean enrollment for Grade 10 across all years
    # ---3. Mean enrollment for Grade 11 across all years
    # ---4. Mean enrollment for Grade 12 across all years
    for i in ('grade10', 'grade11', 'grade12'):
        x = all_data_array[i][all_data_array['school_code'] == school_code]
        y = np.array(x)
        #y = [i for i in y if i >= 0]
        y = y[np.isfinite(y)] #Handle Nan
        print("Mean enrollement for ", i.capitalize(), ': ', int(np.mean(y)),sep= '')
    
    #---5. Highest enrollment for a single grade within the entire time period
    #---6. Lowest enrollment for a single grade within the entire time period
    x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == school_code]
    y = [list(x[i]) for i in range(x.size)]
    y = np.array(np.concatenate(y))
    #y = [i for i in y if i >= 0]
    y = y[np.isfinite(y)] #Handle Nan
    y = np.array(y)
    print("Hightest enrollment for a sigle grade: ", int(np.max(y)))
    print("Lowest enrollment for a sigle grade: ", int(np.min(y)))

    #---7. Total enrollment for each year from 2013 to 2022
    #---8. Total ten year enrollment
    #---9. Mean total yearly enrollment over 10 years
    ten_year_total = 0
    ten_year_array = np.zeros(10)
    for i in range(2013, 2023):
        x = all_data_array[['grade10', 'grade11', 'grade12']][(all_data_array['school_year'] == i) & (all_data_array['school_code'] == school_code)]
        y = convert_tuple_to_array(x) #np calculation doesn't support data structure of x
        ten_year_total += np.sum(y, dtype= 'i4')
        if (np.any(y>=0)):
            ten_year_array[(i - 2013)] = np.sum(y)
            print("Total enrollment for ", i,": ", np.sum(y, dtype = 'i4'), sep='')
        else: print("Total enrollment for ", i,": ", "no data available", sep='')

    print("Total ten year enrollment: ", ten_year_total)
    print("Mean total enrollment over 10 years: ", np.mean(ten_year_array, dtype= 'i4'))

    #-10. Education planners want to better understand the impact 
    #     of large-scale classes in high schools. Determine if any enrollment numbers were over 500.
    #     If not, print “No enrollments over 500.” If yes, print the median value of the >500 enrollments.
    x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == school_code]
    y = convert_tuple_to_array(x)
    if(np.any(y > 500)):
        print("For all enrollments over 500, the median value was:  ", int(np.median(y[y > 500])))
    else: print("There is no enrollments over 500.")


def print_general_statistics_for_all_school():
    """print_general_statistic_for_all_school:
        If school code is entered. Do the following calculation and print out the ressults
        ---1. The mean enrollment in 2013
        ---2. The mean enrollment in 2022
        ---3. Total graduating class of 2022 across all schools
        ---4. Highest enrollment for a single grade within the entire time period (across all schools)
        ---5. Lowest enrollment for a single grade within the entire time period (across all schools)

    Args:
        None

    Returns:
        None
    """
    # ---1. The mean enrollment in 2013
    # ---2. The mean enrollment in 2022
    for i in range(2013, 2023, 9):
        x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_year'] == i] # example of masking
        y = convert_tuple_to_array(x)
        print("Mean enrollment in ", i, ": ", np.mean(y, dtype= 'i4'), sep='')

    # ---3. Total graduating class of 2022 across all schools
    x = all_data_array[['grade12']][all_data_array['school_year'] == 2022]
    y = convert_tuple_to_array(x)
    print("Total graduating class of 2022: ", np.sum(y, dtype= 'i4'))

    # ---4. Highest enrollment for a single grade within the entire time period (across all schools)
    # ---5. Lowest enrollment for a single grade within the entire time period (across all schools)
    x = all_data_array[['grade10', 'grade11', 'grade12']]
    x = np.array(x)
    x = x.reshape(x.size,)
    y = convert_tuple_to_array(x)
    print("Highest enrollment for a single grade:", int(np.max(y)))
    print("Lowest enrollment for a single grade:", int(np.min(y)))


# Convert structured array to non-structured array
# Sometime, numpy calculation doesn't work on structured array
def convert_tuple_to_array (x):
    """convert_tuple_to_array: Convert structured array to non-structured array

    Args:
        x (numpy array): data in this numpy array is in cutom data structure.

    Returns:
        y (numpy array): data that has no data structure
    """
    y = [list(x[i]) for i in range(x.size)]
    y = np.array(np.concatenate(y))
    #y = [i for i in y if i >= 0]
    y = y[np.isfinite(y)]
    y = np.array(y)
    return y

def main():
    user_input = '1' # initiate the user_input to start the while loop

    while user_input != '0':
        print("\n\nENSF 692 School Enrollment Statistics\n\n")

        # Print Stage 1 requirements here

        print("Shape of full data array: ", full_data_arry.shape)
        print("Dimensions of full data array: ", full_data_arry.ndim)

        # Prompt for user input
        user_input = input("Please enter the high school name or school code: ")
        

        try:
            if not((user_input in all_data_array['school_name']) or (int(user_input) in all_data_array['school_code']) or (user_input == '0')):
                raise ValueError()
        # Print Stage 2 requirements here
            elif (user_input in all_data_array['school_name']):
                print("\n***Requested School Statistics***\n")
                print_school_specific_statistics_from_school_name(user_input)
            elif (int(user_input) in all_data_array['school_code']):
                print("\n***Requested School Statistics***\n")
                print_school_specific_statistics_from_school_code(int(user_input))
            elif(user_input == '0'):
                print("Program Ends")
                break

        # Print Stage 3 requirements here
            print("\n***General Statistics for All Schools***\n")
            print_general_statistics_for_all_school()
                
        except ValueError:
            print("Invalid input. Please input school code or name. Enter 0 to quit.")


if __name__ == '__main__':
    main()

