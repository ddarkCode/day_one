#Instructions
#Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.

#Example Output
#After you have written your code, you should run your program and it should print the following:

#Day 1 - Python Print Function
#The function is declared like this:
#print('what to print')

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#2
#Fix the code below 👇

#print(Day 1 - String Manipulation")
#print("String Concatenation is done with the "+" sign.")
#  print('e.g. print("Hello " + "world")')
#print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#3
#Write a program that prints the number of characters in a user's name.
# You might need to Google for a function that calculates the length of a string.
print(len(input('What is your name?\n')))

#Write a program that switches the values stored in the variables a and b.

#Warning. Do not change the code on lines 1-4 and 12-18.
#Your program should work for different inputs. e.g. any value of a and b.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

temp = a
a = b
b = temp
print('a: ', a)
print('b: ', b)


#Write your code above this line 👆
####################################

#Day One Project

#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
print('Good day and welcome to the band name generator app')
city_name = input('Which city did you grow up in?\n')
pet_name = input('What is the name of your pet?\n')
print('Your Band Name Is: ', city_name + ' ' + pet_name)