from art import logo
print (logo)
# TODO-2: Save data into dictionary {name: price}

bids = {}


# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_price = int(bidding_dictionary[bidder])
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


# TODO-3: Whether if new bids need to be added
new_bid = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = input("What is your bid?: $")
    bids[name] = price
    new_bid = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if new_bid == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif new_bid == "yes":
        print("\n" * 100)