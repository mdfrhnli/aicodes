# pip install easyAI
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class Nim(TwoPlayerGame):
    def __init__(self, players, pile=20):
        self.players = players
        self.current_player = 1
        self.pile = pile

    def possible_moves(self):
        return [str(i) for i in range(1, min(4, self.pile) + 1)]

    def make_move(self, move):
        self.pile -= int(move)

    def win(self):
        return self.pile <= 0

    def is_over(self):
        return self.win()

    def show(self):
        print(f"Pile: {self.pile}")

    def scoring(self):
        return 100 if self.win() else 0

if __name__ == "__main__":
    Nim([Human_Player(), AI_Player(Negamax(4))], pile=20).play()
