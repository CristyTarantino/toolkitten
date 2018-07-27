"""
Description - Week 1 homework for 1mwtt program
Author - Cristina Tarantino
Date - July 2018
"""

# https://docs.python.org/2/library/string.html
from string import ascii_lowercase, ascii_uppercase
import operator
import random


def get_input_number(msg):
    # try to convert the input in an integer
    try:
        user_number = int(input(msg))
    # if it is not possible acknowledge the user and continue to prompt him to insert a number
    except ValueError:
        print("\nThat wasn't a valid number!")
        return get_input_number(msg)
    # else execute the input manipulation and break the infinite loop
    else:
        return user_number

# DAY 1
# 1. Calculate a table for each letter in the alphabet from a-z,
# and count how many times each letter appears in `alice_in_wonderland.txt`
# (fancy word for counting stuff is "frequency distribution" - because you are counting the frequency of something)


def char_frequency_list_from_alphabet(text):
    # generate a list of the alphabet in Python
    char_frequency_list = []

    for c in ascii_lowercase:
        char_frequency_list.append([c, 0])

    # convert all to lowercase
    text = text.lower()

    # for each character in the text
    for char in char_frequency_list:
        # https://docs.python.org/2/library/string.html#string.count
        char[1] += text.count(char[0])

    return char_frequency_list


def char_frequency_list_only_present_alphas(text):
    char_frequency_list = []

    # convert all to lowercase
    text = text.lower()

    # for every char in text
    for t in text:
        # check if the current char is in the first index of each element in char_frequency_list
        visited_chars_list = [c[0] for c in char_frequency_list]
        # if is not in not been added yet and is a letter then add it to the frequency list
        if t not in visited_chars_list and t.isalpha():
            value = text.count(t)
            char_frequency_list.append([t, value])
        else:
            continue

    char_frequency_list = sorted(char_frequency_list)

    return char_frequency_list


# DAY 2

# 2. There is something small that needs fixing. Can you spot it and fix it? (Hint, we only want A-Z and a-z)
# original loop
# for i in range(65,65+2*26):
#     print(i, " stands for ", chr(i))

print("\nExercise Fix the loop for correct char range")

for i in range(65, 65 + 2 * 29):
    if 90 < i < 97:
        continue
    # Get the character given by an ASCII number
    print(i, " stand for ", chr(i))


# 3. numbers to letters. Make a function that prints A-Z and a-z

def numbers_to_letters():
    for c in range(65, 65 + 2 * 29):
        if 90 < c < 97:     # or if chr(c).isalpha():
            continue
        print(chr(c))


# 4. Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;))
# "I LOVE YOU" [ 73, , 76, ...]

def cypher_message():
    message = input("\nType a message for the love of your life: ")
    char_list = []

    for c in message:
        # Get the ASCII number of a character
        char_list.append(ord(c))

    return char_list


# 5. Write a function that does a ceaser cypher (Google), ask the user a number, and shift their message by that number.

def ceaser_cypher(function_verb, operation):
    TOTAL_ALPHABET_NUM = len(ascii_lowercase)
    LOWER_ALPHABET_LOW_OFFSET = ord(ascii_lowercase[0])
    LOWER_ALPHABET_UPP_OFFSET = ord(ascii_uppercase[0])

    shifting_num = get_input_number("\nPlease type a number that will be used for the shifting strategy: ")
    message = input("\nPlease type a message to be %s: " % function_verb)
    encrypted_message = ""

    for c in message:
        if c.isalpha():
            if c.islower():
                offset = LOWER_ALPHABET_LOW_OFFSET
            else:
                offset = LOWER_ALPHABET_UPP_OFFSET

            letter_to_number = ord(c) - offset
            encrypted_c = operation(letter_to_number, shifting_num) % TOTAL_ALPHABET_NUM
            encrypted_message += chr(encrypted_c + offset)
        else:
            encrypted_message += c

    return encrypted_message


def encryption_ceaser_cypher():
    return ceaser_cypher("encrypted", operator.add)


def decryption_ceaser_cypher():
    return ceaser_cypher("decrypted", operator.sub)


# 6. Write a function that prints out all elements of the below board,
# starting from the first element of the first line, till the end. Each line should be read from beginning to end.

M = "land"
o = "water"

world = [
            [o,o,o,o,o,o,o,o,o,o,o],
            [o,o,o,o,M,M,o,o,o,o,o],
            [o,o,o,o,o,o,o,o,M,M,o],
            [o,o,o,M,o,o,o,o,o,M,o],
            [o,o,o,M,o,M,M,o,o,o,o],
            [o,o,o,o,M,M,M,M,o,o,o],
            [o,o,o,M,M,M,M,M,M,M,o],
            [o,o,o,M,M,o,M,M,M,o,o],
            [o,o,o,o,o,o,M,M,o,o,o],
            [o,M,o,o,o,M,o,o,o,o,o],
            [o,o,o,o,o,o,o,o,o,o,o]
        ]


