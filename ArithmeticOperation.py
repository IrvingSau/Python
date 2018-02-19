#Date: 2018/2/19
#Author: IrvingSau
#Purpose: Try some python

#引入模块
import math

#dir函数查看模块中的内容
dir(math)

print("This is some arithmetirc operation:")
print("2的3次方是")
print(2**3)
print("2的三次方是(使用math中的pow()函数)", pow(2, 3))
#python 支持次方运算 运算符为**

print("除法测试")
print("2/3=")
print(2/3)
print("3/2=")
print(3/2)
#在python3中和Java与C不同，除法中不会直接取整

print("Type Change in Python: ")
print("abc * 3 =", abc*3)
print("2/0.5=", 2/0.5)

a = 10
b = 25
c = 30

print("b/a并且取整除：", b//a)

#if语句结构示例:
'''if(condition):
	statement;
else if():
	statement;'''
if(a != b):
	print('a=',10,"和",'b=', 25,"是不相等的")
else:
	print("a和b是相等的")
