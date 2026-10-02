import numpy as np
age = np.array([15, 22, 17, 30, 16, 25])

print(np.where(age>=18,"Adult","minor"))