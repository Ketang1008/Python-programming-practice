# Use open function to read the contents of a file !
f=open('sample.txt','r') #by default the mode is r
data=f.read()
print(data)
f.close() 