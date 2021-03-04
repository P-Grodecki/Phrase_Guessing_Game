# Import your Game class
from phrasehunter import game
from phrasehunter import phrase

# Create your Dunder Main statement.
if __name__=='__main__':
    # Inside Dunder Main:
    ## Create an instance of your Game class
    the_game = game.Game()
    print(the_game.the_phrase)
    
    selected_phrase = phrase.Phrase()
    print(selected_phrase.a_phrase)

    ## Start your game by calling the instance method that starts the game loop
