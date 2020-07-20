# Veneer - Classes
> Organize the operation of an art marketplace.

## General info
Use Python classes to manage the listing, buying and selling of art pieces.

## Technologies
* Python 3.7.6 
* Git Bash 2.27.0
* Atom v1.49.0
* Windows 10 Pro

## Features
* An Art class that keeps track of the owner of an art piece and some details including year and artist name.
  * Display the information about the art piece in a clear and concise way.
* A Listing class that keeps track of the name of the art piece listed, it's price and the seller details.
  * Expiration date options for linstings. They are automatically removed from the marketplace if the date is passed.
* A Marketplace class that keeps track of all the current listings.
  * Functionality to add or remove listing, and show all listings in the marketplace.
* A Client class that keeps track of the clients name, location and if it is a museum or not.
  * Function to sell artwork by creating a new listing on the marketplace.
  * Function to buy artwork, change the ownership and remove listing from the marketplace.
  * Wallet for each client that gets updated when artworks are bought or sold.
  * Wishlist for clients where they can store interesting listings.

## Status
Project is: _finished_

## Inspiration
This is a guided project that practices Python classes from the Computer Science Carreer Path on [Codecademy](https://www.codecademy.com/learn).
