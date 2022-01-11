import random
import time

num1 = random.randrange(200)
num2 = random.randrange(200)

if num1 > num2:
    higher_num = num1
else:
    higher_num = num2

guess = input(
    f"The random numbers generated are: {num1} and {num2}. Which number is higher? "
)

guess = int(guess)
while guess:
    if guess == higher_num:
        print("Good job, you got it!!!")
        time.sleep(1)
    else:
        print("try again!")
        time.sleep(1)
