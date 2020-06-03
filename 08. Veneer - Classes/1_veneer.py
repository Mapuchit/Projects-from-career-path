 ## Classes project
 ## Veneer - Create an Art Marketplace - for people and organizations to buy and sell pieces of art!

## The Marketplace of Artistic Ideas

# create a marketplace to maintain the responsibilities of buying, selling, listing, and delisting artworks
class Marketplace:
  def __init__(self, todays_date):
    self.listings = []
    self.todays_date = todays_date
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, old_listing):
    self.listings.remove(old_listing)
  def show_listings(self):
    print("Veneer's listings:")
    # remove expired listings before printing
    for listing in self.listings:
      if self.todays_date > listing.expiration_date:
        self.listings.remove(listing)
      else:
        print(listing)

# create our main marketplace
veneer = Marketplace(10)
print(veneer.show_listings()) # still empty

## Don't Be Listless

# create a class to list works of art
# these will be parameters for our Marketplace
class Listings:
  def __init__(self, art, price, expiration_date, seller):
    self.art = art
    self.price = price
    self.seller = seller
    self.expiration_date = expiration_date
  def __repr__(self):
    return "{n}, ${p}M (USD), expires: {d}".format(n = self.art.title, p = self.price, d = self.expiration_date)

## The Thin Veneer of Viability

# building a model for our works of art
class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  # a representation of the artwork in as close to standard citation format as we can manage
  def __repr__(self):
    return "{a}. \"{t}\". {y}, {m}. {o}, {l}.".format(a = self.artist, t = self.title, m = self.medium, y = self.year, o = self.owner.name, l = self.owner.location)

## We Need Clients!

# create a class for clients
class Client:
  def __init__(self, name, location, is_museum, wallet):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    self.wallet = wallet
    self.wishlist = []
  def sell_artwork(self, artwork, price, expiration_date):
    # make sure the client owns the art they’re trying to sell
    if artwork.owner == self:
      new_listing = Listings(artwork, price, expiration_date, self.name)
      veneer.add_listing(new_listing)
  def buy_artwork(self, artwork):
    # check that the artwork is not owned by the client and make sure that the artwork is listed in veneer.listings
    if artwork.owner != self:
      for listing in veneer.listings:
        if listing.art == artwork:
          # go through with the transaction, save the listing
          art_listing = listing
          # update own wallet
          self.wallet -= art_listing.price #art_listing.price
          # update seller wallet
          art_listing.art.owner.wallet += art_listing.price
          # update the owner
          artwork.owner = self
          # remove from listings
          veneer.remove_listing(art_listing)
          # remove from wishlist if present
          if art_listing.art.title in self.wishlist:
            self.wishlist.remove(art_listing.art.title)
  def addto_wishlist(self, artwork):
    if artwork.owner != self:
      for listing in veneer.listings:
        if listing.art == artwork:
            self.wishlist.append(listing.art.title)

# our first client
edytta = Client("Edytta Halpirt", "Private Collection", False, 25)
# our second client
moma = Client("The MOMA", "New York", True, 125)

# create a new work of art
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)
print("A new work of art:")
print(girl_with_mandolin)

# use edytta.sell_artwork() to create a listing for girl_with_mandolin
edytta.sell_artwork(girl_with_mandolin, 6, 11)
# try if our newly listed work of art is on the marker
veneer.show_listings()
# prints "Girl with a Mandolin (Fanny Tellier), $6M (USD)"

## Buy Low, Sell High

# The MOMA is very interested in purchasing girl_with_mandolin
moma.addto_wishlist(girl_with_mandolin)
print(moma.wishlist)
moma.buy_artwork(girl_with_mandolin)
# check if the purchase was successful
print("The MOMA purchased an artwork:")
print(girl_with_mandolin)

# check if the wallet's have been updated for the seller and the buyer
print(edytta.wallet) # 31
print(moma.wallet) # 119
# check if the artwork has been removed from the client's wishlist
print(moma.wishlist)
# check if our listings have been updated
veneer.show_listings() # empty again
