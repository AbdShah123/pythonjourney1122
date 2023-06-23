var1="helloworld"
print(isinstance(var1, str))                     # to check the instance type by specifying the instance type within the code 
if var1==str(var1):
    print("the given variable is string type data") # similar to type() instance but produce result in the form of true or false
else:
    print("the given is integer type data")
# originally the reult is printed something like this
print(type(var1))