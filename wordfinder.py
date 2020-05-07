
from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, filepath):
        """Creates a WordFinder object with an input dictionary file that has 1 word per line"""
        self.filepath = filepath
        self.words = self.read_words(filepath)
        print(f"{len(self.words)} words read")

    def read_words(self, filepath):
        """Helper function to read each line from filepath into the self.words list"""
        with open(filepath) as file:
            return file.read().split('\n')

    def random(self):
        """Returns a random word from the dictionary"""
        return choice(self.words)

    def to_string(self):
        """Returns a human readable string representation of the dictionary"""
        return f"WordFinder object with {len(self.words)} words"
