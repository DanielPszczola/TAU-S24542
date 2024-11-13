import random

class GameOverException(Exception):
    pass

class Game:
    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.start = self.random_edge_position()
        self.stop = self.random_edge_position()
        while self.stop == self.start or self.are_adjacent(self.start, self.stop):
            self.stop = self.random_edge_position()
        self.board[self.start[0]][self.start[1]] = 'A'
        self.board[self.stop[0]][self.stop[1]] = 'B'
        self.add_obstacles()
        self.player_position = self.start

    def random_edge_position(self):
        if random.choice([True, False]):
            return (0, random.randint(0, self.cols - 1))
        else:
            return (random.randint(0, self.rows - 1), 0)

    def are_adjacent(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1

    def add_obstacles(self):
        num_obstacles = (self.rows * self.cols) // 4
        for _ in range(num_obstacles):
            x, y = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            while self.board[x][y] != ' ':
                x, y = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            self.board[x][y] = 'X'

    def move(self, direction):
        if direction == 'right':
            new_pos = self.move_right(self.player_position)
        elif direction == 'left':
            new_pos = self.move_left(self.player_position)
        elif direction == 'up':
            new_pos = self.move_up(self.player_position)
        elif direction == 'down':
            new_pos = self.move_down(self.player_position)
        else:
            return

        if new_pos != self.player_position:
            self.board[self.player_position[0]][self.player_position[1]] = ' '
            self.player_position = new_pos
            self.board[self.player_position[0]][self.player_position[1]] = 'P'

    def move_right(self, position):
        if position[1] + 1 < self.cols:
            if self.board[position[0]][position[1] + 1] == 'B':
                print("Wygrana! Dotarłeś do punktu B!")
                raise GameOverException("Win")
            if self.board[position[0]][position[1] + 1] == 'X':
                print("Przegrana! Trafiłeś na przeszkodę!")
                raise GameOverException("Loss")
            return (position[0], position[1] + 1)
        else:
            print("Przegrana! Wyszedłeś poza planszę!")
            raise GameOverException("Loss")

    def move_left(self, position):
        if position[1] - 1 >= 0:
            if self.board[position[0]][position[1] - 1] == 'B':
                print("Wygrana! Dotarłeś do punktu B!")
                raise GameOverException("Win")
            if self.board[position[0]][position[1] - 1] == 'X':
                print("Przegrana! Trafiłeś na przeszkodę!")
                raise GameOverException("Loss")
            return (position[0], position[1] - 1)
        else:
            print("Przegrana! Wyszedłeś poza planszę!")
            raise GameOverException("Loss")

    def move_up(self, position):
        if position[0] - 1 >= 0:
            if self.board[position[0] - 1][position[1]] == 'B':
                print("Wygrana! Dotarłeś do punktu B!")
                raise GameOverException("Win")
            if self.board[position[0] - 1][position[1]] == 'X':
                print("Przegrana! Trafiłeś na przeszkodę!")
                raise GameOverException("Loss")
            return (position[0] - 1, position[1])
        else:
            print("Przegrana! Wyszedłeś poza planszę!")
            raise GameOverException("Loss")

    def move_down(self, position):
        if position[0] + 1 < self.rows:
            if self.board[position[0] + 1][position[1]] == 'B':
                print("Wygrana! Dotarłeś do punktu B!")
                raise GameOverException("Win")
            if self.board[position[0] + 1][position[1]] == 'X':
                print("Przegrana! Trafiłeś na przeszkodę!")
                raise GameOverException("Loss")
            return (position[0] + 1, position[1])
        else:
            print("Przegrana! Wyszedłeś poza planszę!")
            raise GameOverException("Loss")

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

if __name__ == "__main__":
    game = Game()
    while True:
        game.display_board()
        move = input("Enter move (right, left, up, down): ")
        try:
            game.move(move)
        except GameOverException as e:
            print(f"Game Over: {e}")
            break
