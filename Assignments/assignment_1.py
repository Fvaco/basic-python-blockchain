# 1) Create two variables – one with your name and one with your age

# name = "Fvaco"
# age = 29
name = input('Enter your name: ')
age = input('Enter your age: ')

# 2) Create a function which prints your data as one string


def print_user_data():
    """ Prints the user name (uses global variables)"""
    print(name + ' has ' + str(age) + ' years old')


print_user_data()
# 3) Create a function which prints ANY data (two arguments) as one string


def print_concatenated_data(first_element, second_element):
    """ Print two concatenated strings 

    Arguments:
        :param first_element: The first string to be concatenated
        :param second_element: The second string to be concatenated
    """
    print(first_element + ' has ' + second_element + ' years old')


print_concatenated_data(name, age)

# 4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)


def calculate_my_decades(age):
    """ Calculates the integer part of the age received 

    Arguments:
        :param age: The age for which the decades should be calculated

    Returns the number of decades lived
    """
    return age // 10


print('You already lived ' + str(calculate_my_decades(int(age))) + ' decades')
