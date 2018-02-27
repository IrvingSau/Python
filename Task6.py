months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

iMonth = int(input("Enter the month: "))
iDay = int(input("Enter the day: "))

result = 0

for i in range(0,iMonth - 1):
	result = result + months[i]

result = result + iDay

print("%d/%d is the day number %d in the year." % (iDay, iMonth, result))