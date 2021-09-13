sub1=int(input("Enter the marks of first subject :"))
sub2=int(input("Enter the marks of second subject :"))
sub3=int(input("Enter the marks of third subject :"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")

elif(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage less than 40")

else:
    print("Congratulations ! , you are pass" )

