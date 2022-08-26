#create two python lists
list_x = list(range(100000))
list_y = list(range(100000))

# import numpy library
import numpy as np

# create two numpy Arrays using above two lists
arr_x = np.array(list_x)
arr_y = np.array(list_y)


# Define a function to calculate the sum
# using python list
def list_sum():
    z = [] # an empty list to store sum
    for i in range(len(list_x)):
        z.append(list_x[i] + list_y[i])


# Define a function to calculate the sum
# Using numpy array
def numpy_arr_sum():
    # In numpy we can directly perform sum element-wise as
    z = arr_x + arr_y

# IMport Timer class from timeit library
from timeit import Timer
timer_obj1 = Timer("list_sum()",
                    "from __main__ import list_sum")
timer_obj2 = Timer("numpy_arr_sum()",
                    "from __main__ import numpy_arr_sum")

print ("Pure python version:",timer_obj1.timeit(1000))
print ("Numpy version:",timer_obj2.timeit(1000))
