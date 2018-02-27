# Try to use the list in Python
# Author: IrvingSau
# Date: 2018/2/27

amount = input("How many floating point numbers do you want to multiply together: ")
amount = int(amount)

result = 1

a = [0 for x in range(0, amount)]# Create a list whose length is amount inputed by user and is fill with 0;

for i in range(0, len(a)):
	a[i] = float(input("Enter a floating point number: ")) 
	result = result * a[i]

print("The product is %f" % (result))