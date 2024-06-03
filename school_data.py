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

L = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])
full_data_arry = np.array([np.resize(a,(20,3)) for a in L])
grade_array = full_data_arry.reshape(200,3)
grade_array = np.array(grade_array.transpose())
year_array = np.array(range(2013, 2023))



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

name_code_array = np.zeros(school_code_array.shape, dtype= [('school_code', school_code_array.dtype), 
                                                     ('school_name', school_array.dtype)])

name_code_array['school_code'] = school_code_array
name_code_array['school_name'] = school_array

print(name_code_array)

school_array = np.tile(school_array, 10)
school_code_array = np.tile(school_code_array, 10)
year_array = np.repeat(year_array, 20)
year_array = year_array.reshape((1,200))


all_data_array = np.zeros(year_array.shape, dtype=[('school_year', year_array.dtype), 
                                                   ('school_name', school_array.dtype), 
                                                   ('school_code', school_code_array.dtype), 
                                                   ('grade10', full_data_arry.dtype),
                                                   ('grade11', full_data_arry.dtype), 
                                                   ('grade12', full_data_arry.dtype)])

all_data_array['school_year'] = year_array
all_data_array['school_name'] = school_array
all_data_array['school_code'] = school_code_array
all_data_array['grade10'] = grade_array[0:1, :] #subarray
all_data_array['grade11'] = grade_array[1:2, :]
all_data_array['grade12'] = grade_array[2:3, :]

# You may add your own additional classes, functions, variables, etc.

def print_school_specific_statistics_from_school_name(school_name):
    x = name_code_array['school_code'][name_code_array['school_name'] == school_name]
    print_school_specific_statistics_from_school_code(x[0])
    

def print_school_specific_statistics_from_school_code(school_code):
    school_name = all_data_array['school_name'][all_data_array['school_code'] == school_code][0]
    print("School name: ", school_name, ", School Code: ", school_code, sep='')
    
    '''
    x = all_data_array['grade10'][all_data_array['school_code'] == school_code]
    y = np.array(x)
    y = [i for i in y if i >= 0]
    #y = convert_tuple_to_array(x)
    print("Mean enrollement for Grade10: ", int(np.mean(y)))
    #print("Mean enrollement for Grade11: ", np.mean(all_data_array['grade11'][all_data_array['school_code'] == school_code], dtype= 'i4'))
    #print("Mean enrollement for Grade12: ", np.mean(all_data_array['grade12'][all_data_array['school_code'] == school_code], dtype= 'i4'))

    x = all_data_array['grade11'][all_data_array['school_code'] == school_code]
    y = np.array(x)
    y = [i for i in y if i >= 0]
    #y = convert_tuple_to_array(x)
    print("Mean enrollement for Grade10: ", int(np.mean(y)))

    x = all_data_array['grade12'][all_data_array['school_code'] == school_code]
    y = np.array(x)
    y = [i for i in y if i >= 0]
    #y = convert_tuple_to_array(x)
    print("Mean enrollement for Grade10: ", int(np.mean(y)))
'''

    for i in ('grade10', 'grade11', 'grade12'):
        x = all_data_array[i][all_data_array['school_code'] == school_code]
        y = np.array(x)
        y = [i for i in y if i >= 0]
        #y = convert_tuple_to_array(x)
        print("Mean enrollement for ", i.capitalize(), ': ', int(np.mean(y)),sep= '')
    

    x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == school_code]
    y = [list(x[i]) for i in range(x.size)]
    y = np.array(np.concatenate(y))
    y = [i for i in y if i >= 0]
    y = np.array(y)
    print("Hightest enrollment for a sigle grade: ", int(np.max(y)))
    print("Hightest enrollment for a sigle grade: ", int(np.min(y)))


    ten_year_total = 0
    ten_year_array = np.zeros(10)
    for i in range(2013, 2023):
        x = all_data_array[['grade10', 'grade11', 'grade12']][(all_data_array['school_year'] == i) & (all_data_array['school_code'] == school_code)]
        y = convert_tuple_to_array(x)
        ten_year_total += np.sum(y, dtype= 'i4')
        ten_year_array[(i - 2013)] = np.sum(y)
        print("Total enrollment for ", i,": ", np.sum(y, dtype = 'i4'), sep='')

    print("Total ten year enrollment: ", ten_year_total)
    print("Mean total enrollment over 10 years: ", np.mean(ten_year_array, dtype= 'i4'))

    x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == school_code]
    y = convert_tuple_to_array(x)
    print("For all enrollments over 500, the median value was:  ", int(np.median(y[y > 500])))


def print_general_statistics_for_all_school():
    for i in range(2013, 2023, 9):
        x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_year'] == i]
        y = convert_tuple_to_array(x)
        print("Mean enrollment in ", i, ": ", np.mean(y, dtype= 'i4'), sep='')

    x = all_data_array[['grade12']][all_data_array['school_year'] == 2022]
    y = convert_tuple_to_array(x)
    print("Total graduating class of 2022: ", np.sum(y, dtype= 'i4'))

    x = all_data_array[['grade10', 'grade11', 'grade12']]
    x = np.array(x)
    x = x.reshape(x.size,)
    y = convert_tuple_to_array(x)
    print("Total graduating", int(np.max(y)))
    print("Total graduating", int(np.min(y)))



def convert_tuple_to_array (x):
    y = [list(x[i]) for i in range(x.size)]
    y = np.array(np.concatenate(y))
    y = [i for i in y if i >= 0]
    y = np.array(y)
    return y

def main():
    user_input = '1'
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
            print("Invalid input")


if __name__ == '__main__':
    main()

