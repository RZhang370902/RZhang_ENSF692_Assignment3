import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

L = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])
full_data_arry = np.array([np.resize(a,(20,3)) for a in L])

print("Shape of full data array: ", full_data_arry.shape)
print("Dimensions of full data array: ", full_data_arry.ndim)

#print(full_data_arry.reshape(200,3))
grade_array = full_data_arry.reshape(200,3)
grade_array = np.array(grade_array.transpose())
#print(grade_array)
#print(grade_array.shape)
year_array = np.array(range(2013, 2023))
year_array = np.repeat(year_array, 20)
#year_array = np.tile(year_array,(1, 20))
year_array = year_array.reshape((1,200))
#L = np.ones((1,200),'i4')
#print(year_array)

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
school_array = np.tile(school_array, 10)
#school_array = school_array.reshape(200,1)
#print(school_array)

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

school_code_array = np.tile(school_code_array, 10)

#school_code_array = school_code_array.reshape(200, 1)
#print(school_code_array)
#print(L)
#print(year_array[:,np.newaxis])
#print(school_array.dtype)

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

#print(year_array.shape)
#print(all_data_array['school_name'][all_data_array['school_code'] == 9813][0])




#all_data_array = np.hstack((year_array, school_array, school_code_array, grade_array))

#all_data_array = np.hstack((year_array, school_array, school_code_array, grade_array))
#all_data_array = np.hstack((year_array, school_code_array, grade_array))
#all_data_array = all_data_array.transpose()
#all_data_array = np.array(all_data_array, dtype=([('1','i8'), ('3', 'i4') , ('4', 'f4'), ('5','f4'), ('6', 'f4')]))
#print(all_data_array[1,:])

#all_data_array = all_data_array.reshape(6, 200)
#print(all_data_array[all_data_array['school_code'] == 1224 ])
#print(year_array.dtype)
#print(grade_array.dtype)
#print(all_data_array.dtype)


user_input_2 = 'Centennial High School'
#print(user_input_2 in all_data_array['school_name'][0,0])

#user_input = input("Please enter the high school name or school code: ")
#print(user_input)


def print_school_specific_statistics_from_school_name(school_name):
    
    pass

def print_school_specific_statistics_from_school_code(school_code):
    school_name = all_data_array['school_name'][all_data_array['school_code'] == school_code][0]
    print("School name: ", school_name, ", School Code: ", school_code, sep='')
    
    print("Mean enrollement for Grade10: ", np.mean(all_data_array['grade10'][all_data_array['school_code'] == school_code], dtype= 'i4'))
    
    print("Mean enrollement for Grade10: ", np.mean(all_data_array['grade11'][all_data_array['school_code'] == school_code], dtype= 'i4'))
    
    print("Mean enrollement for Grade10: ", np.mean(all_data_array['grade12'][all_data_array['school_code'] == school_code], dtype= 'i4'))
    
    #grade_10_max = all_data_array['grade10'][all_data_array['school_code'] == school_code].max()
    #grade_11_max = all_data_array['grade11'][all_data_array['school_code'] == school_code].max()
    #grade_12_max = all_data_array['grade12'][all_data_array['school_code'] == school_code].max()
    #single_grade_max = np.array([grade_10_max, grade_11_max, grade_12_max], dtype= 'i8')
    #print("Hightest enrollment for a sigle grade: ", np.max(single_grade_max))

    x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == school_code]
    y = [list(x[i]) for i in range(x.size)]
    y = np.array(np.concatenate(y), dtype = 'i4')
    y = [i for i in y if i >= 0]
    y = np.array(y)
    print("Hightest enrollment for a sigle grade: ", np.max(y))
    print("Hightest enrollment for a sigle grade: ", np.min(y))

    #x = all_data_array[['grade10', 'grade11', 'grade12']][(all_data_array['school_year'] == 2013) & (all_data_array['school_code'] == school_code)]
    #y = np.array(list(x[0]), dtype= 'i4')
    #print("Total enrollment for 2013:", np.sum(y))

    ten_year_total = 0
    ten_year_array = np.zeros(10)
    for i in range(2013, 2023):
        x = all_data_array[['grade10', 'grade11', 'grade12']][(all_data_array['school_year'] == i) & (all_data_array['school_code'] == school_code)]
        #y = np.array(list(x[0]), dtype= 'i4')
        #y = [i for i in y if i >= 0]
        #y = np.array(y)
        y = convert_tuple_to_array(x)
        ten_year_total += np.sum(y, dtype= 'i4')
        ten_year_array[(i - 2013)] = np.sum(y)
        print("Total enrollment for ", i,": ", np.sum(y, dtype = 'i4'), sep='')

    print("Total ten year enrollment: ", ten_year_total)
    print("Mean total enrollment over 10 years: ", np.mean(ten_year_array, dtype= 'i4'))

    x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == school_code]
    #y = [list(x[i]) for i in range(x.size)]
    #y = np.array(np.concatenate(y))
    #y = [i for i in y if i >= 0]
    #y = np.array(y)
    y = convert_tuple_to_array(x)
    print("For all enrollments over 500, the median value was:  ", int(np.median(y[y > 500])))


