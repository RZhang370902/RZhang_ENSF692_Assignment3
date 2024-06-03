import numpy as np
import pandas as pd



school_year = pd.read_csv('Assignment3Data.csv')['School Year'].values
school_name = pd.read_csv('Assignment3Data.csv')['School Name'].values
school_code = pd.read_csv('Assignment3Data.csv')['School Code'].values
grade_10 = pd.read_csv('Assignment3Data.csv')['Grade 10'].values
grade_11 = pd.read_csv('Assignment3Data.csv')['Grade 11'].values
grade_12 = pd.read_csv('Assignment3Data.csv')['Grade 12'].values


print(school_year)
#print(school_name)
#print(school_code)
#print(grade_10)
#print(grade_11)
#print(grade_12)


school_data = np.zeros(school_year.shape, dtype=[('school_year', school_year.dtype),
                                 ('school_name', school_name.dtype),
                                 ('school_code', school_code.dtype),
                                 ('grade_10', grade_10.dtype),
                                 ('grade_11', grade_11.dtype),
                                 ('grade_12', grade_12.dtype)])

#school_data.reshape(school_year.shape)

print(school_year.shape)
print(school_data.shape)
print(school_data.dtype)
print(school_code.dtype)


school_data['school_year'] = school_year
school_data['school_name'] = school_name
school_data['school_code'] = school_code
school_data['grade_10'] = grade_10
school_data['grade_11'] = grade_11
school_data['grade_12'] = grade_12
#print(school_data['school_year'])
#print(school_data)

user_input_1 = 1224
user_input_2 = 'Centennial High School'
user_input_3 = 'Louise Dean School'
user_input_4 = 9857
#print(school_data[:][school_data['school_code'] == 1224])
#print(school_data[:][school_data['school_name'] == user_input_3])
print(np.mean(school_data['grade_10'][school_data['school_code'] == user_input_4],dtype='i4'))

#print(np.isin(school_data['school_name'], user_input_2))
print(user_input_1 in school_data['school_name'])