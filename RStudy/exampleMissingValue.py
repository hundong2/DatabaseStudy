import pandas as pd

#input data 
df = pd.DataFrame({'A': [1,2,None,4],
                  'B': [5, None, 7, 8]})

print("input value\n")
print(df)
print("\n")
#Eliminate row that missing value                   
df.dropna(inplace=True)

print("df.dropna(), row\n")
print(df)
print("\n")
#Eliminate column that mising value
df.dropna(axis=1, inplace=True)

print(df)




