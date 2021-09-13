def sum(n):
    if n<=1:   #base condition
        return 1
    else:
        return n+sum(n-1)

n=int(input("Enter the value of n :"))
print("The sum of first {} natural numbers is {}".format(n,sum(n)))
