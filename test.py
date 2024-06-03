import numpy as np

from workfile1 import all_data_array 

school_code = 9857
'''
x = all_data_array[['grade10', 'grade11', 'grade12']][(all_data_array['school_year'] == 2013) & (all_data_array['school_code'] == 1679)]
print(x)
print(x[0])
b = list(x[0])
print(b)
print(np.sum(b))

y = all_data_array[['grade10', 'grade11', 'grade12']][(all_data_array['school_code'] == 1679)]
print(y)
c = [list(y[i]) for i in range(y.size)]
print(c)
print(np.concatenate(c))
print(np.concatenate(c).max())

x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == school_code]
print(x)
c = [list(x[i]) for i in range(x.size)]
print(c)
print(np.concatenate(c))
print(np.concatenate(c).max())
print(np.concatenate(c).min())

ten_year_array = np.zeros(10)
print(ten_year_array)
ten_year_array[5] = 1
print(ten_year_array)
'''

school_code = 9857
'''
x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == school_code]
y = [list(x[i]) for i in range(x.size)]
y = np.array(np.concatenate(y), dtype = 'i4')
print(y)
print(int(np.median(y[y > 500])))

x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_year'] == 2013]
y = [list(x[i]) for i in range(x.size)]
y = np.array(np.concatenate(y), dtype = 'i4')
print(np.mean(y, dtype='i4'))
'''
def print_general_statistics_for_all_school():
    for i in range(2013, 2023, 9):
        print("i: ", i)
        x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_year'] == i]
        y = [list(x[j]) for j in range(x.size)]
        y = np.array(np.concatenate(y))
        print(y)
        y = [i for i in y if i >= 0]
        print(np.mean(y, dtype= 'i4'))

print_general_statistics_for_all_school()
'''
x = all_data_array[['grade10', 'grade11', 'grade12']][(all_data_array['school_year'] == 2022)]
print(x)
y = [list(x[j]) for j in range(x.size)]
y = np.array(np.concatenate(y))
y = [i for i in y if i > 0]
print(np.mean(y, dtype = 'i4'))
'''

x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == school_code]
print(x)
print(x.size)
print(x.shape)
y = [list(x[i]) for i in range(x.size)]
y = np.array(np.concatenate(y))
y = [i for i in y if i >= 0]
y = np.array(y)
#print(y)
print("For all enrollments over 500, the median value was:  ", int(np.median(y[y > 500])))

#x = all_data_array[['grade10', 'grade11', 'grade12']]
#x = all_data_array['grade10']['grade11']['grade12']
x = all_data_array[['grade10', 'grade11', 'grade12']]
x = np.array(x)
print(x)
x = x.reshape(x.size)
print(x)
#print(x)
print(x.shape)
#y = list(x[0])
#print(y)
y = [list(x[i]) for i in range(x.size)]
y = np.array(np.concatenate(y))
y = [i for i in y if i >= 0]
y = np.array(y)
print(int(np.max(y)))
print(int(np.min(y)))
#y = convert_tuple_to_array(x)
#print("Total graduating", np.max(y, dtype= 'i4'))

from school_data import name_code_array
x = name_code_array['school_code'][name_code_array['school_name'] == 'John G Diefenbaker High School']
print(x[0])

print()
print()
x = all_data_array['grade10'][all_data_array['school_code'] == 9830]
y = np.array(x)
y = [i for i in y if i >= 0]
print(x)
print(y)

for i in ('a', 'b', 'c'):
    print(i)

from school_data import convert_tuple_to_array

x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == 9830]
y = convert_tuple_to_array(x)
print(np.any(y > 500))
