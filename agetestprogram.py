def age():
    while True:
        is_age=int(input("Input your age: "))
        if is_age>18:
                print("you're older")
        else:
            print("you're younger")
        c=input("Do you want to perform the calculation again(Y/n): ")
        if c=='N' or c=='n':
            break
 

age()