import pandas as pd
coffee = pd.read_csv('coffee.csv')
print(coffee.head())

#loc[]
coffee.loc[0,"Units Sold"] = 10
print(coffee.head())
coffee.loc[1:3,"Units Sold"] = 10 #row trong đoạn [a,b]
print(coffee.head())

