x="variable 1"     # a test case program to acess global variable program that exist outside the main loop
def my_function():
    print("This is my function "+x)
my_function()
# As you can see from the output a global variable can be acccessed outside the main program let's take more
# practical approch
# before digging deeper let's see what local variable actually are look closely
y="2nd variable"
def my_function_2():
    y="johnson"
    print(f"Hello there {y} nice to meet you ")
my_function_2()
print(f"this is my {y} program ")
# as you can see that variable within inside the local program wasn't acessed instead a global variable was 
# acessed

