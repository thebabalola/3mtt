
# ---------- Comparators --------- 
	# Equal to (==), Not equal to (!=), Less than (<), Less than or equal to (<=), Greater than (>), Greater than or equal to (>=)

# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

#For BOOL_FOUR
# Negative numbers represent values less than zero.
# The further a number is from zero on the negative side, the smaller it is.
# For example, -22 is smaller than -18 because it is further left on the number line.


# --------- Compare... Closelier! ----------

# Assign True or False as appropriate on the lines below!
# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False


# ------- How the Tables Have Turned ---------

# Create comparative statements as appropriate on the lines below!
# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = -22 >= 3

# Make me true!
bool_three = 625 == (25**2) #25 raise to power 25 = 25*25

# Make me false!
bool_four = -1 <= -18

# Make me true!
bool_five = 97 != 56


# ------- To Be and/or Not to Be (Boolean Operator - and, or, not)  also lnown as, 'Logical Operators'

# And
1 < 2 and 2 < 3 is True
1 < 2 and 2 > 3 is False

#Let’s practice with and. Assign each variable to the appropriate boolean value.
bool_one = 2 > 5 and 100 == 15**2   # = False
		   #False	  #False		
bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5   # = False
				# False				#False	
bool_three = 19 % 4 != 300 / 10 / 10 and False   	# = False
				# False					  #false
bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2	# = True
				#True				#True
bool_five = True and True  
			# True

# Or
1 < 2 or 2 < 3 is True
1 < 2 or 2 > 3 is False

bool_one = 2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur' 
					#False	  			#True
bool_two = True or False

bool_three = 100 ** 0.5 >= 50 or False
				#False	  		#False
bool_four = True or True

bool_five = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1
					#False	  				#False

# Not
bool_one = not True  #= false

bool_two = not 3 ** 4 < 4 ** 3 		# = false
	#i.e  81 is not < 64  =  True
bool_three = not 10 % 3 <= 10 % 2 	#= false
	#i.e 1 is not <= 0  = True
bool_four = not 3 ** 2 + 4 ** 2 != 5 ** 2	# = False
	#i.e 9 + 16 is equals to  25  =  True
bool_five = not not False
		#i.e not True = false


# -------- This and That (or This, But Not That!) --------

		# there’s an order of operations for boolean operators:
		# not is evaluated first;
		# and is evaluated next;
		# or is evaluated last.

bool_one = False or not True and True
# false or false and true
# false or false
# false

bool_two = False and not True or True
 # false and false or true
 # false or true - Since the 'or' operator needs one operand is true, the result is true.
 # true

bool_three = True and not (False or False)
 # true and not(false)
 # true and true
 # true

bool_four = not not True or False and not True
# not false or false and false 
# true or false - Since the 'or' operator needs one operand is true, the result is true.
# true

bool_five = False or not (True and True)
#false or not(true)
#false or false
#false


# -------- Mix 'n' Match ---------

bool_one = (2 <= 2) and "Alpha" == "Bravo"	# Make me false
             #true			#false
			   # = false (because the 'and' keyword, needs both condition to be true)

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = 24 / 2  >= 12 * 2 - (7 + 5) or 'false' == 'wrong'

# Make me false!
bool_three = not(25 ** 2 > 25 * 4 and 30 % 3 == 30 * 0)

# Make me true!
bool_four = 7 ** 2 + 1 > 7 * 7 or 25 * 4 == 50 + .50

# Make me true!
bool_five = 'name' == 'name' and 100 % 10 <= 100 / 100



# ----- Conditional Statement Syntax -------

#if  (if is a conditional statement that executes some specified code after checking if its expression is True.)
if 8 < 9:
  print("Eight is less than nine!") 

response = 'Y'

answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")


# --------- If You're Having... -----------
def using_control_once():
    if 100 == 1000 / 10:
        return "Success #1"

def using_control_again():
    if 'name' == 'name':
        return "Success #2"
    
print(using_control_once())
print(using_control_again()) 


# ---------- Else Problems, I Feel Bad for You, Son... --------
if 8 > 9:
  print("I don't get printed!")
else:
  print("I get printed!")


answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False   # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False   # Make sure this returns False
    

# --------- I Got 99 Problems, But a Switch Ain't One ----------
if 8 > 9:
  print("I don't get printed!")
elif 8 < 9:
  print("I get printed!")
else:
  print("I also don't get printed!")


def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer  < 5:          
        return -1
    else:
        return 0
        
print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))




#--------- The Big If ---------
   		# ---EXERCISE -----

# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
      
print(grade_converter(92))	# This should print an "A" 
print(grade_converter(70))	# This should print a "C"
print(grade_converter(61))	# This should print an "F"


# The function should return the following letter grades:

# 90 or higher should get an “A”
# 80 - 89 should get a “B”
# 70 - 79 should get a “C”
# 65 - 69 should get a “D”
# Anything below a 65 should receive an “F”
