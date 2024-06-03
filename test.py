import numpy as np

from workfile1 import all_data_array 

school_code = 9857

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

