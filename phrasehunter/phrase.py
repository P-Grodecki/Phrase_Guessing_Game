# Create your Phrase class logic here.
class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        guesses = [letter.lower() for letter in guesses]
        for letter in self.phrase:
            if letter in guesses:
                print(f'{letter}', end=" ")
            elif letter == ' ':
                print(' ', end=" ")
            else:
                print('_', end=" ")
        print("",end='\n')

    def check_guess(self, guess):
        return guess.lower() in self.phrase

    def check_complete(self, guesses):
        guesses = [letter.lower() for letter in guesses] 
        no_space_phrase = self.phrase.replace(" ",'')
        if set(no_space_phrase).intersection(set(guesses)) == set(no_space_phrase):
            return True
        else:
            return False

if __name__ == '__main__':
    test_phrase = Phrase("Life is like a box of chocolates")
    print(test_phrase.phrase)
    print(str(test_phrase.check_guess('a')))
