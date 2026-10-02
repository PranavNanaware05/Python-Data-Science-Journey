import pandas as pd
data={
    "Name":["pranav","Amit","rahul","Sneha"],
    "Age":[21,22,23,24],
    "Salary":[20000,30000,21000,40000]
}
df=pd.DataFrame(data)
print(df)

df["Department"]=["IT","HR","IT","Sales"]

print(df)

df["bonus"]= df["Salary"]*0.10
print(df)

df.loc[df["Salary"]<30000,"Salary"]=31000

print(df)

df.loc[df["Age"]==22,"Salary"]=33000

print(df)