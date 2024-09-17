import numpy as np
import pandas as pd
coffee = pd.read_csv('coffee.csv')
coffee['price'] = 1.23
coffee['new_price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99,coffee['price'])
coffee.drop(columns=['price'],inplace=True)
coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']
coffee.rename(columns={'new_price':'price'}, inplace=True)

coffee.loc[[0,1],'Units Sold'] = np.nan
print(coffee.head())
print(coffee.info())

#isna() xem dữ liệu có phải là null hay không
print(coffee.isna())
print(coffee.isna().sum())

#fillna() fill vào những vị trí null
'''
The fillna function has several arguments that you can utilize, but we'll focus on the most commonly used ones:

value: Scalar, dict, Series, or DataFrame. 
    The value to use to fill holes (e.g. 0). This is what we use in our solution.

method: {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}. 
    Method to use for filling holes in reindexed Series. Default is None.

axis: {0 or ‘index’, 1 or ‘columns’}. 
    Axis along which to fill missing values.

inplace: Bool. If True, fills in place. 
    Note: this will modify any other views on this object. Default is False.

Intuition
In our solution, we use:
products['quantity'].fillna(0, inplace=True)
'''
coffee.fillna(1000, inplace=True)
print(coffee.head())
coffee.loc[[0,1],'Units Sold'] = np.nan
coffee.fillna(coffee['Units Sold'].mean(),inplace=True) #fill giá trị trung bình
print(coffee.head())

#interpolate() điền giá trị NaN bằng nội suy
coffee.loc[[2,3],'Units Sold'] = np.nan
coffee.loc[1,'Units Sold'] = 15
coffee.loc[4,'Units Sold'] = 35
print(coffee.head())
coffee['Units Sold'] = coffee['Units Sold'].interpolate()
print(coffee.head())

#dropna()
'''
df.dropna(axis= , how= , thresh= , subset= , inplace= )
axis: Trục để loại bỏ giá trị thiếu. 0 hoặc 'index' (mặc định) để loại bỏ hàng, 1 hoặc 'columns' để loại bỏ cột.
how: Cách loại bỏ. Có hai giá trị chính:
    'any': Loại bỏ hàng hoặc cột nếu có bất kỳ giá trị thiếu nào (mặc định).
    'all': Loại bỏ hàng hoặc cột nếu tất cả các giá trị trong hàng hoặc cột đó là thiếu.
thresh: Số lượng giá trị không thiếu tối thiểu cần có trong hàng hoặc cột để không bị loại bỏ. Ví dụ, nếu bạn đặt thresh=2, hàng hoặc cột cần có ít nhất 2 giá trị không thiếu để giữ lại.
subset: Danh sách các cột hoặc hàng để kiểm tra giá trị thiếu. Nếu không chỉ định, hàm sẽ kiểm tra toàn bộ DataFrame.
inplace: Nếu True, thay đổi DataFrame/Series trực tiếp và không trả về bản sao mới. Mặc định là False.
'''
coffee.loc[[2,3],'Units Sold'] = np.nan
print(coffee.dropna(subset= ['Units Sold']).head())

#isna() và notna()
print(coffee[coffee['Units Sold'].isna()])
print(coffee[coffee['Units Sold'].notna()])
