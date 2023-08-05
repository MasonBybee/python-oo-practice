from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):

    def get_words(self):
        """Filter out lines starting with '#' and empty lines from the words list."""
        words = super().get_words()
        return [word for word in words if word and not word.startswith('#')]