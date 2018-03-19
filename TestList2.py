#创建列表

#方法一, 列表名 = [元素1，元素2...元素n]
List1 = [1, 2, 3]
List2 = ["Irving", "Anbul"]

print(List1)
print(List2)

#方法二， 列表名 = list(), 相当于构建一个对象

List3 = list()

for i in range(5):
    temp = int(input("Please input the element for List3: "))
    List3.append(temp)

print(List3)

#查询列表

List4 = [1, 1, 2, 2, 3, 3]

print(List4)

print("First 2 index in List4 is ", List4.index(2)) #查询2在这个列表中的index
print("There are ", List4.count(2), " 2 in the list4") #计算2这个元素在列表中出现的次数

