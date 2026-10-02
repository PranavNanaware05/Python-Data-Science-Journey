import numpy as np

arr_zero=np.zeros(5)
print(arr_zero)

arr_one=np.ones(4)
print(arr_one)

full_arr=np.full((2,3),4)
print(full_arr)

arr=np.arange(1,6)
print(arr)

arr_1=np.arange(1,10,2)
print(arr_1)

arr_2=np.eye(4)
print(arr_2)

arr_2=np.linspace(0,10,5)
print(arr_2)

r_arr=np.random.randint(1,100,(3,3))
print(r_arr)