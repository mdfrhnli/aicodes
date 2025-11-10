# pip install easyAI
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class TicTacToe(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.board = [0 for _ in range(9)]
        self.current_player = 1

    def possible_moves(self):
        return [str(i + 1) for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player

    def unmake_move(self, move):
        self.board[int(move) - 1] = 0

    def lose(self):
        opponent = 3 - self.current_player
        combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        return any(all(self.board[i] == opponent for i in combo) for combo in combos)

    def is_over(self):
        return self.lose() or all(self.board[i] != 0 for i in range(9))

    def show(self):
        symbols = ['.', 'X', 'O']
        for i in range(0,9,3):
            print(' '.join(symbols[self.board[i+j]] for j in range(3)))

    def scoring(self):
        return -100 if self.lose() else 0

if __name__ == "__main__":
    game = TicTacToe([Human_Player(), AI_Player(Negamax(4))])
    game.play()
