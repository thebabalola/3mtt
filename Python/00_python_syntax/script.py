# Learn Python 3


# --------- Comments --------
city_name = "St. Potatosburg" #variable stores name of city
city_pop = 340000


# -------- Print Function --------
print('Hello world!')
print("Hello " + 'Taiwo')


# -------- variables --------
todays_date = '8th Sept, 2024'
name = 'Senior Dev Rebirth'
experience = 3. #float


# --------- Arithmetics --------
num1 = 5
num2 = 4
product = num1 * num2

num = 1398
divisor = 11
remainder = num % divisor

print(product)
print(remainder)


# -------- Updating Variables --------
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall = annual_rainfall +  september_rainfall + october_rainfall + november_rainfall + december_rainfall
print(annual_rainfall)


# -------- numbers --------
cucumbers = 7
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber

print(total_cost)


# -------- Two Types of Division (Modulo and Quotient) -------
    # (To yield a float as the result quoteient are usually roundded up, programmers often change either the numerator or the denominator (or both) to be a float:)

quotient = 7/2 # the value of quotient is 3, even though the result of the division here is 3.5

# (using the dot . the remainder is rounded up to float )
quotient1 = 7/2.
# the value of quotient1 is 3.5 
quotient2 = 7./2
# the value of quotient2 is 3.5
quotient3 = 7./2.
# the value of quotient3 is 3.5

# (using the float() method the remainder is rounded up to float )
quotient1 = float(7)/2 
# the value of quotient1 is 3.5

cucumbers = 100
num_people = 6
whole_cucumbers_per_person = float(cucumbers) / num_people

print(whole_cucumbers_per_person)  #outputs: float value of the cucumver divided among the 5 persons


# -------- Multi-line Strings ---------
    # ( If we want a string to span multiple lines, we can also use triple quotes)
haiku = ''' 
The old pond,
A frog jumps in:
Plop!
'''


# ------- Booleans (Can be refered to as a special case of an integer - True = 1 and False = 0.)

# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.
age_is_12 = False
name_is_maria = True


# -------- ValueError --------
age = 13
print("I am " + str(age) + " years old!")   #coverts int number to string


number1 = "100"
number2 = "10"
string_addition = number1 + number2 

int_addition = int(number1) + int(number2)  #coverts string number to int
print(int_addition)


string_int = "10"
numeric_int = 12

print(float(string_int))    #coverts string number to float
print(float(numeric_int))    #coverts int number to float


float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2

big_string = 'The product was ' + str(product)  # concatinates and turns/accomodates product to string
print(big_string)


# -------- Overall Review -------

skill_completed = "Python Syntax"
exercises_completed = 13

points_per_exercise = 5 #The amount of points for each exercise may change, because points don't exist yet

point_total = 100
point_total = point_total + exercises_completed * points_per_exercise
print('I got' + str(point_total) + 'points!')   #coverts total_point to string as it is ben printed amoung strings
