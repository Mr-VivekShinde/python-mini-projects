#Temperature_Converter

print("Slect your conversion type \n 1) C <-> K \n 2) C <-> F \n 3) F <-> K")
type= int(input("Enter your conversion type (1,2 or 3) : "))

if (type==1):
    print("select \n a) C to K \n b) K to C")
    unit=input('Enter you preference (a or b) :')
    if (unit == "a"):
        C=float(input("Enter value in degree celcius:"))
        K = round((C + 273.15),3)
        print(f"{C} C = {K} K")
    elif (unit=="b"):
        K=float(input("Enter value in kelvin:"))
        C = round((K - 273.15),3)
        print(f"{K} K = {C} C")
    else:
        print("invalid selection, select a or b")


elif (type==2):
    print("select \n a) C to F \n b) F to C")
    unit=input('Enter you preference (a or b) :')
    if (unit == "a"):
        C=float(input("Enter value in degree celcius:"))
        F = round((C*(9/5) + 32),3)
        print(f"{C} C = {F} F")
    elif (unit=="b"):
        F=float(input("Enter value in degree Fahrenheit:"))
        C = round(((F-32)*(5/9)),3)
        print(f"{F} F = {C} C")
    else:
        print("invalid selection, select a or b")


elif (type==3):
    print("select \n a) K to F \n b) F to K")
    unit=input('Enter you preference (a or b) :')
    if (unit == "a"):
        K=float(input("Enter value in kelvin:"))
        F = round(((K-273.15)*(9/5) + 32),3)
        print(f"{K} K = {F} F")
    elif (unit=="b"):
        F=float(input("Enter value in degree Fahrenheit:"))
        K = round(((F-32)*(5/9)+273.15),3)
        print(f"{F} F = {K} K")
    else:
        print("invalid selection, select a or b")

else:
    print("invalid selection, select 1,2 or 3 ")