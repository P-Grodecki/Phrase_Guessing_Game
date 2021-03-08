# Create your Phrase class logic here.
class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        guesses = [letter.upper() for letter in guesses]
        for letter in self.phrase:
            letter = letter.upper()
            if letter in guesses:
                print(f'{letter}', end=" ")
            elif letter == ' ':
                print(' ', end=" ")
            else:
                print('_', end=" ")
        print("",end='\n')

    


if __name__ == '__main__':
    phrase = Phrase("Life is like a box of chocolates")
    print(phrase_to_show.phrase)