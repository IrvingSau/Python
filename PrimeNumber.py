def isPN(x):
    for i in range(2, int(x / 2)):
        if x % i == 0:
            return 0;
    else:
        return 1;

list1 = [32, 41, 23, 33, 18, 29, 7, 14, 76, 37, 21]

for i in list1:
    if(isPN(i)):
        print(i)