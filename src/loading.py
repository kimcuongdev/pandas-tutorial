import  pandas as pd
coffee = pd.read_csv('coffee.csv')
print(coffee.head()) #In ra 5 hàng đầu
results = pd.read_parquet('results.parquet')
print(results.head())
olympics_data = pd.read_excel('olympics-data.xlsx')
print(olympics_data.head()) #rất tốn tgian
bios = pd.read_csv('bios.csv')
bios.to_parquet('bios.parquet')
print(bios.head())

