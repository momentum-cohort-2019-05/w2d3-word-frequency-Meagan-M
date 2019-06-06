STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass
    # 1) use open to read in a text file (store the read file in a variable)

    with open(file) as my_file:
        my_file = my_file.read()

        print(my_file)
 # -remove punctuation
#  def clean_text(text):
    # """
    # Given a text, return the text with no spaces or punctuation and all lowercased.
    # """
    # new_text = ""
    # text = text.lower()
    # for character in text:
    #     if character.isalpha():p
    #         new_text = new_text + character
    # return new_text


    # 2) calculate the frequency of words
       

        # -all words are lowercase
        # -remove stop words
        # -keep a count of how often a word is used (use a dictionary)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
