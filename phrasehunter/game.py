
# Create your Game class logic in here.
# Handle Imports
import random
if __name__=='__main__':
    import phrase
else:
    from phrasehunter import phrase

class Game():
    #This is the game class which will manage the functioning of the game.    
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = []

    def create_phrases(self):
        phrase_options = []
        phrase_options.append(phrase.Phrase("My name is Patrick"))
        phrase_options.append(phrase.Phrase("Yellow is the color of my house"))
        phrase_options.append(phrase.Phrase("This is an example phrase"))
        phrase_options.append(phrase.Phrase("The quick red fox jumped over the lazy brown dog"))
        phrase_options.append(phrase.Phrase("Jake cracked the safe"))
        return phrase_options

    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print('-'*50 + '\n       Welcome to the phrase guessing game.\n' + '-'*50)

    def start(self):
        self.welcome()
        print(f'Number missed: {self.missed}')
        self.active_phrase.display(self.guesses)
        user_guess = self.get_guess()
        self.guesses.append(user_guess)
        self.active_phrase.display(self.guesses)

    def get_guess(self):
        # Prompt user for their next guess.
        # If not a letter, then re-enter guess.
        while True:
            next_guess = input('Enter your next guess: ')
            if next_guess.isalpha():
                if len(next_guess) > 1:
                    print('Guess must be a single letter only. Try again.')
                else:
                    return next_guess
                    break
            else:
                print('Guess must be a single letter only. Try again.')

            

    
    
    
    # def show_game(self):
    #     # This method will show the game
    #     pass

    # def check_game_over(self):
    #     # This method will check if the game is over
    #     pass

    # def user_interaction(self):
    #     # This method will handle user interactions
    #     pass


if __name__=='__main__':
    the_game = Game()
    #the_game.create_phrases()
    #phrase_list = the_game.create_phrases()
    print(the_game.the_phrase)
    print(the_game.phrases[1].phrase)
    #print(phrase_list[3].phrase)