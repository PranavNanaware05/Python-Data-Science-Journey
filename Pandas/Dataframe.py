import pandas as pd

data={
    'name':["rahul","vishakha","lalita","rishabh"],
    'age':[16,17,18,19]
}

df=pd.DataFrame(data)

print(df)
print(type(df))