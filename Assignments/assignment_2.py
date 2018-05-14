CONDITION_LONGER_THAN_5_CHARACTERS = 0
CONDITION_CONTAINS_N = 1

names = ['Max', 'Linda', 'Martha', 'Ivan', 'Raúl',
         'Oscar', 'Dimitri', 'Joel', 'Natasha', 'Caroline']


def contains_n(name):
    return 'n' in name or 'N' in name


def print_name_line(name):
    print(name + ' (' + str(len(name)) + ')')


def print_section_title(title_message):
    print('-'*30)
    print(title_message)
    print('-'*30)


def print_names(conditions=[]):
    if CONDITION_LONGER_THAN_5_CHARACTERS in conditions:
        if CONDITION_CONTAINS_N in conditions:
            for name in names:
                if(contains_n(name) and len(name) > 5):
                    print_name_line(name)
        else:
            for name in names:
                if(len(name) > 5):
                    print_name_line(name)
    else:
        for name in names:
            print_name_line(name)


# 1) Create a list of names and use a for loop to output the length of each name (len() ).
print_section_title('Printing all names (' + str(len(names))+')')
print_names()


# 2) Add an if check inside the loop to only output names longer than 5 characters.
print_section_title('Printing only names longer than 5 characters')
print_names([CONDITION_LONGER_THAN_5_CHARACTERS])

# 3) Add another if  check to see whether a name includes a “n”  or “N”  character.
print_section_title(
    "Printing only names longer than 5 characters AND includes a 'N' or 'n'")
print_names([CONDITION_LONGER_THAN_5_CHARACTERS, CONDITION_CONTAINS_N])
# 4) Use a while  loop to empty the list of names (via pop() )
print_section_title('Clearing names list')
while len(names) > 0:
    names.pop()
else:
    print(names)
