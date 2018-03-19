# List的删除
List1 = [0, 1, 2, 3, 4, 5, 6]

#输出List中最后一个元素，类似于Stack中的pop()
print(List1.pop())
print(List1)

#删除List中最后一个元素, 此处由于之前6被pop出了，所以最后元素的index为5
del List1[5]
print(List1)

#从左找删除第一个指定的元素 - 0
List1.remove(0)
print(List1)

#对List进行排序
List1.insert(3, 90)
List1.insert(5,56)
print(List1)
List1.sort()
print(List1)

#对List反转
List1.reverse()
print(List1)

#拷贝列表
List2 = List1.copy()
print(List2)

#清空列表
List1.clear()
print(List1)

#通过子函数求List中元素的绝对值
def absList(List):
    for i in range(len(List)):
        if List[i] < 0:
            List[i] = List[i] * -1
    return List

List2 = [1, -2, -3]

print(absList(List2))