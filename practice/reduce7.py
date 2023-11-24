import functools

# initializing blockchain list
MINING_REWARD = 10

genesis_block = {
    "previous_hash": "", 
    "index": 0, 
    "transactions": []
}
blockchain = [genesis_block]
open_transactions = []
owner = "Yusuf"
participants = {"Yusuf"}

def get_last_value():
    """Returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None 
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]


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

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True 
    return False 


def mine_block():
    last_block = blockchain[-1] # gets last value
    hashed_block = hash_block(last_block)
    reward_transaction = {
        "sender": "MINING",
        "recipient": owner,
        "amount" : MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block, 
        "index": len(blockchain), 
        "transactions": copied_transactions
    }
    blockchain.append(block)
    return True 


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
    # TODO: create a hash by using the hashlib library
    return "-".join([str(block[key]) for key in block])

def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block["transactions"] if tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx["amount"] for tx in open_transactions if tx["sender"] == participant]
    tx_sender.append(open_tx_sender)
    # TODO: refactor using the sum function to get all tx_amt
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + tx_amt[0] if len(tx_amt) > 0 else 0, tx_sender, 0)
    # amount_sent = 0 
    # print(f"tx sender {tx_sender}")
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         amount_sent += tx[0]
    tx_recipient = [[tx["amount"] for tx in block["transactions"] if tx["recipient"] == participant] for block in blockchain]
    # TODO: make the amount recieved for loop shorter by using reduce
    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_recieved += tx[0]
   
    return amount_recieved - amount_sent

def verify_chain():
    """Verifies the current blockchain and returns True if valid, False if not valid."""
    for (index, block) in enumerate(blockchain):  # creates tuple with index
        print(block)
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index -1]):
            return False 
    return True 

def verify_all_transactions():
    # is_valid = True 
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True 
    #     else:
    #         is_valid = False 
    # return is_valid
    return all([verify_transaction(tx) for tx in open_transactions])

waiting_for_input = True 
while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction")
    print("2: Output the blockchain blocks")
    print("3: Mine a new block.")
    print("4: Output Participants")
    print("5: check transaction validity")
    print("h: Manipulate blockhain blocks")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient=recipient, amount=amount):
            print("Added Transaction.")
        else:
            print("Transaction failed.")
        print(open_transactions)
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "3":
        if mine_block():
            open_transactions = []
    elif user_choice == "4":
        print(participants)
    elif user_choice == "5":
        if verify_all_transactions():
            print("All Transactions are valid.")
        else:
            print("There are invalid transactions.")
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
    print(f"Balance of Yusuf {get_balance('Yusuf'):6.2f}")
else:
    # executes when loop finishes
    print("User left")


print("DONE!!")
