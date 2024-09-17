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
'''
Argument Definition:
DataFrame.rename(mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='raise')

mapper, index, columns: The dictionaries you can pass to rename index or columns. 

axis: Can be either "index" or "columns". 
        Determines whether you're renaming the index or the columns. 
        By default, if you provide the columns argument, you're renaming columns.

copy: If set to True, a new DataFrame is created. 
        If False, the original DataFrame is modified.

inplace: If set to True, the renaming will modify the DataFrame in place and nothing will be returned. 
        If False, a new DataFrame with renamed columns will be returned without modifying the original DataFrame.

level: For DataFrames with multi-level index, level from which the labels should be renamed.

errors: If 'raise', an error is raised if you try to rename an item that doesn't exist. 
        If set to 'ignore', any failure to rename items will be ignored.
'''
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
#astype()
'''
DataFrame.astype(dtype, copy=True, errors='raise')
dtype: It's a data type, or dict of column name -> data type.

copy: By default, astype always returns a newly allocated object. 
    If copy is set to False, a new object will only be created if the old object cannot be casted to the required type.
errors: Controls the raising of exceptions on invalid data for the provided dtype.
    By default, raise is set which means exceptions will be raised.
So in our case we want to cast the grade column from float to int 
    and we can do so with the following line:
    students = students.astype({'grade': int})
'''


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