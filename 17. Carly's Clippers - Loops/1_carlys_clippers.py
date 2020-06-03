 ## Loops project
 ## Carly's Clippers

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# the average price of a cut
total_price = 0
for price in prices:
  total_price += price

average_price = total_price / len(prices)
print("Average haircut price before discount: " + str(average_price))

# cutting all prices by 5 dollars
new_prices = [price - 5 for price in prices]
print("The new discount prices are: " + str(new_prices))

# the new average new_prices
total_price_new = 0
for price in new_prices:
  total_price_new += price

average_price_new = total_price_new / len(new_prices)
print("Average haircut price after discount: " + str(average_price_new))

# how much revenue was brought in last week
total_revenue = 0
# create a variable i that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average daily revenue: " + str(average_daily_revenue))

# advertising haircuts under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print("Haircuts under $30: " + str(cuts_under_30))
