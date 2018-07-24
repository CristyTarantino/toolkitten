import string

# DAY 1
# 1. Calculate a table for each letter in the alphabet from a-z,
# and count how many times each letter appears in `alice_in_wonderland.txt`
# (fancy word for counting stuff is "frequency distribution" - because you are counting the frequency of something)


def count_letters(text):
    # generate a dict of the alphabet in Python
    # The fromkeys() method creates a new dictionary
    # from the given sequence of elements with a value provided by the user.
    char_frequency_list = dict.fromkeys(string.ascii_lowercase, 0)

    text = text.lower()

    # for each character in the text
    for char in text:
        # if is present in the dictionary
        if char in char_frequency_list:
            # increment its value of 1
            char_frequency_list[char] += 1

    return char_frequency_list


# DAY 2
# 2. numbers to letters. Make a function that prints A-Z and a-z
# for i in range(65, 65+2*26)
#     print(i, " stand for ", chr(i))

# 3. Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;))
#
# "I LOVE YOU" [ 73, , 76, ...]

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
