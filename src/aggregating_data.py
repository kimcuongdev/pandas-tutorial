import pandas as pd
import numpy as np
bios = pd.read_csv('bios.csv')
coffee = pd.read_csv('coffee.csv')
coffee['price'] = 1.23
coffee['new_price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99,coffee['price'])
coffee.drop(columns=['price'],inplace=True)
coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']
coffee.rename(columns={'new_price':'price'}, inplace=True)
print(bios.head())

#value_counts()
print(bios['born_city'].value_counts())
print(bios[bios['born_country'] == "USA"]['born_city'].value_counts())
print(bios[bios['born_country'] == "USA"]['born_region'].value_counts().tail())

#groupby()
'''
Hàm groupby() trong pandas được sử dụng để nhóm dữ liệu trong DataFrame hoặc 
theo một hoặc nhiều cột. Sau khi nhóm dữ liệu, bạn có thể thực hiện 
các phép toán thống kê hoặc các phép toán khác trên từng nhóm. 
Cú pháp:
DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, observed=False, dropna=True)
Các tham số chính:
by: Tên cột hoặc danh sách các cột để nhóm dữ liệu theo. Có thể là tên cột, danh sách cột, hoặc hàm.
axis: Trục để nhóm. Mặc định là 0 (dọc theo các hàng).
level: Nếu nhóm theo các cấp trong chỉ số đa cấp (MultiIndex), chỉ định cấp nhóm.
as_index: Nếu True (mặc định), cột nhóm sẽ trở thành chỉ số. Nếu False, cột nhóm sẽ không trở thành chỉ số.
sort: Nếu True (mặc định), nhóm sẽ được sắp xếp theo giá trị nhóm. Nếu False, nhóm không được sắp xếp.
group_keys: Nếu True (mặc định), các khóa nhóm sẽ được thêm vào chỉ số của DataFrame trả về.
observed: Nếu True, chỉ các giá trị đã xuất hiện trong nhóm sẽ được ghi nhận (chỉ áp dụng cho các nhóm với biến phân loại).
dropna: Nếu True (mặc định), nhóm sẽ loại bỏ các giá trị NaN. Nếu False, nhóm sẽ giữ lại giá trị NaN.
'''
print(coffee.groupby(['Coffee Type'])['Units Sold'].sum())
print(coffee.groupby(['Coffee Type']).agg({'Units Sold': 'sum','price':'mean'}))
df = pd.DataFrame({
    'Department': ['HR', 'IT', 'HR', 'IT', 'IT', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [50000, 60000, 55000, 70000, 65000, 52000]
})

