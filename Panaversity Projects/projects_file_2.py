#PROJECT NO: 11
#Simulate rolling two dice, and prints results of each roll as well as the total.
import random
num_sides: int = 6
die_1: int = random.randint(1,num_sides)
die_2: int = random.randint(1,num_sides)
total: int = die_1 + die_2
print(f"Die have {num_sides} sides each")
print(f"First die: {die_1}")
print(f"Second die: {die_2}")
print(f"Total of two dice: {total}" )


#PROJECT NO: 12
#Use Python to calculate the number of seconds in a year,  and tell the user what the result is in a nice ..
# ..print statement that looks like this (of course the value 5 should be the calculated number instead):
num_of_days: int = 365
num_of_hours_in_day: int = 24
num_of_minutes_in_hour: int = 60
num_of_seconds_in_minutes: int = 60
num_of_seconds_in_year: int = num_of_days * num_of_hours_in_day * num_of_minutes_in_hour * num_of_seconds_in_minutes
print(f"There are {num_of_seconds_in_year} seconds in an Year")


#PROJECT NO: 13
#Write a program which prompts the user for an adjective,...
# .. then a noun, then a verb, and then prints a fun sentence with those words!
adjective: str = str(input("Enter adjective: "))
noun: str = str(input("Enter noun: "))
verb: str = str(input("Enter verb: "))
print(f"{noun} is {verb} {adjective}")


#PROJECT NO: 14
#Write a function that takes a list of numbers and returns the sum of those numbers
def add_numbers():
    numbers: list[int] = [ 34, 23, 12, 98, 45]
    sum_numbers: int = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
    print(sum_numbers)
add_numbers()


#PROJECT NO: 15
#Write a program that doubles each element in a list of numbers. For example, if you start with this list:
numbers: list[int] = [1,2,3,4]
for i in range(len(numbers)):
    element_at_index = numbers[i]
    numbers[i] = element_at_index * 2
print(numbers)


#PROJECT NO: 16
#Add three copies of a message to the list
def add_three_copies(my_list,data):
    for i in range(3):
        my_list.append(data)
data: str = str(input(" Enter the message to Copy: "))
my_list: list = []
print(f" List before: {my_list}")
add_three_copies(my_list , data)
print(f"List after : {my_list}")


#PROJECT NO: 17
#Fill out the function get_first_element(lst) which takes in a list lst as a parameter and.. 
# ..prints the first element in the list. The list is guaranteed to be non-empty...
#  ...We've written some code for you which prompts the user to input the list one element at a time.
my_list: list[int] = [4,5,6,7,8]
get_first_number: int = int(input("Enter the first number of list:  "))
my_list.insert(0,get_first_number)
print(my_list)


#PROJECT NO: 18
#write a program which adds the number at the last of the list
list_number: list[int] = [2,4,6,8,10]
get_last_number: int = int(input("Enter the last number of list:  "))
my_list.append(get_last_number)
print(my_list)


#PROJECT NO: 19
#Write a program which continuously asks the user to enter values which ...
#... are added one by one into a list. When the user presses enter without typing anything, print the list.
value_number_1: str = str(input("Enter first value: "))
value_number_2: str = str(input("Enter second value: "))
value_number_3: str = str(input("Enter third value: "))
values_list: list[str] = [(value_number_1) , (value_number_2) , (value_number_3)]
print(values_list)


#PROJECT NO: 20
#Write a program that prints the first 20 even numbers..
# ..There are several correct approaches, but they all use a loop of some sort..
# .. Do no write twenty print statements
def show_evens():
    for i in range(20):
        print( i * 2)
show_evens()
