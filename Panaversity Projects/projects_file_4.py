#PROJECT NO: 31
# Write a function that takes two numbers and finds the average between the two.
def take_average():
    num_1: int = int(input("Enter the num_1: "))
    num_2: int = int(input("Enter the num_2: "))
    average: int = (num_1  + num_2) / 2
    print(average)
take_average()


#PROJECT NO: 32
# Write a program which print 1 to 10 countings
def count_numbers():
    for i in range(10):
        curr_num = i + 1
        print(curr_num)
print("Let's count until 10 and see who will reach first.")
count_numbers()
print("I have Done. ")


#PROJECT NO: 33
# Write a python program which prints the table of 2
for i in range(1,  10 ):
    print(F"  2 * {i} = {i * 2 }")
    i = i + 1


#PROJECT NO: 34
# Write a python program which says 100 time sorry to my Friend
friend_name: str = str(input("Enter  friend name: "))
for i in range(1,100):
    print(f"I am Sorry!. Dear {friend_name}")
    i = i + 1


#PROJECT NO: 35
# prints the number of even numbers in the list
def find_evens():
    my_list = []
    x: int = int(input("enter x: "))
    y: int = int(input("enter y: "))
    z: int = int(input("enter z: "))
    if x % 2 == 0 :
        my_list.append(x)
    else:
        print(f"{x} it is not even")
    if y % 2 == 0 :
        my_list.append(y)
    else:
        print(f"{y} it is not even")
    if z % 2 == 0 :
        my_list.append(z)
    else:
        print(f"{z} it is not even")
    print(my_list)
find_evens()


#PROJECT NO: 36
# Fill out the double(num) function to return the result of multiplying num by 2.
#  We've written a main() function for you which asks the user for a number, 
# calls your code for double(num) , and prints the result.
num: int = int(input("enter the num: "))
num_double: int = num * 2 
result: int = num_double
print(f"The double of {num} is {num_double}")


#PROJECT NO: 37
# Fill out the get_name() function to return your name as a string! 
user_name: str = str(input("Enter your name: "))
def get_name():
    return user_name
def main():
    name: str = get_name()
    print("Hello" , name , "!")
main()


#PROJECT NO: 38
#Write a program which finds 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd.
nums: list = [10,11,12,13,14,15,16,17,18,19]
odd_nums: list = []
even_nums: list = []
for num in nums:
    if num % 2 != 0:
        odd_nums.append(num)
    else:
        even_nums.append(num)
print(f"Odds: {odd_nums}")
print(f"Evens: {even_nums}")


#PROJECT NO: 39
# write a python program which can be able to 
# find all the divisors of that particular number.
num: int = int(input("put the num: "))
def print_divisors():
    for i in range(num):
        divisor = i + 1
        if num % divisor == 0:
            print(divisor)
print_divisors()


#PROJECT NO: 40
#fill out print_multiple(message, repeats), 
# which takes as parameters a string message to print,
#  and an integer repeats number of times to print message.
message_to_print: str = str(input("Enter Message: "))
repeats: int = int(input("Enter repeats number: "))
def print_multiple(message , repeats):
    for i in range(repeats):
        print(message)
print_multiple(message_to_print , repeats)