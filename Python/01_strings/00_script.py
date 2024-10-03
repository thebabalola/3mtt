#A string can contain letters, numbers, and symbols.
name = "Ryan"
age = "19"
food = "cheese"


# ------ Escaping characters ----------
 # 'There's a snake in my boot!' - the "there's would cause problem"
 #  'There\'s a snake in my boot!'  - The wright way to write it


#Access by Index (strings are arrays of cahracters)
c = "cats"[0]
n = "Ryan"[3]

fifth_letter = 'MONTY'[4]
print(fifth_letter) # outputs: Y


# --------- String methods ---------

#len() -  this gets the length of a string! (the number of characters)
parrot = "Norwegian Blue"
print(len(parrot)) #outputs: 14 - length of the parrot variable

#lower()  - get rids of all the capitalization in a strings.
name = "Ryan".lower()

parrot = "Norwegian Blue".lower()
print(parrot.lower())
print(name)  

#upper()  - makes all characters capitalization in a strings.
dove = "sparkling blue"
print(dove.upper())

#str()  - The str() method turns non-strings into strings!
str(2) #would turn 2 into "2".

pi = 3.14
print(str(pi))


# --------- Dot Notation ---------
	#(Methods such as upper() and lower() that uses .dot notation only works with strings. While len() and str() works with all othwer data types - int, float etc)

lion = "roar"
len(lion)
lion.upper()

ministry = "The Ministry of Silly Walks"

print(len(ministry))
print(ministry.upper())


# -------- printing strings ---------
"""Tell Python to print "Monty Python"
to the console on line 4!"""

print('Monty Python')


# -------- Printing Variables --------
"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print(the_machine_goes)


# -------- String Concatenation --------
print("Spam " + "and " + "eggs")


#  ------- Explicit String Conversion (involves combining a string with something that isn’t a string.)
print("The value of pi is around " + str(3.14)) 


# -------- String Formatting with % (Part 1) --------
string_1 = "Camelot"
string_2 = "place"

print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)) 

# -------- String Formatting with f (Part 2) -------- 
name = "Alex"
quest = "Teaching Python"
color = "Blue"

print(f"Ah, so your name is {name}, your quest is {quest}, and your favorite color is {color}.")
print(f'''Hi, my name is {name}
and my quest, is to complete {quest}
''')  #this inolves the use of '''triple quote''' for multi-line string


# ---- REVIEW ----
my_string = 'Learning Python'
print(len(my_string))
print(my_string.upper())
