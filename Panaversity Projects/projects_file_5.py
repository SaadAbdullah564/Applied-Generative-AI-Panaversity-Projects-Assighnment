#PROJECT NO: 41
# Write a function called print_ones_digit , which takes as a parameter 
# an integer num and prints its ones digit. The modulo (remainder) operator, %,
#  should be helpful to you here. Call your function from main()!
def print_ones():
    num: int = int(input("Enter number:  "))
    ones_digit: int = num % 10
    print(f"The digit at ones place of {num} is {ones_digit}")
print_ones()


#PROJECT NO: 42
#make a sentence
word: str = str(input("Enter word:  "))
print("Is this a verb noun and adjective? ")
parts_of_speech: int = int(input("Enter parts of speech: "))
def make_sentence(word, parts_of_speech):
    if parts_of_speech == 0:
        print(f"I am excited to this {word} from this i add many things in my collection")
    elif parts_of_speech == 1:
        # verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif parts_of_speech == 2:
        # adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")
make_sentence(word, parts_of_speech)


#PROJECT NO: 43
# write a program which specifies the age
adult_age: int = 18
def calculate_ages():
    age: int = int(input("enter age: "))
    if age >= adult_age:
        print(f"How old is this person?:{age}")
        print("entered age is greater than adult age")
        print(True)
    else:
        print(f"How old is this person?:{age}")
        print("entered age is less than adult age")
calculate_ages()


#PROJECT NO: 44
#write a program which can print your name in italics.
user_name: str = str(input("Enter name:  "))
def greet(user_name):
    print(f"Greetings {user_name} !")
greet(user_name)


#PROJECT NO: 45
#Implement the following function which takes in 3 integers as parameters:
def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False
in_range(45, 67, 78)


#PROJECT NO: 46
#write a python program to get the number of fruits in a shop
def main():
	fruit : str = input("Enter a fruit: ")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)
def num_in_stock(fruit):
	"""
	This function returns the number of fruit Sophia has in stock.
	"""
	if fruit == 'apple':
		return 2
	if fruit == 'durian':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0
if __name__ == '__main__':
    main()


#PROJECT NO: 47
#take many inputs from user
def user_info():
    first_name: str = str(input("Enter first name: "))
    last_name: str = str(input("Enter last name: "))
    user_email: str = str(input("Enter Email: "))
    return first_name , last_name , user_email
def call_info():
    complete_data: str = user_info()
    print("The complete details of user are" , complete_data )
call_info()


#PROJECT NO: 48
#write a program 
def main_no_2():
	num: int = 7
	num = subtract_seven(num)
	print("this should be zero: ", num)
def subtract_seven(num):
	num = num - 7
	return num
main_no_2()


#PROJECT NO: 49
#write a python program which can be able too guess a number between 1 and 99
import random
def number():
    secret_number = random.randint(1, 99)
    print("Hint : I am thinking a number between 1 and 99")
    guess_number: int = int(input("Enter your guess: "))
    if guess_number < secret_number:
        print("your guess is too low")
    else:
        print("your guess is too high") 
    print("Congrats! The  correct number was: " , secret_number)
number()


#PROJECT NO: 50
# write a python program to find the solution
max_term_value: int = 50
def main_no_3():
    curr_term: int = 0
    next_term: int = 1 
    while curr_term <= max_term_value:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
main_no_3()