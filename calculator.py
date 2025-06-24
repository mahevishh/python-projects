print("simpel CLI calculator")
num1=float(input("enter your first number"))
op=input("enter operator(+,-,*,/,%)")
num2=float(input("enter your second number"))
if op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=="*":
    result=num1*num2
elif op=="/":
    result=num1/num2
elif op=="%":
    result=num1%num2
else:
    print("invalid symbol")
print("result=", result);
