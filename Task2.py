def abs(number):
	if number >= 0:
		return number;
	else:
		return number * -1;

number = input("Enter a floating-point number: ")
number = float(number)
print("The absolute value of %f is %f" % (number, abs(number)))