import string


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


filename = "../alice_in_wonderland.txt"
# source http://www.gutenberg.org/files/11/11-0.txt


# open the file in read only mode
# source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
with open(filename) as f:
    read_data = f.read()
f.closed

# print(count_letters(raw))
for key, value in count_letters(read_data).items():
    print("Number of letter " + key + ": " + str(value))
