"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open("green-eggs.txt").read()
    print(file)
    print(type(file))


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
    """

# splitting text into words of strings
    file = open("green-eggs.txt").read()
    split_string = file.split()

    chains = {}
    list_tuples = []

# appended tuple into a list
    for i in range(len(split_string) - 1):
        list_tuples.append((split_string[i], split_string[i + 1]))

    # print(list_tuples)

# make dictionary
    value = []
# correct value

    # for loop thru all tuples with duplicates
    for i in range(len(list_tuples) - 2):
        if list_tuples[i] in chains:
            chains[list_tuples[i]] += [list_tuples[i + 1][1]]
        else:
            chains[list_tuples[i]] = [list_tuples[i + 1][1]]

    return chains

    #  print(chains)
    # for key in chains:
    #     print(key, chains[key])


def make_text(chains):
    """Return text from chains."""

    make_chains()

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

