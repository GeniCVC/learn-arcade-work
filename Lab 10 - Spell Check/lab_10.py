import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# Binary Search Function
def binary_search(word, dictionary_list):
    low = 0
    high = len(dictionary_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if dictionary_list[mid] == word:
            return True
        elif dictionary_list[mid] < word:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Main Function
def main():
    """ Read in lines from a file """
    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("dictionary.txt")

    # Create an empty list to store our names
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Add the name to the list
        dictionary_list.append(line.strip())

    # Closes file
    my_file.close()


# Linear Search
    print("--- Linear Search ---")

    # Open file, and automatically close when we exit this block.
    with open("AliceInWonderLand200.txt") as story:
        line_number = 0
        # Loop through each line in the file like a list
        for line in story:
            line_number += 1
            word_list = split_line(line)  # Split the line into words
            for word in word_list:
                capitalized_word = word.upper()  # Convert all letters to uppercase
                if capitalized_word in dictionary_list:
                    pass
                else:
                    print(f"Word {capitalized_word} is not in the dictionary. Found on line {line_number}")

# Binary Search
    print("--- Binary Search ---")

    # Open file again to reset the pointer
    with open("AliceInWonderLand200.txt") as story:
        line_number = 0
        for line in story:
            line_number += 1
            word_list = split_line(line)  # Split the line into words
            for word in word_list:
                capitalized_word = word.upper()  # Convert all letters to uppercase
                if not binary_search(capitalized_word, dictionary_list):
                    print(f"Word '{capitalized_word}' is not in the dictionary. Found on line {line_number}")


main()
