# DATE TIME
	# Here we’ll use datetime to print the date and time in a nice format.

# Getting the Current Date and Time
	# We can use a function called datetime.now() to retrieve the current date and time.
from datetime import datetime

print(datetime.now())
	#OR
date = datetime.now()
print(date)		##outputs: current date,month & year

print(date.day)		#outputs: current day
print(date.month)	#outputs: current month
print(date.year)	#outputs: current year

print(date.hour)	##outputs: current hour
print(date.minute)	###outputs: current minute
print(date.second)



# Extracting Information
	# In the case we don’t want the entire date and time

date = datetime.now()

current_year = date.year
current_month = date.month
current_day = date.day

print(current_year)
print(f'{current_month:02d}/{current_day:02d}/{current_year:04d}')


#Hot Date
	#(in order to print today’s date in the following format? mm/dd/yyyy)

print(f'{date.month:02d}-{date.day:02d}-{date.year:04d}')


#Pretty Time
print(f'{date.hour:02d}:{date.minute:02d}:{date.second:02d}')
