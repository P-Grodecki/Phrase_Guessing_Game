# Create your Game class logic in here.

class Game():
    #This is the game class which will manage the functioning of the game.
    #pass
    def __init__(self):
        self.the_phrase = "Hi There from the Game Class"

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

    print(the_game.the_phrase)