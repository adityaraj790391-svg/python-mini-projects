# Step-1 Import the important libraries

from spellchecker import SpellChecker

# Step-2 Creating the app class

class SpellingCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            corrected_words.append(corrected_word)

    

    

    

    