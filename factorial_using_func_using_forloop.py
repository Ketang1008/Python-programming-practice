def fact(n):
    product=1
    
    for i in range(1,n+1):
        product=product * i
    return product

n=int(input("Enter the number whose factorial is to be calculated :"))
print(fact(n))
