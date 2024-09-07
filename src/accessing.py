import pandas as pd
coffee = pd.read_csv('coffee.csv')
print(coffee) #In ra toàn bộ file
#head()
print(coffee.head()) #In ra 5 dòng đầu
print(coffee.head(10)) #In ra 10 dòng đầu
#tail()
print(coffee.tail()) #In ra 5 dòng cuối
print(coffee.tail(10)) #In ra 10 dòng cuối
#sample()
print(coffee.sample(5)) #In ngẫu nhiên 5 dòng
#loc[[row],[column]]
print(coffee.loc[0])    #In ra thông tin dòng đầu tiên
print(coffee.loc[[0]])  #In ra dòng đầu tiên
print(coffee.loc[0:3])  #In ra thông tin từ dòng 1 đến dòng 3
print(coffee.loc[0:5,["Day","Units Sold"]])
#iloc -> loc theo index
print(coffee.iloc[0:5,1:3])
coffee.index = coffee.Day #Thay đổi index theo ngày
print(coffee)
#print(coffee.loc[0:5]) -> lỗi do index hàng bây giờ đã theo ngày
print(coffee.loc["Monday"])
print(coffee.loc["Monday":"Wednesday"])
print(coffee.iloc[0:5,1:])