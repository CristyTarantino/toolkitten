"""
Description - Week 1 homework for 1mwtt program
Author - Cristina Tarantino
Date - July 2018
"""

# https://docs.python.org/2/library/string.html
import string

# DAY 1
# 1. Calculate a table for each letter in the alphabet from a-z,
# and count how many times each letter appears in `alice_in_wonderland.txt`
# (fancy word for counting stuff is "frequency distribution" - because you are counting the frequency of something)


def count_letters_list(text):
    # generate a list of the alphabet in Python
    char_frequency_list = []

    for c in string.ascii_lowercase:
        char_frequency_list.append([c, 0])

    text = text.lower()

    # for each character in the text
    for char in char_frequency_list:
        # https://docs.python.org/2/library/string.html#string.count
        char[1] += text.count(char[0])

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
        if 90 < c < 97:
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


# 4. Write a function that does a ceaser cypher (Google), ask the user a number, and shift their message by that number.


# 5. Write a function that prints out all elements of the above board,
# starting from the first element of the first line, till the end. Each line should be read from beginning to end.


# 6. Now write a function that prints out all elements in reverse.


# 7. There is one small bug in the continent counter above.
# Can you find it and fix it? (Hint: change the world so that the continent borders the edge)


# 8. Write a function that generates an n x n sized board with either land or water chosen randomly.


# 9. Run your continent counter for a 20 x 20 board. How long does it take to run?
# (If it runs quickly, try 30 x 30 ... 100 x 100 just be aware you might end up in a VERY LOOOONG WAIT)
# make sure you know how to break a running program as
# it may take a long time to complete and you might not have time to wait for it ;)


# 10. Write test coverage in unittest and/or trace for Continent Counter.

# DAY 3

# 11. Modify "a" for another name in my_dict.
# Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.


# 12. Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.
def count_letters_dict(text):
    # generate a dict of the alphabet in Python
    # The fromkeys() method creates a new dictionary
    # from the given sequence of elements with a value provided by the user.
    char_frequency_dict = dict.fromkeys(string.ascii_lowercase, 0)

    text = text.lower()

    # for each character in the text
    for char in text:
        # if is present in the dictionary
        if char in char_frequency_dict:
            # increment its value of 1
            char_frequency_dict[char] += 1

    return char_frequency_dict


# 13. Create a dictionary with your own personal details, feel free to be creative and funny so for example,
# you could include key-value pairs with `quirky fact`, `fav quote`, `pet`. Practice adding, modifying, accesing.


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
