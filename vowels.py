mylist=["Welcome","Ketan","Sam"]
a=0
e=0
i=0
o=0
u=0

for k in range(0,len(mylist)):
    vowels=0
    a=0
    e=0
    i=0
    o=0
    u=0
    print("number of vowels are :")
    for j in mylist[k]:
        
        if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
            vowels+=1
        if(j=='a'):
            a+=1
        if(j=='e'):
            e+=1
        if(j=='i'):
            i+=1
        if(j=='o'):
            o+=1
        if(j=='u'):
            u+=1
        if (j == 'A' or j == 'E' or j == 'I' or j == 'O' or j == 'U'):
            vowels += 1
        if (j == 'A'):
            a += 1
        if (j == 'E'):
            e += 1
        if (j == 'I'):
            i += 1
        if (j == 'O'):
            o += 1
        if (j == 'U'):
            u += 1
            
    print(vowels)
    print("a=",a)
    print("e=",e)
    print("i=",i)
    print("o=",o)
    print("u=",u)