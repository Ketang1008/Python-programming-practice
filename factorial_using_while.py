num=int(input("Enter the number:"))
i=1
factorial=1
while(i<=num):

    factorial=factorial*i
    i=i+1
print("The factorial of {} is {}".format(num,factorial))