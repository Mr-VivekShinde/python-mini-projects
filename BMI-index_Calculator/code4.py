#BMI-index_Calculator

def calc_BMI(BMI):
    if(BMI<18.5):
        print("You falls into the Underweight category.\n")
    elif(BMI>=18.5 and BMI<=24.9):
        print("Congratulations! You falls into the Normalweight category.\n")
    elif(BMI>=25.0 and BMI<=29.9):
        print("You falls into the Overweight category.\n")
    elif(BMI>=30.0 and BMI<=39.9):
        print("You falls into the Obese category.\n")
    elif(BMI>=40):
        print("You falls into the Mobidly Obese category.\n")
    else:
        print("\nError! invalid input \n")
    print("NOTE: You can check once again. Dont forget to use proper unit value")


weight=float(input("Enter your weight :"))
wt_unit=input("Enter unit for given weight(K = kilogram or L =pounds) :")
wt_unit=wt_unit.lower()

if (wt_unit =="k"):
    user_height=float(input("\nEnter your height :"))
    ht_unit=input("Enter unit for given height (cm, m or ft) :")
    if (ht_unit=="cm"):
        height=(user_height/100)
    elif(ht_unit=="ft"):
        height=(user_height*0.3)
    elif (ht_unit=="m"):
        height=user_height
    else:
        print("\nError! invalid height unit\n")

    BMI=(weight/(height**2))
    print(f"\nYour BMI-index is : {round(BMI,2)}")
    calc_BMI(BMI)

elif (wt_unit =="l"):
    weight=weight*2.205
    user_height=float(input("\nEnter your height :"))
    ht_unit=input("Enter unit for given height (cm, m or ft)  :")
    if (ht_unit=="cm"):
        height=(user_height/100)
    elif(ht_unit=="ft"):
        height=(user_height*0.3)
    elif (ht_unit=="m"):
        height=user_height
    else:
        print("\nError! invalid height unit\n")

    BMI=(weight/(height**2))
    print(f"\nYour BMI-index is : {round(BMI,2)}")
    calc_BMI(BMI)

else:
    print("Error! invalid input")


