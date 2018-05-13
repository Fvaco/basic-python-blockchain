# 1) Create two variables – one with your name and one with your age

name = "Iván"
age = 29

# 2) Create a function which prints your data as one string


def print_data():
    print(name + ' has ' + str(age) + ' years old')


print_data()
# 3) Create a function which prints ANY data (two arguments) as one string

def print_data_with_arguments(name, age):
    print(name + ' has ' + age + ' years old')


print_data_with_arguments(input('Enter your name: '),
                          input('Enter your age: '))

# 4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)


def calculate_my_decades():
    return int(age / 10)


print('You already lived ' + str(calculate_my_decades()) + ' decades')
