# initializing blockchain list
blockchain = []


def get_last_value():
    """Returns the last value of the current blockchain."""
    return blockchain[-1]


def add_value(amount, last_transaction=[1]):
    """ Appends a new value as the last value to the blockchain.

    Arguments:
        :amount: the amount that should be added.
        :last_transaction: the last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, amount])

def get_user_input():
    """Returns the input of a user as a transaction amount float value."""
    return float(input("Please enter your transaction amount "))


# Add while loop to get input and condition to quit the loop
add_value(get_user_input())
add_value(last_transaction=get_last_value(), amount=get_user_input())
add_value(get_user_input(), get_last_value())

print(blockchain)
# TODO: Add for loop to loop through blockchain using in keyword
