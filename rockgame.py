import random

class RockPaperScissors:
    choices = ["rock", "paper", "scissors"]

    def __init__(self):
        self.player = None
        self.computer = None
    
    def get_player_choice(self):
        self.player = input("Enter rock, paper, scissors: ")
    
    def generate_computer_choice(self):
        self.computer = random.choice(self.choices)
    
    def decide_winner(self):
         if self.player == self.computer:
            return "It's a tie!"
         elif (self.player == "rock" and self.computer == "scissors"):
              return ' You Win'
         elif (self.player == "scissors" and self.computer == "paper"):
              return  ' You Win'
         elif (self.player == "paper" and self.computer == "rock"):
              return "You win!"
         else:
            return "You lose!" 
    
game = RockPaperScissors()
game.get_player_choice()
game.generate_computer_choice()
print(f'player choice is: {game.player}')
print(f'Computer choice is: {game.computer}')
print('***********************wineer*****************')
print(game.decide_winner())









