import pandas as pd
data = pd.DataFrame({
    'city': ['Jacksonville','Jacksonville','Jacksonville','Jacksonville','Jacksonville',
             'ElPaso','ElPaso','ElPaso','ElPaso','ElPaso'],
    'month': ['January','February','March','April','May',
              'January','February','March','April','May'],
    'temperature': [13,23,38,5,34,20,6,26,2,43]
})
print(data.head())
'''
pivot: tái cấu trúc bảng dữ liệu, từ dạng dài thành dạng rộng
function: DataFrame.pivot(index='', columns='', values='')
    index: đánh index bảng mới bằng các dữ liệu khác nhau trong bảng cũ
    columns: đặt tên cột bảng mới bằng các dữ liệu khác nhau trong bảng cũ
    values: giá trị ô trong bảng mới tương ứng
'''
data_clean = data.pivot(index='month', columns='city', values='temperature')
print(data_clean.head())
data_clean = data_clean.reindex(['January','February','March','April','May'])
print(data_clean.head())