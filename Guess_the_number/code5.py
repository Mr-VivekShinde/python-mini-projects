#GUESS_THE_NUMBER:

print("You get a 7 chance to guess a number between (1,100):")
import random
num=random.randint(1,100)
user_num=int(input("Guess an integer between 1 to 100 : "))
while user_num!=num:
    for i in range(6,0,-1):
        if (user_num > num):
            print("Your guess is bigger than the actual number.\n")
            print(f"remaing chances:{i}")
            user_num=int(input("Guess an integer between 1 to 100 : "))
        elif (user_num < num):
            print("Your guess is smaller than the actual number.\n")
            print(f"remaing chances:{i}")
            user_num=int(input("Guess an integer between 1 to 100 : "))
print("Congrats! You have guessed it right.")         

    
    
