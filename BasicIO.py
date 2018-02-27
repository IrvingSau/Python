# Test the basic IO
a = 1
id(a)

name = input("What is your name ")

age = input("What is your age ")
age = int(age)
#Python中输入默认保存为字符串格式，如果要转换为int或者float需要用int(), float()

print("Your name is", name, ", and your age is %d" % (age))