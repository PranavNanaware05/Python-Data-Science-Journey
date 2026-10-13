import pandas as pd
import matplotlib.pyplot as plt

data={
    'month':["jan","feb","mar","apr","may"],
    "sale":[20,30,25,40,50]
    
}

df=pd.DataFrame(data)

plt.bar(df["month"],df["sale"])
plt.xlabel("month")
plt.ylabel("Sale")
plt.title("matplotlib with pandas")
plt.show()