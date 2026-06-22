# Step-1 Import the important libraries

from spellchecker import SpellChecker

# Step-2 Creating the app class

class SpellingCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

# Step-3 Taking input from the user

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"Correcting '{word}' to '{corrected_word}'")
                corrected_words.append(corrected_word)

# Step-4 Returning the corrected text

        return ' '.join(corrected_words)

# Step-5 Running the app

def run(self):
    print("\n---Spelling Checker App---")

    while True:

        text = input("\nEnter a sentence (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Exiting the app. Goodbye!")
            break

        corrected_text = self.correct_text(text)
        print(f"Corrected Text: {corrected_text}")


# Step-6 Main function to run the app

if __name__ == "__main__":
    app = SpellingCheckerApp()
    app.run()





            
            

    

    

    