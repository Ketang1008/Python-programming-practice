myDict={
    "fast":"In a quick manner",
    "harry":"A Coder",
    "marks":[1,2,5],
    "anotherdict":{'harry':'Player'},
    1:2
}


#Dictionary methods
print(list(myDict.keys())) #prints the keys of the dictionary
print(myDict.values())     #prints the values of the dictionary
print(myDict.items())     #prints the (key,value) for all contents of the dictionary
print(myDict)
updateDict={
    "Lovish":"friend",
    "Divya":"Friend",
    "Shubham":"friend"
    }
myDict.update(updateDict)  #Updates the dictionary by adding key values pairs from the  updateDict
print(myDict)




