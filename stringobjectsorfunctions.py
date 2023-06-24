# now we will learn string object in python
string_1='HelloWorld'
string_1.upper()             #if I print this it'll return me the result in the upper case and vice versa 
# now let's print this result in upper case
print(string_1.upper())    #similarly performing operations like this one
print(string_1.split(","))    #presummely just split the words nothing uncommmon rigth over here 
print(string_1.format())
width=10
print(string_1.center(width))
print(string_1.ljust(width))
print(string_1.casefold())        #doesn't change the original string only return a new string
print(string_1.find('H'))         #finding the specific elemant based on the index number of an elemant
print(string_1.replace('World',' Hell'))    #replacing the word based upon the specified variable or string object text