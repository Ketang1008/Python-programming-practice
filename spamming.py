text=input("Enter the text\n")


if("make a lot of money\n" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this"):
    spam=True
elif("subscribe this"):
    spam=True
else:
    spam=False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")