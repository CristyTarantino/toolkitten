"""
Description - Week 1 homework for 1mwtt program
Author - Cristina Tarantino
Date - July 2018
"""

# https://docs.python.org/2/library/string.html
from string import ascii_lowercase, ascii_uppercase
import operator
import random

# TODO test this
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

print("\nExercise Fix the loop for correct char range\n")

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


# 8. There is one small bug in the continent counter above.
# Can you find it and fix it? (Hint: change the world so that the continent borders the edge)
def continent_counter(world, column, row):
    if 0 < row < len(world) and 0 < column < len(world[0]):
        if world[row][column] != 'land':
            return 0

        size = 1

        # if  world[row][column] == 'land' => flag that land as counted
        world[row][column] += 'counted'

        # ...then we count all of the neighboring tiles
        # (and, of course, their neighbors by way of the recursion).​

        # row above left column
        size = size + continent_counter(world, column - 1, row - 1)
        # row above above column
        size = size + continent_counter(world, column,     row - 1)
        # row above right column
        size = size + continent_counter(world, column + 1, row - 1)

        # same row left column
        size = size + continent_counter(world, column - 1, row)
        # same row right column
        size = size + continent_counter(world, column + 1, row)

        # row below left column
        size = size + continent_counter(world, column - 1, row + 1)
        # row below below column
        size = size + continent_counter(world, column,     row + 1)
        # row below right column
        size = size + continent_counter(world, column + 1, row + 1)

        return size
    else:
        return 0


# 9. Write a function that generates an n x n sized board with either land or water chosen randomly.


def generate_random_board(n, m=None):
    L = "land"
    W = "water"

    if not m:
        m = n

    world = [[random.choice([L, W]) for column in range(m)] for row in range(n)]

    return world


# Personal exercise for practice.
# Find the largest two, and see whether they look like fun to play on.

# example output would be:
# {
#   'continent-row-3-column-3': 24,
#   'continent-row-8-column-2': 3,
#   'continent-row-4-column-1': 2,
#   'continent-row-1-column-9': 1
# }
# where key gives the coordinates of the beginning of the continent
# and value is the area that continent expands through
def find_continets(world):
    continents = {}

    for row in range(len(world)):
        for column in range(len(world[0])):
            curr_cont_size = continent_counter(world, row, column)
            if curr_cont_size:
                continents["continent-row-" + str(row) + "-column-" + str(column)] = curr_cont_size

    return continents


def find_largest_n_continents(world, n):
    continents = find_continets(world)

    largest_n_continents = {}

    if len(continents) < n:
        n = len(continents)

    if len(continents) >= n:
        # for item in range(n):
            # https://docs.python.org/3.7/library/stdtypes.html#list.sort
            # https://docs.python.org/3.7/library/stdtypes.html#dict.get
            sorted_continents = [(k, continents[k]) for k in sorted(continents, key=continents.get, reverse=True)]
            for item in range(n):
                largest_n_continents[sorted_continents[item][0]] = sorted_continents[item][1]

    return largest_n_continents


# 10. Run your continent counter for a 20 x 20 board. How long does it take to run?
# (If it runs quickly, try 30 x 30 ... 100 x 100 just be aware you might end up in a VERY LOOOONG WAIT)
# make sure you know how to break a running program as
# it may take a long time to complete and you might not have time to wait for it ;)

# I have uncommented the lines below to avoid program crashing
# recursions are good looking but have a great time and space complexity
# and they can cause stack overflows which then causes the applications to crash
# recursion are implemented using memory stack. A stack has a size,
# once the recursion uses more space than the stack has available we incur in stack overflow

# generate_random_board(20)
# generate_random_board(30)

# 11. Write test coverage in unittest and/or trace for Continent Counter.

# please look at soc_wk2_cert_cristina_tarantino.test.py

# DAY 3

# 12. Modify "a" for another name in my_dict.
# Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.

print("\nExercise Modify key name in my_dict\n")

my_dict = {
    "a": 35000,
    "b": 8000,
    "z": 450
}

my_dict["new_key"] = my_dict["a"]

del(my_dict["a"])

print(my_dict)


# 13. Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

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


# 14. Create a dictionary with your own personal details, feel free to be creative and funny so for example,
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

print("\n", who_am_i)

# loop
for k, v in who_am_i.items():
    print(k, ":", v)

print("\n", who_am_i.keys())
print("\n", who_am_i.values())
print("\n", len(who_am_i), "\n")

for i, k in enumerate(who_am_i):
    print(i, k)

del(who_am_i["skin_type"])

print("\n", sorted(who_am_i))

who_am_i["skin_type"] = "ghost"

print("\n", who_am_i)

who_am_i["skin_type"] = "pail white"

print("\n", who_am_i)


# 15. Mapping with cities and states/regions in your country or some other country.

print("\nExercise Mapping with cities and states/regions in your country or some other country")

