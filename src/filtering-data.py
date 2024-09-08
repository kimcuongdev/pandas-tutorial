import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
bios = pd.read_csv('bios.csv')
print(bios.head())

#loc[điều kiện hàng, cột chọn]
print(bios.loc[bios['height_cm'] > 215])
print(bios.loc[bios['height_cm'] > 215, ['name','height_cm']])
print(bios.loc[(bios['height_cm'] > 180) & (bios['weight_kg'] > 150) & (bios['born_country'] == 'USA'), ['name','height_cm','weight_kg']])

#str.contains('tên chuỗi con', case = có phân biệt viết hoa không, regex= có dùng regex không)
print(bios.loc[bios['name'].str.contains('Stanley'),['name','athlete_id']])
print(bios.loc[bios['name'].str.contains('Stanley|Stanford'),['name','athlete_id']]) #có sử dụng regex

#isin([list các chuỗi])
print(bios.loc[bios['born_country'].isin(['USA','FRA','VN']), ['name','born_country']])
print(bios.loc[bios['born_country'].isin(['USA','FRA','VN']), ['name','born_country']])
print(bios.loc[(bios['born_country'].isin(['USA','FRA','VN'])) & (bios['name'].str.startswith('Keith')), ['name','born_country']])

#query
print(bios.query('born_country == "USA" and born_city == "Seattle" and height_cm > 175'))
print(bios.query('born_country == "USA" and born_city == "Seattle" and height_cm > 175')[['name','born_country','born_city','height_cm']])

