# Import your Game class
from phrasehunter import phrase
from phrasehunter import game

def print_phrase(phrase_object):
    print(f'The phrase is: {phrase_object.phrase}')



# Create your Dunder Main statement.
if __name__=='__main__':
    """     # Inside Dunder Main:
    ## Create an instance of your Game class
    the_game = game.Game()
    
    # test code - show the created phrases
    print('\n')
    print('\n'.join([_.phrase for _ in the_game.phrases]))

    # test code - test random output
    print('\n')
    for _ in range(5):
        print_phrase(the_game.get_random_phrase())

    # Unpacking and such.
    selected_phrase = phrase.Phrase("I like abby")
    print(selected_phrase.phrase)
    
    the_game.welcome()
    print(f'The Active Phrase: {the_game.active_phrase.phrase}')
    user_guesses = ['A', 'C', 'W', 'G', 'H', 'O', 'L']
    the_game.active_phrase.display(user_guesses)
    ## Start your game by calling the instance method that starts the game loop """

    the_game = game.Game()
    the_game.start()
    #print(f'\nThe Active Phrase: {the_game.active_phrase.phrase}')
    #user_guesses = ['A', 'C', 'W', 'G', 'H', 'O', 'L']
