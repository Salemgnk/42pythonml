import string
import sys

def text_analyzer(input):

    """
    Analyzes a given text and displays the sums of its upper-case characters, lower-case characters, punctuation characters, and spaces.

    Parameters:
    input (str): The text to be analyzed.

    Returns:
    None
    """

    upper_counter = 0
    lower_counter = 0
    punctuation_mark = 0
    spaces = 0
    num_char = len(input)

    for i in input:
        if i.isupper():
            upper_counter += 1
        elif i.islower():
            lower_counter += 1
        elif i == ' ':
            spaces += 1
        elif i in string.punctuation:
            punctuation_mark += 1

    print(f"The text contains {num_char} character(s):")
    print(f"- {upper_counter} upper letter(s)")
    print(f"- {lower_counter} lower letter(s)")
    print(f"- {punctuation_mark} punctuation mark(s)")
    print(f"- {spaces} space(s)")
    return

def main():
    if len(sys.argv) == 1:
        return
    elif len(sys.argv) > 2:
        print("Error: too many arguments")
    else:
        text_analyzer(sys.argv[1])

if __name__ == "__main__":
    main()