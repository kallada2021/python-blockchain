# initializing blockchain list
blockchain = []


def get_last_value():
    """Returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None 
    return blockchain[-1]


def add_transaction(amount, last_transaction):
    """ Appends a new value as the last value to the blockchain.

    Arguments:
        :amount: the amount that should be added.
        :last_transaction: the last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
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

# TODO: Write a function to loop through the blockchain and validate data -- use a for in loop to check the last block index with the first block


while True:
    print("Please choose")
    print("1: Add a new transaction")
    print("2: Output the blockchain blocks")
    print("h: Manipulate blockhain blocks")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_value())
    elif user_choice == "2":
         print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        break
    else:
       print("Invalid input. Please pick a valid input.")

print("DONE!!")
