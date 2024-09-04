import pandas as pd

#DataFrame
df1 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print("df1:")
print(df1.head())

#Shape,size
print("df1 shape:")
print(df1.shape)
print("df1 size:")
print(df1.size)

#Đặt tên cột
df2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"], index=["x","y","z"])
print("df2:")
print(df2.head())

#In ra n dòng đầu tiên -> truyền tham số n vào head()
print("df1 head:")
print(df1.head(1))
print("df2 head:")
print(df2.head(2))

#In ra n dòng cuối -> truyền tham số n vào tail()
print("df1 tail:")
print(df1.tail(1))
print("df2 tail:")
print(df2.tail(2))

#Xem tên cột
print("df1.columns:")
print(df1.columns) #chưa có tên cột
print("df2.columns:")
print(df2.columns)

#Xem index (hàng)
print("df1.index:")
print(df1.index)
print("df2.index:")
print(df2.index.tolist()) #tolist()

#Xem info
print("df1.info():")
print(df1.info())
print("df2.info():")
print(df2.info())

#Describe
'''
count: số lượng giá trị không rỗng
mean: trung bình cộng
std: độ lệch chuẩn
min: giá trị nhỏ nhất
25%: phân vị thứ nhất: Giá trị mà 25% số liệu trong cột nhỏ hơn hoặc bằng nó.
50%: trung vị (med)
75%: phân vị thứ ba: Giá trị mà 75% số liệu trong cột nhỏ hơn hoặc bằng nó
max: giá trị lớn nhất
'''
print("Desribe df1:")
print(df1.describe())

#Unique
#Số giá trị khác nhau ở mỗi cột:
print(df1.nunique())
#Liệt kê giá trị khác nhau ở một cột:
print(df2["A"].unique())
