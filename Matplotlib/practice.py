import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 120, 150, 130, 180, 200],
    "Expenses": [60, 70, 80, 75, 90, 100],
    "Customers": [50, 55, 70, 65, 85, 95]
}

df=pd.DataFrame(data)
df["Profit"]=np.subtract(df["Sales"],df["Expenses"])

print(df)
plt.figure(figsize=(10,8))

plt.subplot(1,2,1)
plt.plot(df["Month"],df["Sales"],marker="o")
plt.plot(df["Month"],df["Expenses"],marker="o")
plt.title("Sales vs Expenses")
plt.legend()
plt.grid()


plt.subplot(1,2,2)
bars=plt.bar(df["Month"],df["Profit"])
plt.title("Monthly Profit")
plt.bar_label(bars)
plt.grid(axis="y")

plt.tight_layout()
plt.show()