import pandas as pd
data={
    "Name":["Pranav","Rohit","Sneha"],
    "Age":[21,22,23],
    "City":["Pune","Satara","Sangali"],
    "Salary":[24000,40000,32000]
}

df=pd.DataFrame(data)
print(df)

df.loc[len(df)]=["Kiran",25,"Pune",32000]
print(df)

df.loc[2,"Age"]=25
print(df)