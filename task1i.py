class TableSoccer:
    def __init__(self):
        self.ball_position = 5  # 0..10
        self.goal_position = 10
        self.opponent_position = 7

    def move_player(self, direction):
        if direction == 'left' and self.ball_position > 0:
            self.ball_position -= 1
        elif direction == 'right' and self.ball_position < 10:
            self.ball_position += 1
        print(f"Ball moved {direction} to position {self.ball_position}")

    def kick_ball(self):
        if self.ball_position >= self.opponent_position:
            print("GOAL!")
        else:
            print("Missed! Ball intercepted by opponent.")

    def sensor(self):
        return self.ball_position, self.opponent_position

    def agent(self):
        ball, opponent = self.sensor()
        print(f"Ball at: {ball}, Opponent at: {opponent}")

        # Move right until reaching opponent (or border)
        while self.ball_position < self.opponent_position and self.ball_position < 10:
            self.move_player('right')

        self.kick_ball()

if __name__ == "__main__":
    game = TableSoccer()
    game.agent()