def print_general_statistics_for_all_school():
    for i in range(2013, 2023, 9):
        #print("i: ", i)
        x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_year'] == i]
        y = convert_tuple_to_array(x)
        #y = [list(x[j]) for j in range(x.size)]
        #y = np.array(np.concatenate(y))
        #y = [i for i in y if i >= 0]
        print("Mean enrollment in ", i, ": ", np.mean(y, dtype= 'i4'), sep='')

    x = all_data_array[['grade12']][all_data_array['school_year'] == 2022]
    y = convert_tuple_to_array(x)
    print("Total graduating class of 2022: ", np.sum(y, dtype= 'i4'))

    x = all_data_array[['grade10', 'grade11', 'grade12']]
    x = np.array(x)
    x = x.reshape(x.size,)

    #x = all_data_array[['grade10', 'grade11', 'grade12']]
    y = convert_tuple_to_array(x)
    print("Total graduating", int(np.max(y)))
    print("Total graduating", int(np.min(y)))


    


def convert_tuple_to_array (x):
    y = [list(x[i]) for i in range(x.size)]
    y = np.array(np.concatenate(y))
    y = [i for i in y if i >= 0]
    y = np.array(y)
    return y



    #grade_10_min = all_data_array['grade10'][all_data_array['school_code'] == school_code].min()
    #grade_11_min = all_data_array['grade11'][all_data_array['school_code'] == school_code].min()
    #grade_12_min = all_data_array['grade12'][all_data_array['school_code'] == school_code].min()
    #single_grade_min = np.array([grade_10_min, grade_11_min, grade_12_min], dtype= 'i8')
    #print("Lowest enrollment for a sigle grade: ", np.min(single_grade_min))

    #print("Total enrollment for 2013: ", all_data_array['grade10'][all_data_array['school_code'] == school_code])
    #print("Total enrollment for 2013: ", all_data_array['grade10'][all_data_array['school_code'] == school_code & all_data_array['school_year'] == 2013])
    
    
    
    #x = [all_data_array[i][all_data_array['school_code'] == school_code].max() for i in ('grade10', 'grade11', 'grade12')]
    #print(x)


def main():
    user_input = 1

    while user_input != '0':

        user_input = input("Please enter the high school name or school code: ")
        try:
            if not((user_input in all_data_array['school_name']) or (int(user_input) in all_data_array['school_code']) or (user_input == '0')):
                raise ValueError()
            elif (user_input in all_data_array['school_name']):
                print(user_input)
            elif (int(user_input) in all_data_array['school_code']):
                print_school_specific_statistics_from_school_code(int(user_input))
                print_general_statistics_for_all_school()
                
        except ValueError:
            print("Invalid input")


if __name__ == '__main__':
    main()



