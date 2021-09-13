a=int(input("Enter the number :"))
print("The next number for the {} number is".format(a)),int(a+1)
print("The next number for the {} number is".format(a),int(a-1)



hour1=int(input())
hour2=int(input())
minute1=int(input())
minute2=int(input())
second1=int(input())
second2=int(input())
print(hour2*3600+minute2*60+second2-hour1*3600-minute1*60-second2)