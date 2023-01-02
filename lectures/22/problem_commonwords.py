#
# Lecture 22 - Determine the `n' most common words in a text file
#
# Pedro Vasconcelos, 2023

from typing import List, Tuple, Dict

def text_to_words(txt: str) -> List[str]:
    """Clean up a a line of text and return a list of words."""
    my_substitutions = txt.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")
    # Translate the text now.
    cleaned_text = txt.translate(my_substitutions)
    trans = cleaned_text.split()
    return trans

def read_file_words(filename: str) -> Dict[str,int]:
    """Read through all lines in a file; return a dictionary of
    word counts."""
    counts : Dict[str,int] = dict()
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            for word in text_to_words(line):
                counts[word] = counts.get(word,0) + 1
    return counts

def common_words(filename: str, n: int) -> List[Tuple[str,int]]:
    """Read a file and determine the n most common words."""
    counts = read_file_words(filename)
    listofcounts = list(counts.items())
    listofcounts.sort(key=lambda p:-p[1])
    return listofcounts[:n]


if __name__=="__main__":
    #
    # determine the 20 most common words in "Alice In Wonderland"
    #
    wordcounts = common_words("AliceInWonderland.txt", 20)
    for word,count in wordcounts:
        print(word, '\t', count)
