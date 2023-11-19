# initializing blockchain list
blockchain = []
# create an open_transactions structure
# TODO: create a genesis block (dictionary) as the first structure of the blockchain with a sender, recipient and transaction amount

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
    else:
        print("-" * 20)

def verify_chain():
    # index = 0
    is_valid = True
    for index in range(len(blockchain)):
        if index == 0:
            continue
        elif blockchain[index][0] == blockchain[index - 1]:
            is_valid = True 
        else:
            is_valid = False 
            break 
    # for block in blockchain:
    #     if index == 0:
    #         index += 1
    #         continue
    #     elif block[0] == blockchain[index - 1]:
    #         is_valid = True 
    #     else:
    #         is_valid = False 
    #         break 
    #     index += 1
    return is_valid

# Write a function to mine the block
def mine_block():
    pass

waiting_for_input = True 
while waiting_for_input:
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
        waiting_for_input = False 
    else:
       print("Invalid input. Please pick a valid input.")
    if not verify_chain():
        print("Invalid blockchain.")
        break
else:
    # executes when loop finishes
    print("User left")


print("DONE!!")
