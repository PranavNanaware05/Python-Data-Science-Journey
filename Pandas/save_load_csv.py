import pandas as pd
data={
    "name":["pranav","Amit","vishakha"],
    "age":[17,18,19],
    "salary":[10000,20000,30000]
}

df=pd.DataFrame(data)

print(df)

df.to_csv("example_data.csv",index=False)

df1=pd.read_csv("example_data.csv")
print(df1)