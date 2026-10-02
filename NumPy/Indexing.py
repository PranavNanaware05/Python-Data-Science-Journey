import numpy as np

arr_1=np.array([10,20,30,40,50])
print(arr_1)

print(arr_1[0])#10
print(arr_1[-1])

arr_2=np.array([
    [10,20,30],
    [40,50,60]
    ])

print(arr_2)
print(arr_2[0][1])#20
print(arr_2[1][1])#50
print(arr_2[1][-1])#60