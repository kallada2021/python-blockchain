# TODO: make tx_amount DRY and add function doc strings
blockchain = []


def get_last_value():
    return blockchain[-1]


def add_value(amount, last_transaction=[1]):
    blockchain.append([last_transaction, amount])


tx_amount = float(input("Please enter your transaction amount "))
add_value(tx_amount)
add_value(last_transaction=get_last_value(), amount=22)
add_value(8.89, get_last_value())

print(blockchain)
