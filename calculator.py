print(" welcome to calculator app ")
Num1=float(input("Enter first number " ))  
operation=input("choose an operation (+ , - , * , / , % ) : ")
Num2=float(input("Enter second number "))
if operation=="+":
    result=Num1+Num2
    print (Num1, "+",Num2, "= " , result)
elif operation=="-":
    result=Num1-Num2
    print(Num1, "-" , Num2, "= ", result)    
elif operation=="*":
    result=Num1*Num2
    print(Num1, "*", Num2, "= ", result)
elif operation=="/":    # 10/0
    if Num2 !=0:
       result=(Num1/Num2)
       print(Num1, "/", Num2, "= ", result)
    else:
        print("can't division by zero")
elif operation=="%":
    result=(Num1%Num2)
    print(Num1, "%", Num2, "= ", result)
else:
    print("sorry , invalid operation " ,operation) 