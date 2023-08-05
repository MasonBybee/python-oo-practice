"""Word Finder: finds random words from a dictionary."""
from random import randint


class WordFinder:
    def __init__(self, file):
        self.path = file
        self.words = self.get_words()
        self.print_word_count()

    def get_words(self):
        """Creates a list with all the words in a given file"""
        with open(self.path, 'r') as file:
            return [line.strip() for line in file]

    def print_word_count(self):
        """Prints the total word count"""
        print(f"{len(self.words)} words read")

    def random(self):
        """Returns a random word from the given file"""
        return self.words[randint(0, len(self.words) - 1)]