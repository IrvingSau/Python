a = 1
b = a
c = 1
d = 1.0

id(a)
id(b)
id(c)
id(d)
# abc的值相等，并且abc的地址相等

if a == b:
	print("The value between a and b are equal")
if a == c:
	print("The value between a and c are equal")
if c is b:
	print("The address between c and b are equal")
if c is not d:
	print("The address between c and d are not equal")