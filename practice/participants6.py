# initializing blockchain list
genesis_block = {
    "previous_hash": "", 
    "index": 0, 
    "transactions": []
}
blockchain = [genesis_block]
open_transactions = []
owner = "IAmTheOwner"
# TODO: create a set to add participants



def get_last_value():
    """Returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None 
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Appends a new value as the last value to the blockchain.

    Arguments:
        :sender. Sender of the coins.
        :recipient: Recipient of the coins
        :amount: The amount of coins send. Default is 1.0
    """
    transaction = {
        "sender" : sender,
        "recipient": recipient,
        "amount": amount
    }
    open_transactions.append(transaction)
    # TODO: add recipient and sender to the participants set


def mine_block():
    last_block = blockchain[-1] # gets last value
    hashed_block = hash_block(last_block)
    # TODO: create a reward transaction to give the owner a balance when mining a block
    block = {
        "previous_hash": hashed_block, 
        "index": len(blockchain), 
        "transactions": open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """Returns the input of a user as a transaction amount float value."""
    tx_recipient = input("Enter the transaction's recipient")
    tx_amount = float(input("Please enter your transaction amount "))
    return (tx_recipient, tx_amount)

def get_user_choice():
    user_input = input("Your choice")
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print(f"Outputting block \n{block}")
    else:
        print("-" * 20)


def hash_block(block):
    return "-".join([str(block[key]) for key in block])

def verify_chain():
    """Verifies the current blockchain and returns True if valid, False if not valid."""
    for (index, block) in enumerate(blockchain):  # creates tuple with index
        print(block)
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index -1]):
            return False 
    return True 


waiting_for_input = True 
while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction")
    print("2: Output the blockchain blocks")
    print("3: Mine a new block.")
    print("4: Output participants.")
    print("h: Manipulate blockhain blocks.")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient,amount=amount)
        print(open_transactions)
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "3":
        # TODO: reset transactions after mining a block
        mine_block()
    elif user_choice == "4":
        # TODO: output participants
        print("Output participants set here!")
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "", 
                "index": 0, 
                "transactions": [{"sender": "Chris", "recipient": "Omar", "amount": 55.50}]
            }
    elif user_choice == "q":
        waiting_for_input = False 
    else:
       print("Invalid input. Please pick a valid input.")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid blockchain.")
        break
else:
    # executes when loop finishes
    print("User left")


print("DONE!!")
