blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain or None if the blockchain is empty"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Appen a new value as well as the last blockchain value to the blockchain

    Arguments:
        :transaction_amount: The amount that should be added
        :last_transaction: The last blockchain transaction (default: [1])
     """
    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])
    return blockchain


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float """
    return float(input('Your transaction amount: '))


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_elements():
    for block in blockchain:
        print(block)


def verify_chain():
    #block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose: ')
    print('1. Add a new value to the blockchain')
    print('2. Outputh the blockchain blocks')
    print('h. Manipulate the chain')
    print('q. Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_value = get_transaction_value()
        add_transaction(tx_value, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if(len(blockchain)>1):
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list')
    if not verify_chain():
        print('WARNING: Invalid blockchain')
        waiting_for_input =  False


print('Done!')
