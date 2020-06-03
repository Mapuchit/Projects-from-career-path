 ## Classes project
 ## Basta Fazoolin' - family-style Italian restaurant Basta Fazoolin’ with My Heart

## Making the Menus

# four different menus: brunch, early-bird, dinner, and kids
# create a menu class
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "Our {menu} is available from {s} to {e}".format(menu = self.name, s = self.start_time, e = self.end_time)
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return total_price

# our first menu
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("Brunch Menu", brunch_items, 1100, 1600)

# our second menu
earlyb_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("Early Bird Menu", earlyb_items, 1500, 1800)

# our third menu
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("Dinner Menu", dinner_items, 1700, 2300)

# our last menu
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids Menu", kids_items, 1100, 2100)

print(brunch.name)
# try out the string representation
print(brunch)

# test our calculate_bill method
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

## Creating the Franchises

# create a Franchise class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

# our first two franchises
menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store)

# test out our available_menus() method
print(new_installment.available_menus(1200))
print(flagship_store.available_menus(1700))

## Creating Businesses!

# We’re going to create a restaurant that sells arepas!
# first define a Business class
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# create our first business
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
print(basta_fazoolin.name)
print(basta_fazoolin.franchises)

# create a new business
# create the menu
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("Arepa Menu", arepas_items, 10000, 20000)
# create the franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
# create the business
take_a_arepa = Business("Take a' Arepa", [arepas_place])
print(take_a_arepa.name)
print(take_a_arepa.franchises)
print(take_a_arepa.franchises[0].menus[0])
