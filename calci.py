while(True):
    n1=int(input("Enter a number:"))
    n2=int(input("Enter another number:"))
    print("+    -> Addition")
    print("-    -> Subtraction")
    print("*    -> Multiplication")
    print("/    -> Division")
    op=input("Enter any operator from the choice given above:")
    if(op=="+"):
        print("---------------")
        print(n1,"+",n2,"=",n1+n2)
        print("---------------")
        print("Result:\t",n1+n2)
    elif(op=="-"):
        print("---------------")
        print(n1,"-",n2,"=",n1-n2)
        print("---------------")
        print("Result:\t",n1-n2)
    elif(op=="*"):
        print("---------------")
        print(n1,"*",n2,"=",n1*n2)
        print("---------------")
        print("Result:\t",n1*n2)
    elif(op=="/"):
        if(n2!=0):
            print("---------------")
            print(n1,"/",n2,"=",n1/n2)
            print("---------------")
            print("Result:\t",n1/n2)
        else:
            print("Division by zero is not possible")
    a=input("Do you want to continue(y/n):")
    if(a=='n'):
        break
    
