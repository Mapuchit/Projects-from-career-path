 ## Working with Lists project
 ## Len's Slice

# toppings and their matching prices
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

# number of pizzas sold
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# # combining prices with toppings
pizzas = list(zip(prices, toppings))
print(pizzas)

# sorting pizzas by price (the first item in the tuple elements of pizzas list) from cheapest to most expensive
pizzas.sort()
print(pizzas)

# prints the cheapest and priciest pizzas
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
print(cheapest_pizza) # cheese
print(priciest_pizza) # anchovies

# identifying the 3 cheapest pizzas
three_cheapest = pizzas[:3]
print(three_cheapest)

# how many different 2 dollar pizzas we have
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
