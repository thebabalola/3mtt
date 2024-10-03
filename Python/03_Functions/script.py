# ------- What Good are Functions? -------

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print("With tax: %f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print("With tip: %f" % bill)
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


# ------ Function Junction ------
	# Functions are defined with three components:

def hello_world():      								#  - The header					 
    """Prints 'Hello World!' to the console."""  		#  - An optional comment  
    print("Hello World!")  # Proper indentation			# - The body, 

hello_world()											# - The function call 

def spam():
    """Prints 'Eggs!'"""
    print('Eggs!')

spam()


# ------- Call and Response ------
	# After defining a function, it must be called to be implemented

def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print(f"{n} squared is {squared}.") 
    return squared

square(10)	# Calls the square function


# ------- Parameters and Arguments -------
	# A parameter is a variable that is an input to a function.  While the values passed into the parameters are known as the arguments

def power(base, exponent):
  """outputs the result  of 34 to the power of 4"""
  result = base ** exponent
  print(f"{base} to the power of {exponent} is {result}.")

power(37, 4)  # Add arguments here!


# ------- Functions Calling Functions -------
def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  # return n + 2 - original code body
  return one_good_turn(n) + 2     # adds the result of one_good_turn(n) to 2


# ------ Practice Makes Perfect -------
def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")


def cube (number):
  return number ** 3

def by_three (number):
  if number % 3 == 0:      
    return cube(number)
  else:
    return False




# ------- I Know Kung Fu -------
# Importing a specific function from a module
from module import functionName

# Importing a specific function from the math module
from math import sqrt

# Importing everything from a module
from module import *

from math import *



# ------ Generic Imports ------
	# There is a Python module named math that includes a number of useful variables and functions, 
	# and sqrt() is one of those functions. In order to access math.
	# all you need is the import keyword. When you simply import a module this way, it’s called a generic import.

import math

print(math.sqrt(25))  #The sqrt() methid, finds the sqaure root of a 25, which = 5



# ------- Function Imports -------
	# module: A Python file (with a .py extension) that contains definitions like variables, functions, or classes.
	# function: A function defined within the module that you want to import.

from module import functionName  # this import a function from the module(a python file)
from math import sqrt 	# this imports sqrt function from math (this is an act of hand picking a particular function that you want)



# ------- Universal Imports ------
from module import *     # imports all the variables and functions in a module 

from math import * 		# imports all the variables and functions from the math module 




# ------- Here Be Dragons -------
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!



# ------- On Beyond Strings -------
	# Analytic built-in functions, outside of .upper(), .lower(), str(), and len() . 

# Usage: When a function uses " * "args, it can take any number of arguments.
def biggest_number(*args):
  print(max(args)) 
  return max(args) #  The max() Finds and returns the largest number from the provided arguments.
    
def smallest_number(*args):
  print(min(args)) # The min() Finds and returns the smallest number from the provided arguments.
  return min(args)

def distance_from_zero(arg):
  print(abs(arg)) 
  return abs(arg)  # abs() Finds and returns the absolute value of a single argument.(which means converting negative numbers to positive and leaving positive numbers unchanged.)

biggest_number(-10, -5, 5, 10)   	# outputs: 10
smallest_number(-10, -5, 5, 10)		# outputs: -10
distance_from_zero(-10)				# outputs: 10


		# ----- max() -----
maximum = 2, 3, 9, 5
print(max(maximum)) 		# outputs: 9

		# ----- min() -----
minimum = 11, 7 , 9, 27
print(min(minimum))			# outputs: 7

		# ----- abs() -----
absolute = -42
print(abs(absolute))		# outputs: 42

		# ----- type() -----
      #  returns the type of the data it receives as an argument.
integer = 42
longFloat = 0.23
string = 'Hello Bro'

print(type(integer))		# outputs: <type 'int'>
print(type(longFloat))		# outputs: <type 'float'>
print(type(string))			# outputs: <type 'str'>



# ------- Review: Functions --------
def speak(message):
  return message

if happy():
  speak("I'm happy!")
elif sad():
  speak("I'm sad.")
else:
  speak("I don't know what I'm feeling.")


def shut_down(s):
  if s == 'yes':
    return 'Shutting down'
  elif s == 'no':
    return 'Shutdown aborted'
  else:
    return "Sorry"
    


# ------- Review: Modules -------
from math import sqrt

print(sqrt(13689))		# outputs: 117.0



# ------- Review: Built-In Functions -------
def is_numeric(num):
  return type(num) == int or type(num) == float:

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2


def distance_from_zero(dist):
  #checks if distance inputed is int or floatso as to return it absolute value
  if type(dist) == int or type(dist) == float:
    return abs(dist)
  else:
    return 'Nope'