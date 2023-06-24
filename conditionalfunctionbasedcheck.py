def condtion():
   while True:
    statement1=int(input("Please input the first number: "))
    statement2=int(input("Please input the second number: "))
    if statement1>statement2:
       print(f"{statement1} is the bigger one")
    else:
       print(f"{statement2} is the bigger one")
    c=input("do you want to perfom the calculation again (Y/N) :")
    if c=='N' or c=='n':
            break
       
condtion()