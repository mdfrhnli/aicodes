import numpy as np
import random

class Game2048:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        self.board = np.zeros((4, 4), dtype=int)
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty_cells = list(zip(*np.where(self.board == 0)))
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = 2 if random.random() < 0.9 else 4

    def compress(self, row):
        new_row = row[row != 0]
        new_row = np.pad(new_row, (0, 4 - len(new_row)))
        return new_row

    def merge(self, row):
        for i in range(3):
            if row[i] != 0 and row[i] == row[i+1]:
                row[i] *= 2
                self.score += row[i]
                row[i+1] = 0
        return row

    def move_left(self):
        moved = False
        new_board = np.zeros((4, 4), dtype=int)
        for i in range(4):
            row = self.compress(self.board[i])
            row = self.merge(row)
            row = self.compress(row)
            new_board[i] = row
            if not np.array_equal(row, self.board[i]):
                moved = True
        self.board = new_board
        return moved

    def move_right(self):
        self.board = np.fliplr(self.board)
        moved = self.move_left()
        self.board = np.fliplr(self.board)
        return moved

    def move_up(self):
        self.board = self.board.T
        moved = self.move_left()
        self.board = self.board.T
        return moved

    def move_down(self):
        self.board = self.board.T
        moved = self.move_right()
        self.board = self.board.T
        return moved

    def is_game_over(self):
        if np.any(self.board == 0):
            return False
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j+1] or self.board[j][i] == self.board[j+1][i]:
                    return False
        return True

    def display(self):
        print("Score:", self.score)
        print(self.board)

def simple_ai(game):
    moves = [game.move_left, game.move_up, game.move_right, game.move_down]
    while not game.is_game_over():
        moved = False
        for move in moves:
            if move():
                game.add_random_tile()
                game.display()
                moved = True
                break
        if not moved:
            break
    print("Game Over! Final Score:", game.score)

if __name__ == "__main__":
    g = Game2048(seed=42)
    g.display()
    simple_ai(g)
