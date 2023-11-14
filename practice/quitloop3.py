# initializing blockchain list
blockchain = []


def get_last_value():
    """Returns the last value of the current blockchain."""
    # TODO: check if the blockchain is empty or if it has a value
    return blockchain[-1]


def add_value(amount, last_transaction=[1]):
    """ Appends a new value as the last value to the blockchain.

    Arguments:
        :amount: the amount that should be added.
        :last_transaction: the last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, amount])

def get_transaction_value():
    """Returns the input of a user as a transaction amount float value."""
    return float(input("Please enter your transaction amount "))

def get_user_choice():
    user_input = input("Your choice")
    return user_input

def print_blockchain_elements():
     for block in blockchain:
        print(f"Outputting block \n{block}")

add_value(get_transaction_value())

# TODO add a third choice to the while loop to allow the user to quit and add code to end the infinate loop when the user quits
# TODO: handle invalid input selection
while True:
    print("Please choose")
    print("1: Add a new transaction")
    print("2: Output the blockchain blocks")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_value())
    else:
        print_blockchain_elements()

print("DONE!!")