italian_regions_to_county = {
    "Abruzzo": "L'Aquila",
    "Basilicata": "Potenza",
    "Calabria": "Catanzaro",
    "Campania": "Napoli",
    "Emilia-Romagna": "Bologna",
    "Friuli-Venezia Giulia": "Trieste",
    "Lazio": "Roma",
    "Liguaria": "Genova",
    "Lombardia": "Milano",
    "Marche": "Ancona",
    "Molise": "Campobasso",
    "Piemonte": "Torino",
    "Puglia": "Bari",
    "Sardegna": "Cagliari",
    "Sicilia": "Palermo",
    "Toscana": "Firenze",
    "Trentino-Alto Adige": "Trento",
    "Umbria": "Perugia",
    "Valle d'Aosta": "Aosta",
    "Veneto": "Venezia"
}

italian_county_to_abbreviations = {
    "L'Aquila": "AQ",
    "Potenza": "PZ",
    "Catanzaro": "CZ",
    "Napoli": "NA",
    "Bologna": "BO",
    "Trieste": "TS",
    "Roma": "RM",
    "Genova": "GE",
    "Milano": "MI",
    "Ancona": "AN",
    "Campobasso": "CB",
    "Torino": "TO",
    "Bari": "BA",
    "Cagliari": "CA",
    "Palermo": "PA",
    "Firenze": "FI",
    "Trento": "TN",
    "Perugia": "PG",
    "Aosta": "AO",
    "Venezia": "VE"
}

print()
for region, county in italian_regions_to_county.items():
    print("%s has the city %s" % (region, county))

print()
for county, abbrv in italian_county_to_abbreviations.items():
    print("%s is abbreviated as %s" % (county, abbrv))

print()
for region, county in italian_regions_to_county.items():
    # Return the value for key if key is in the dictionary, else default.
    # If default is not given, it defaults to None, so that this method never raises a KeyError.
    print("%s has the city %s which is abbreviated as %s" % (region, county, italian_county_to_abbreviations.get(county)))


# 16. Find the Python documentation for dictionaries and try to do even more things to them.


print("\nExercise Python documentation for dictionaries")


# ways of initializing
a = dict(one=1, two=2, three=3)
b = {"one": 1, "two": 2, "three": 3}
c = dict(zip(["one", "two", "three"], [1, 2, 3]))
d = dict([("two", 2), ("one", 1), ("three", 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

if a == b == c == d == e:
    print("lots of ways of initializing dictionaries")


# check for keys
if "four" in a:
    print("there is no number 4 in the dictionary")


# get keys
print(a.get("four"))
print(a.get("one"))

print(a.items())

# pop
print("\nRemove one with pop")
print(a.pop("one"))
print(a)

print("\nAdd the pop key")
print(a.setdefault("one"))
print(a)

tmp_a = {"twenty-six": 26, "one": 1}
print(a.update(tmp_a))
print(a)


# 17. Find out what you can't do with dictionaries. A big one is that they do not have order, so try playing with that.
def sort_dict_by_numeric_value(dictionary):
    sorted_dictionary = {}

    # https://docs.python.org/3.7/library/stdtypes.html#list.sort
    # sorted(dictionary, key=dictionary.get, reverse=True)
    # returns the array of keys sorted my value. Do to that we use
    # the keyword key (sortBy) that specifies a function of one argument that is used to extract a
    # comparison key from each list element
    for k, v in [(k, dictionary[k]) for k in sorted(dictionary, key=dictionary.get, reverse=True)]:
        sorted_dictionary[k] = v

    return sorted_dictionary


def sort_dict_by_key(dictionary):
    sorted_dictionary = {}
    for key in sorted(dictionary):
        sorted_dictionary[key] = dictionary[key]

    return sorted_dictionary


# 18. Write a test to check the outcome of the alice_in_wonderfland task:
# one test for list of lists, and one test for dictionary output.

# Please have a look at all the tests in the file soc_wk2_cert_cristina_tarantino.test.py


# 19. Review the chat reply of today's beautiful class
# interaction and instantiate a student variable for everyone who shared their dream.


# 20. Translate the real world 1MWTT student into a Student class,
# decide on all the attributes that would be meaningful.
# Hint: You can start with the DIY signup form https://memberportal.1millionwomentotech.com/diy
# but feel free to be creative and add/modify as you see it best! This is the REAL work of a creator
# to find the meaningful description of reality and translate it for computers.


# 21. Write some more songs using this and make sure you understand that you're passing a list of strings as the lyrics.


# 22. Put the lyrics in a separate variable, then pass that variable to the class to use instead.


# 23. See if you can hack on this and make it do more things.
# Don't worry if you have no idea how,
# just give it a try, see what happens. Break it, trash it, thrash it, you can't hurt it.

# 24. Search online for "object-oriented programming" and try to overflow your brain with what you read.
# Don't worry if it makes absolutely no sense to you. Half of that stuff makes no sense to me too.


# install pip, NLTK, Anaconda and Jupyter Notebook

# DONE although it's hard to demonstrate I have done it


# from http://www.nltk.org/book/ch01.html _☼
# Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?
# http://jfine-python-classes.readthedocs.io/en/latest/subclass-int.html
