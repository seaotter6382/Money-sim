import time
import random

money = 0
start_money = 10

money = money + start_money
print("you have " + str(money) + " money")
time.sleep(0.5)
while True:
    print("how much money do you want to bet?")
    try:
        word = int(input())
    except ValueError as e:
        print("enter a number not a letter")
        continue
    if word > money:
        print("enter a number less than your money")
    if word <= money:
        print(word)
        break
