blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Appen a new value as well as the last blockchain value to the blockchain

    Arguments:
        :transaction_amount: The amount that should be added
        :last_transaction: The last blockchain transaction (default: [1])
     """
    blockchain.append([last_transaction, transaction_amount])
    return blockchain


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float """
    return float(input('Your transaction amount: '))


add_value(get_user_input())
add_value()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=get_user_input())
add_value(get_user_input(), get_last_blockchain_value())

print(blockchain)
