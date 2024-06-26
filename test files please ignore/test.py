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



for i in ('a', 'b', 'c'):
    print(i)

from school_data import convert_tuple_to_array

x = all_data_array[['grade10', 'grade11', 'grade12']][all_data_array['school_code'] == 9830]
y = convert_tuple_to_array(x)
print(np.any(y > 500))

print()
print()

ten_year_total = 0
ten_year_array = np.zeros(10)
x = all_data_array[['grade10', 'grade11', 'grade12']][(all_data_array['school_year'] == 2022) & (all_data_array['school_code'] == 9830)]
y = convert_tuple_to_array(x)

print(np.any(y>=0))
#ten_year_total += np.sum(y, dtype= 'i4')
#ten_year_array[(i - 2013)] = np.sum(y)
#print("Total enrollment for ", i,": ", np.sum(y, dtype = 'i4'), sep='')

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

print(school_code_array.shape)

a = '0'
print(type(a))