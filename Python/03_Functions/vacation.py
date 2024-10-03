# ------ Before We Begin -------
def answer():
  return 42


# Planning your Trip
def hotel_cost(nights):
  return 140 * nights	# The hotel costs $140 per night.

	# Getting There (We will be needing to take a plane ride to get to your location.)
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  
	# Transportation ( We will need a rental car in order for you to get around.)
def rental_car_cost(days):
  rent = 40
  if days >= 7:
    return rent * days - 50			#  you get $50 off , if car is rented for 7 days or more
  elif days >= 3:
    return rent * days - 20			#  you get $20 off , if car is rented for 3 days or more
  else:
    return rent * days

	# Pull it Together (let’s put them together in order to find the total cost of your trip.)
def trip_cost(city, days, spendingMoney):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spendingMoney

print(trip_cost('Los Angeles', 5, 600)) 

	# Hey, You Never Know! (There also needs to be room for additional costs like fancy food or souvenirs.)
		
		# Modify your trip_cost function definition. Add a third argument, spending_money.
		# Modify what the trip_cost function does. by adding  variable spending_money to the sum that it returns.


	# Plan Your Trip! (What if we went to Los Angeles for 5 days and brought an extra 600 dollars of spending money?)
print(trip_cost('Los Angeles', 5, 600)) 





# N.B
# 	Notice that we changed the argument of hotel_costs() from nights to days - 1.
#   Since we want trip_cost() to only depend on two parameters, 
#   we have to convert the variable nights into days. 
#   If you are going to be staying somewhere, 
#   the number of nights you stay there is one less than the number of days you were there 
#   (imagine a weekend trip to visit family, you leave Saturday and return Sunday, 
#    so you visit for two days, but only stay for one night).