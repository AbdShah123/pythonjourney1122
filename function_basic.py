def greet():
    print("hello world!")
    print("this is python")
    
    
greet()
#second program 
def greet2(first_name, last_name):                   # these are called perimeters written inside the parenthesis 
    print(f"Hi {first_name} and {last_name} in the tutorial of programming languages ")
    
    
greet2("Ahmed","Rizvi")  #these are called arguments written inside the function variable
greet2("lucy", "jackal") #now the function can be reuseable over and over again you don't have to write entire line of code

def greet3(*args):         # here *args stands for argument collector it collects all the argument and print it alongside the function
    print("hello world ", args)        
    

greet3("this is me ")
# let's say in second scenerio you're collecting alot of keys for your program then you will use kwarg statement to pass multiple keybase argument
def greet4(*args, **kwargs):
    print("hello there", args,kwargs)
    
    
greet4("nice to meet you","apples","mango",123,key=123,wine="ver2.45")
