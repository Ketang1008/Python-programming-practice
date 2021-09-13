a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third  number :"))
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0) 


