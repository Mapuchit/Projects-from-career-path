 ## Function Arguments project
 ## The Nile

'''
The Nile fullfilment agency brings everything you could possibly want straight to your door!
Use your knowledge of Python functions and how to manipulate arguments to help automate practices for the biggest world-changing company.
'''

from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

 ## Not Just A River In Egypt

# Develop a program that will help minimize delivery costs.
# First we need to calculate the costs.
def calculate_shipping_cost(from_coords, to_coords, shipping_type = "Overnight"):
  # we gave shipping_type a default argument in case shoppers don't indicate shipping_type

  # both coordinates are given as tuples containing the latitude and the longitude
  # since our get_distance() function looks for all four as separate arguments, we’ll need to separate these variables out using variable unpacking
  from_lat, from_long = from_coords
  to_lat, to_long = to_coords
  # now we can get the distance
  distance = get_distance(from_lat, from_long, to_lat, to_long)
  # also could have used:
  # get_distance(*from_coords, *to_coords)

  # we get the shipping_rate by finding shipping_type in the given SHIPPING_PRICES dictionary
  shipping_rate = SHIPPING_PRICES[shipping_type]

  # calculate the price
  price = distance * shipping_rate

  # return the formatted price
  return format_price(price)

# Test the function
test_function(calculate_shipping_cost)

 ## Careers At The Nile

# A function to help finding the best (cheapest) driver.
# It will take an arbitrary number of drivers as positional arguments.
def calculate_driver_cost(distance, *drivers):

  # we need to calculate how much it would cost for any of the drivers to fulfill this order
  cheapest_driver = None
  cheapest_driver_price = None

  # iterate over all the drivers
  for driver in drivers:
    # calculate the driving time for each
    driver_time = driver.speed * distance
    # calculate the price for each
    price_for_driver = driver.salary * driver_time
    # check is the current driver is the cheapest
    if cheapest_driver == None:
      # means this is the first driver we looked at
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    elif cheapest_driver != None:
      # this is not the first driver looked at
      # check if current drivers price is cheaper
      if price_for_driver < cheapest_driver_price:
        # update cheapest driver
        cheapest_driver = driver
        cheapest_driver_price = price_for_driver

  # we found the cheapest driver!
  return cheapest_driver_price, cheapest_driver

# Test the function
test_function(calculate_driver_cost)

 ## The Nile Exclusive

# A function to calculate how much money we made using information from trips.
# This function will be passed a number of Trip IDs with corresponding trip information as arguments.
# We will save these trips as keyword arguments.
def calculate_money_made(**trips):
  # create a counter variable
  total_money_made = 0

  # iterate through the trips dictionary
  for trip_id, trip in trips.items():
    # calculate the trip revenue
    trip_revenue = trip.cost - trip.driver.cost
    # increment the counter
    total_money_made += trip_revenue

  # return total money made
  return total_money_made

# Test the function
test_function(calculate_money_made)
