# assignment operator 
a=3
var="this is variable 2"
print(f"this is( {a} )which is var 1 and this is( {var} )which is variable 2 you can see that in code ")
# arthematic operator 
# let's take an example of a calculator program and futhur understand the working of the program
d=input("please input any operator (+,/,*,%): ")
if d=='+':
    b=float(input("please input first number: "))
    c=float(input("please input Second number: "))
    result=b+c
    print("your Answer: "+str(result))
elif d=='-':
    b=float(input("please input first number: "))
    c=float(input("please input Second number: "))
    result=b-c
    print("your Answer: "+str(result))
elif d=='*':
    b=float(input("please input first number: "))
    c=float(input("please input Second number: "))
    result=b*c
    print("your Answer:"+str(result))
elif d=='/':
    b=float(input("please input first number: "))
    c=float(input("please input Second number: "))
    result=b/c
    print("your Answer:"+str(result))
elif d=='%':
    b=float(input("please input first number: "))
    c=float(input("please input Second number: "))
    result=b%c
    print("your Answer:"+str(result))
else:
    print("please re-enter your choices once again")
