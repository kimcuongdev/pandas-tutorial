import pandas as pd
import numpy as np
coffee = pd.read_csv('coffee.csv')
print(coffee.head())
coffee['price'] = 1.23
print(coffee.head())
coffee['new_price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99,coffee['price'])
print(coffee.head())

#drop
#khi drop bình thường thì sẽ không update dữ liệu
#nếu muốn drop mà update dữ liệu thì thêm điều kiện inplace = True
print(coffee.drop(columns=['price']))
print(coffee.head())
coffee.drop(columns=['price'],inplace=True)
print(coffee.head())
#hoặc có thể xóa một cách đơn giản:
#coffee = coffee(['Day','Coffee Type','Units Sold','new_price'])

#copy
'''
Hàm copy() trong pandas hoạt động tương tự copy trong numpy
VD: nếu khởi tạo dataframe coffee_new = coffee, ở đây coffee_new trỏ đến coffee
nên nếu thay đổi coffee_new thì coffee cũng thay đổi
=> khắc phục: coffee_new = coffee.copy()
'''

#Tạo thêm cột mang giá trị suy diễn
coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']
print(coffee.head())

#rename
coffee.rename(columns={'new_price':'price'}, inplace=True)
print(coffee.head())

#Sử dụng các hàm trong str
bios = pd.read_csv('bios.csv')
bios_new = bios.copy()
bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
print(bios_new[['name','first_name']].head())
print(bios_new[['name','first_name']].query('first_name == "Stanley"'))

#Biến đổi kiểu dl
bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'])
bios_new['born_year'] = bios_new['born_datetime'].dt.year
print(bios_new[['name','born_datetime','born_year']].head())

#Save
bios_new.to_csv('bios_new.csv',index=False)

#apply()
#apply được truyền một lambda function
bios['height_category'] = bios['height_cm'].apply(lambda x: 'Short' if x < 165 else ('Average' if x < 185 else 'Tall'))
print(bios[['name','height_cm','height_category']].head())
#apply được truyền một hàm
def category_athlete(row):
    if row['height_cm'] < 165 and row['weight_kg'] < 70:
        return 'Light Weight'
    elif row['height_cm'] < 185 or row['weight_kg'] <= 80:
        return 'Middle Weight'
    else:
        return 'Heavy Weight'
bios['Category'] = bios.apply(category_athlete, axis = 1) #axis = 1 để áp dụng lên hàng
print(bios[['name','weight_kg','height_cm','height_category','Category']].head())