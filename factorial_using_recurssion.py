def fact(n):
    if n==1 or n==0:       # Base condition
        return 1
    else:
        return n*fact(n-1)   

n=int(input("Enter the number whose factorial is to be calculated :"))

print("The factorial of {} is".format(n),n*fact(n-1))
