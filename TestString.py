str1 = "Hello Anubl"
print(str1)

#字符串不具有可变性
a = "Jack"
a = "Alex"
#实际上在内存中是新建了一块内存存放Alex，而非将Jack替换

#字符串的函数,可以按control进入源码查询

# 大小写互换
print(str1.swapcase())

# 返回一个首字母大写的版本
print(str1.capitalize())

# 统计这个字符串中某个字字符串出现的次数
print(str1.count("l", 0, 3))#可以用0, 3来规范查找范围


#统一输出小写
print(str1.casefold())

#Center
print(str1.center(50, '*'))

#查找一个值并且返回索引
print(str1.find('e'))

#format, 格式化输出，这里无所谓占位符，只用format中的参数代替了{0}, ...,{n}
str2 = "My name is {0}, my age is {1}"
print(str2.format('Turing', 18))
