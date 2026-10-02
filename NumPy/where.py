import numpy as np
marks=np.array([35,68,79,36, 20,39])

result=np.where(marks>35,"pass","fail")
print(result)