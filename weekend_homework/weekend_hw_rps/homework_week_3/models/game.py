class Game():

    def __init__(self) -> None:
        pass
    
    # def __init__(self, player1, player2):
    #     self.player1 = player1
    #     self.player2 = player2

    def play_game(self, player1, player2):
        if player1.choice.lower() == "rock" and player2.choice.lower() == "scissors":
            return player1
        elif player1.choice.lower() == "rock" and player2.choice.lower() == "paper":
            return player2
        elif player1.choice.lower() == "scissors" and player2.choice.lower() == "rock":
            return player2
        elif player1.choice.lower() == "scissors" and player2.choice.lower() == "paper":
            return player1
        elif player1.choice.lower() == "paper" and player2.choice.lower() == "scissors":
            return player2
        elif player1.choice.lower() == "paper" and player2.choice.lower() == "rock":
            return player1
        else:
            return None