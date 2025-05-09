'''
Introduction to Data Science
Teju Kolawole
Lab 7
'''
#%%

x = 3.55
y = 7.23
z = 1.7
v = 2.4912
b = 4.573
num_values = 5
average = (x + y + z + v + b + num_values)/ 6
print (f"MEAN:{average:.2f}")

#%%

import math

a = pow(x-average, 2)
g = pow(y-average, 2)
c = pow(z-average, 2)
e = pow(v-average, 2)
f = pow(b-average, 2)
sum_squares = a + g + c + e + f
sample_stdev = sum_squares / (num_values-1)
print(f"STDEV: {sample_stdev:.2f}")

#%%

get_mean_of_five = (sample_stdev) 
mean_of_five = get_mean_of_five(3.55, 7.23, 1.7, 2.4912, 4.573)
print(mean_of_five)

#%%

get_stdev_of_five = sample_stdev
stdev_of_five = get_stdev_of_five(3.55, 7.23, 1.7, 2.4912, 4.573)
print(stdev_of_five)