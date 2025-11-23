# ARITHMATIC CALCULATOR (for two numbers)

operator=input("Enter an Operator (+,-,/,*,%,//) : ")
num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))

if (operator == "+"):
    r=(round(num1+num2),3)
    print(f"result : {r}")
elif(operator == "-"):
    r=(round((num1-num2),3))
    print(f"result : {r}")
elif(operator == "*"):
    r=(round((num1*num2),3)) 
    print(f"result : {r}")
elif(operator == "/"):
    r=(round((num1/num2),3))
    print(f"result : {r}")
elif(operator == "//"):
    r=(round((num1//num2),3))
    print(f"result : {r}")
elif (operator == "%"):
    r=(round((num1%num2),3))
    print(f"result : {r}")
elif (operator == "**"):
    r=(round((num1**num2),3))
    print(f"result : {r}")

else:
    print("Error!, Select valid operator")