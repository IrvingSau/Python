def array_abs(array):
	for i in range(0, len(a)):
		if(array[i] < 0):
			array[i] = array[i] * -1
	return array;

a = [0 for x in range(0 , 5)]

for j in range(0, 5):
	a[j] = float(input("Enter a floating number: "))

array_abs(a)

print("The result is ", a)