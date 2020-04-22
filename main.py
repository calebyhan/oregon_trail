import random
import time

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y

def prob_theft(money, food):
    answer = ""
    if money >= 1000:
        rint = random.randint(1, 5)
        if rint == 1:
            answer = "$100 was stolen."
    elif (money > 500) and (money < 1000):
        rint = random.randint(1, 7)
        if rint == 1:
            answer = "$75 was stolen."
    else:
        rint = random.randint(1, 10)
        if rint == 1:
            answer = "$50 was stolen."
    return answer

running = True
money = 6000
while running == True:
    print("OREGON TRAIL")
    time.sleep(1)
    print("By Ocra004, Shadowfax13, Ripsticker321, LJCoder619")
    time.sleep(1)
    print("Copyright 2020")
    time.sleep(1)
    print("Loading....")
    time.sleep(2)
    print("Welcome to the Oregon Trail!")

    start_loop = True
    while start_loop == True:
        start = input("Would you like to 1: Play or 2: leave? ")
        if start == "1":
            print("Let's get started!")
            start_loop = False
        elif start == "2":
            start_loop = False
            running = False
        else:
            print("I do not recognise {}. Please try again.".format(start))
    shop = True
    while shop == True:
        print("Welcome to Bob's Hardware shop! Select what you want to buy.")
        print("1. Yokes of oxen (150 dollars each)")
        print("2.Food (1 dollar per pound)")
        print("3.Ammunition (2 dollars per box)")
        print("4.Clothing (5 dollars per set)")
        print("5.Spare Parts (10 dollars each)")
        print('Enter "." to leave.')
        shop_choice = input("What is your choice?:")
        oxen_choice = True
        food_choice = True
        ammo_choice = True
        if shop_choice == ".":
            shop = False
        elif shop_choice == "1":
            while oxen_choice == True:
                oxen = int(input("How many yokes would you like to buy?(3 max) "))
                if oxen > 4:
                    print("Enter a positive value less than 4.")
                else:
                    print("You purchased {} oxen.".format(oxen))
                    money = money - (oxen*150)
                    oxen_choice = False
        elif shop_choice == "2":
            while food_choice == True:
                food = int(input("How many pounds of food would you like to buy?(2000 max) "))
                if food > 2000:
                    print("Enter a positive value less than 2000.")
                else:
                    print("You purchased {} pounds of food.".format(food))
                    money = money - (food*1)
                    food_choice = False
        elif shop_choice == "3":
            while ammo_choice == True:
                ammo = int(input("How many boxes of ammunition would you like to buy?(100 max) "))
                if ammo > 100:
                    print("Enter a positive value less than 100.")
                else:
                    print("You purchased {} pounds of food.".format(ammo))
                    money = money - (ammo*2)
                    ammo_choice = False


# amount_1 = 0
# amount_2 = 0
# print('Welcome!')
# print('Would you like to:')
# print("1. Play the game")
# print("2. Leave")
# choice = input("Enter choice(1/2): ")
#
# if choice == '1':
#     print("Nice!")
#     print("Now lets get started!")
#     print("Let's go to the shop to buy supplies!")
# choice = input("Let's go!(y/n):")
# if choice == 'y':
#     amount = subtract(6000, amount_1)
#     print("Bob's Hard ware store")
#     print("What would you like to buy?")
#     print("1.Yokes of Oxen (150 dollars each)")
#     print("2.Food (1 dollar per pound)")
#     print("3.Ammunition (2 dollars per box)")
#     print("4.Clothing (5 dollars per set)")
#     print("5.Spare Parts (10 dollars each)")
#     print("Press Enter to Leave")
#     print("You have", amount, "dollars to spend")
#     i = input("Enter the number(1/2/3/4/5:)")
# if choice == "1":
#     print("How many yokes would you like to buy?(3 max)")
# choice = input()
# if choice == '1':
#     print("Sure")
#     print("amount due is 150 dollars")
#     amount_1 = 150
# if choice == '2':
#     print("Sure")
#     print("amount due is 300 dollars")
#     amount_1 = 300
# if choice == '3':
#     print("Sure")
#     print("amount due is 450 dollars")
# else:
#     print("Sorry you can only carry (at max) 3 yokes")
# if choice == '2':
#     print("How many pounds do you want?(1950,2000 max)")
#     choice = input()
# if choice == '1950':
#     print("You might need more!")
#     amount_2 = 1950
#
# if choice == '2000':
#     print("You might need more!")
#     print(add(num1, num2))
#     amount_2 = 2000
# if choice == '3':
#     print("ok")
# if choice == '4':
#     print("ok")
# if choice == '5':
#     print("ok")
#
# if choice == 'n':
#     print("Bye!")
#
# if choice == '2':
#     print("Bye!")
#
# running = True
# while running == True:
