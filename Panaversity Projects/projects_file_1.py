#PROJECT NO: 1
# Write a python program which calculates the sum of two numberz and it take those numberz from user as an input 
num1: int = int(input("Enter the number1: "))
num2: int = int(input("Enter the number2: "))
result: int = num1 + num2
print("The Total is" , result)


#PROJECT NO: 2
#Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!"
animal_name: str = str(input("Enter the Animal Name:" ))
print(f"My Favourite Animal is also {animal_name}")


#PROJECT NO: 3
#Write a python program which takes input from the user in farenhiet scale and show output in celsius scale
farenhiet_scale: int = int(input("Enter the temprature in farenhiet scale: "))
celsius_scale: int = (farenhiet_scale - 32) * 5/9
print(celsius_scale)
print(f"""The temprature in farehiet scale is {farenhiet_scale}
    and in celsius scale is {celsius_scale}""")


#PROJECT NO: 4
#Write a program to solve this age-related riddle!
#Ahmed, Bilal, Usman, Daniyal, and Asad are all friends. Their ages are as follows:
#Ahmed is 21 years old.
#Bilal is 6 years older than Ahmed.
#Usman is 20 years older than Bilal.
#Daniyal is as old as Usman's age plus Ahmed's age.
#Asad is the same age as Usman.
ahmed_age: int = 21
bilal_age: int = ahmed_age + 6
usman_age: int = bilal_age + 20
daniyal_age: int = usman_age + ahmed_age
asad_age: int = usman_age
print("Ahmed's age is " , ahmed_age) 
print("Bilal's age is " , bilal_age)
print("Usman's age is " , usman_age)
print("Daniyal's age is " , daniyal_age)
print("Asad's age is " , asad_age)


#PROJECT NO: 5
#Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle
length_1: int = int(input("Enter the first length: "))
length_2: int = int(input("Enter the second length: "))
length_3: int = int(input("Enter the third length: "))
triangle_perimeter: int = length_1 + length_2 + length_3
print(f"The Perimeter of a Triangle is {triangle_perimeter}")


#PROJECT NO: 6
#Ask the user for a number and print its square (the product of the number times itself).
num: int = int(input("Enter the Number: "))
result: int = num ** 2
print(f"The Square of {num} is {result}")


#PROJECT NO: 7
#write a python program which takes mass from user and gives energy as output according to E=mc**2
C: int = 299792458
mass_in_kg: float = float(input("Enter the mass: "))
energy_in_joules: float = (mass_in_kg) * (C**2)
result: float = energy_in_joules
print(result)


#PROJECT NO: 8
#Converts feet to inches.There are 12 inches per foot. Foot is the singular, and feet is the plural.
length_in_feet: int = int(input("Enter the length in foot: "))
length_in_inches: int = length_in_feet * 12
print(length_in_inches)


#PROJECT NO: 9
#Write a program that asks the user for the lengths of the two perpendicular sides of..
# .. a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
import math
a: int = int(input("Enter a: "))
b: int = int(input("Enter b: "))
c: int = math.sqrt(a**2 + b**2)
print(f"The Hypotenuous is {c} ")


#PROJECT NO: 10
#Ask the user for two numbers, one at a time, and ..
#.. then print the result of dividing the first number by the second and also the remainder of the division.
num_1: int = int(input("Enter num_1: "))
num_2: int = int(input("Enter num_2: "))
quotient: int = num_1 / num_2
reminder: int = num_1 % num_2
print(quotient)
print(reminder)