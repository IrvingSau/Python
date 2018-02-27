first = input("Enter the first integer: ")
first = int(first)
second = input("Enter the second integer: ")
second = int(second)

if (first < 0 and second < 0):
	print("The integer %d and %d are not both positive" % (first, second))
elif (first >= 0 and second >= 0):
	print("The integer %d and %d are both positive" % (first, second))