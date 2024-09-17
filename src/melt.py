import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Mary'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 85]
})

print(df)
'''
melt function: dùng để biến đổi bảng dữ liệu từ dạng rộng thành dạng dài
pd.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name="value", col_level=None, ignore_index=True)
    id_vars: id cột mới, giá trị của cột này sẽ không thay đổi so với cột cũ
    value_vars: biến giá trị, hiểu đơn giản là tên các cột cũ được làm dọc
    var_name: tên cột mới của cột bao gồm value_vars
    value_name: tên cột mới của cột chứa giá trị tương ứng
'''
data_long = pd.melt(df, id_vars='Name', value_vars=['Math','Science'], var_name='Subject', value_name='Score')
print(data_long)