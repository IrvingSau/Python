#Date: 2018/2/19
#Author: IrvingSau
#Purpose: Judege if a year is leap year（闰年）

b = 2016

# str = input("请输入：");
# print ("你输入的内容是: ", str)

if(b % 4 == 0 and b > 0):
	print("this year is leap year")
else:
	print("this year is not leap year")