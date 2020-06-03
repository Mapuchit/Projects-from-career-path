 ## Python Control Flow project
 ## Sal's Shipping

# cost of ground shipping
def ground_ship_cost(weight):
  if weight <= 2:
    ground_cost = weight * 1.50 + 20
  elif 2 < weight <= 6:
    ground_cost = weight * 3.00 + 20
  elif 6 < weight <= 10:
    ground_cost = weight * 4.00 + 20
  else:
    ground_cost = weight * 4.75 + 20
  return ground_cost

# test ground shipping function
print(ground_ship_cost(8.4))

# premium gound shipping flat rate
premium_ground_ship_cost = 125.00

# cost of drone shipping
def drone_ship_cost(weight):
  if weight <= 2:
    drone_cost = weight * 4.50
  elif 2 < weight <= 6:
    drone_cost = weight * 9.00
  elif 6 < weight <= 10:
    drone_cost = weight * 12.00
  else:
    drone_cost = weight * 14.25
  return drone_cost

# test drone shipping function
print(drone_ship_cost(1.5))

# find cheapest shipping method for given weight
def cheapest_shipping(weight):
  if ground_ship_cost(weight) < drone_ship_cost(weight) and ground_ship_cost(weight) < premium_ground_ship_cost:
    print("Ground shipping is your cheapest option.")
    print("It will cost " + str(ground_ship_cost(weight)) + " pounds to ship your package with ground shipping.")
  elif drone_ship_cost(weight) < premium_ground_ship_cost:
    print("Drone shipping is your cheapest option.")
    print("It will cost " + str(drone_ship_cost(weight)) + " pounds to ship your package with drone shipping.")
  else:
    print("Premium ground shipping is your cheapest option.")
    print("It will cost " + str(premium_ground_ship_cost) + " pounds to ship your package with premium ground shipping.")

cheapest_shipping(4.8)
cheapest_shipping(41.5)
