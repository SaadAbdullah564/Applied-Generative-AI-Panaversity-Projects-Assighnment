#PROJECT NO: 21
#Write a program which asks a user for their age and lets them know ..
#.. if they can or can't vote in the following three fictional countries...
#the voting age in Peturksbouipo is 16
#the voting age in Stanlau is 25 
#the voting age in Mayengua is 48 
user_age: int = int(input("Enter the age: "))
if user_age >= 16:
    print("You are elligeble to cast vote in Peturksbouipo")
else:
    print("You are not elligeble to cast vote in peturksbouipo")
if user_age >= 25:
    print("You are elligeble to cast vote in Stanlau")
else:
    print("You are not elligeble to cast vote in Stanlau")
if user_age >= 48:
    print("You are elligeble to cast vote in Mayengua")
else:
    print("You are not elligeble to cast vote in Mayengua")


#PROJECT NO: 22
#Write a program that reads a year from the user and tells whether a given year is a leap year or not.
#The given year must be evenly divisible by 4;
#If the year can also be evenly divided by 100, it is NOT a leap year; unless:
#The year is also evenly divisible by 400. Then it is a leap year.
year: int = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(" That year is leap")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year")
else:
    print(" it is not a leap year")


#PROJECT NO: 23
#Write a program which asks the user how tall they are and prints whether.. 
#.. or not they're taller than a pre-specified minimum height.
minimum_height: int = 50
user_height: int = int(input("Enter the height: "))
if user_height >= minimum_height:
    print("You are Tall enough to Ride")
else:
    print("You are not tall enough to Ride") 


#PROJECT NO: 24
#Print 10 random numbers in the range 1 to 100.
import random
random_numbers = [random.randint(1, 100) for i in range(10) ]
print("10 random numbers between 1 and 100:")
for number in random_numbers:
    print(number)


#PROJECT NO: 25
#This program counts the number of times each number appears in a list...
# ....It uses a dictionary to keep track of the information.
def count_occurrences(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return counts

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
occurrences = count_occurrences(my_list)
print(occurrences) 


#PROJECT NO: 26
#Write a program that loops through a dictionary of fruits,..
#  ..prompting the user to see how many of each fruit they want to buy,..
#  ..and then prints out the total combined cost of all of the fruits.
fruits: dict[int] = {
    "apple_per_kg" : 120 , 
    "mango_per_kg" : 80 ,
    "gava_per_kg" : 250 ,
    "strawberry_per_kg" : 140
}
total_cost_before_purschasing: int = 0
order_of_apple: int = int(input("enter amount of apple: "))
order_of_mango: int = int(input("enter amount of mango: "))
order_of_gava: int = int(input("enter amount of gava: "))
order_of_strawberry: int = int(input("enter amount of strawberry: "))
price: int = fruits
total_of_apple: int = price["apple_per_kg"] * order_of_apple
total_of_mango: int = price["mango_per_kg"] * order_of_mango
total_of_gava: int = price["gava_per_kg"] * order_of_gava
total_of_strawberry: int = price["strawberry_per_kg"] * order_of_strawberry
total_cost_after_purschasing: int = (total_of_apple + total_of_mango + total_of_gava + total_of_strawberry)
print(total_cost_after_purschasing)


#PROJECT NO: 27
# Write a python program which add 2 elements in a list
fruits: list[str] = ["Apple" , "Mango" , "Lychi" , "Banana"]
print(fruits)
fruits.append("Peach")
print(fruits)
fruits.append("Pineapple")
print(fruits)


#PROJECT NO: 28
#Write a program which can be able to differ you on the basis of your age.
age : int = int(input("Enter the age: "))
if age <= 15:
    print("You are kid.")
elif age <= 25:
    print("You are teenager.")
elif age <= 45:
    print("You are adult.")
elif age > 45:
    print("You are a senior citizen.")


#PROJECT NO: 29
#write a python program to print the table of any number of user choice.
num: int = int(input("Enter num whose table you want to get: "))
count: int = 1
while count <= 10:
    print(f"{num} * {count} = " , num * count)
    count = count + 1


#Project no: 30
#write a python program which can add the square of two numbers of users choice.
num_1: int = int(input("enter the number 1: "))
num_2: int = int(input("enter the number 2: "))
def add_squares():
    result: int =  (num_1 ** 2 ) + (num_2 ** 2)
    print(result)
add_squares()