def print_board(board):
    for row in board:
        for item in row:
            print(item)

# def print_board(board):
#     for row in range(len(board)):
#         for item in range(len(board)):
#             print(board[item][row])


# 7. Now write a function that prints out all elements in reverse.
def print_reversed_board(board):
    for row in reversed(board):
        for item in reversed(row):
            print(item)


# 7. There is one small bug in the continent counter above.
# Can you find it and fix it? (Hint: change the world so that the continent borders the edge)


# 8. Write a function that generates an n x n sized board with either land or water chosen randomly.
def generate_random_board(n):
    L = "land"
    W = "water"

    world = [[random.choice([L, W]) for column in range(n)] for row in range(n)]

    return world


# 9. Run your continent counter for a 20 x 20 board. How long does it take to run?
# (If it runs quickly, try 30 x 30 ... 100 x 100 just be aware you might end up in a VERY LOOOONG WAIT)
# make sure you know how to break a running program as
# it may take a long time to complete and you might not have time to wait for it ;)


# 10. Write test coverage in unittest and/or trace for Continent Counter.

# DAY 3

# 11. Modify "a" for another name in my_dict.
# Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.


# 12. Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

# return a dictionary of the entire alphabet and the frequency of each letter
def char_frequency_dict_from_alphabet(text):
    # generate a dict of the alphabet in Python
    # The fromkeys() method creates a new dictionary
    # from the given sequence of elements with a value provided by the user.
    char_frequency_dict = dict.fromkeys(ascii_lowercase, 0)

    # convert all to lowercase
    text = text.lower()

    # for each character in the text
    for char in text:
        # if is present in the dictionary
        if char in char_frequency_dict:
            # increment its value of 1
            char_frequency_dict[char] += 1

    return char_frequency_dict


# return a dictionary of the letter present in the @param text and its frequency
def char_frequency_dict_only_present_alphas(text):
    char_frequency_dict = {}

    # convert all to lowercase
    text = text.lower()

    for char in text:
        if char not in char_frequency_dict.keys() and char.isalpha():
            value = text.count(char)
            char_frequency_dict[char] = value
        else:
            continue

    return char_frequency_dict


# 13. Create a dictionary with your own personal details, feel free to be creative and funny so for example,
# you could include key-value pairs with `quirky fact`, `fav quote`, `pet`. Practice adding, modifying, accessing.

print("\nExercise personal details dictionary")

who_am_i = {
    "name": "Cristina",
    "surname": "Tarantino",
    "hair": "brown",
    "eyes": "brown",
    "skin_type": "pail white",
    "pet": "cat",
    "fav_quote": "divide et impera",
    "quirky fact": "I have dyslexia and I can code",
    "children_num": 1,
    "marital_status": "married"
}

print(who_am_i)

# loop
for k, v in who_am_i.items():
    print(k, ":", v)

print(who_am_i.keys())
print(who_am_i.values())
print(len(who_am_i))

for i, k in enumerate(who_am_i):
    print(i, k)

del(who_am_i["skin_type"])

print(sorted(who_am_i))

who_am_i["skin_type"] = "ghost"

print(who_am_i)

who_am_i["skin_type"] = "pail white"

print(who_am_i)


# 14. Mapping with cities and states/regions in your country or some other country.


# 15. Find the Python documentation for dictionaries and try to do even more things to them.


# 16. Find out what you can't do with dictionaries. A big one is that they do not have order, so try playing with that.

# 17. Write a test to check the outcome of the alice_in_wonderfland task:
# one test for list of lists, and one test for dictionary output.


# 18. Review the chat reply of today's beautiful class
# interaction and instantiate a student variable for everyone who shared their dream.


# 19. Translate the real world 1MWTT student into a Student class,
# decide on all the attributes that would be meaningful.
# Hint: You can start with the DIY signup form https://memberportal.1millionwomentotech.com/diy
# but feel free to be creative and add/modify as you see it best! This is the REAL work of a creator
# to find the meaningful description of reality and translate it for computers.


# 20. Write some more songs using this and make sure you understand that you're passing a list of strings as the lyrics.


# 21. Put the lyrics in a separate variable, then pass that variable to the class to use instead.


# 22. See if you can hack on this and make it do more things.
# Don't worry if you have no idea how,
# just give it a try, see what happens. Break it, trash it, thrash it, you can't hurt it.

# 23. Search online for "object-oriented programming" and try to overflow your brain with what you read.
# Don't worry if it makes absolutely no sense to you. Half of that stuff makes no sense to me too.
