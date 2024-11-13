import unittest
from game import Game, GameOverException

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_board_initialization(self):
        self.assertEqual(len(self.game.board), self.game.rows)
        self.assertEqual(len(self.game.board[0]), self.game.cols)
        self.assertIn('A', [cell for row in self.game.board for cell in row])
        self.assertIn('B', [cell for row in self.game.board for cell in row])
        self.assertNotEqual(self.game.start, self.game.stop)
        self.assertFalse(self.game.are_adjacent(self.game.start, self.game.stop))

    def test_random_edge_position(self):
        pos = self.game.random_edge_position()
        self.assertTrue(pos[0] == 0 or pos[1] == 0 or pos[0] == self.game.rows-1 or pos[1] == self.game.cols-1)

    def test_move_right(self):
        start_position = self.game.player_position
        if start_position[1] + 1 < self.game.cols and self.game.board[start_position[0]][start_position[1] + 1] not in ['X', 'B']:
            new_position = self.game.move_right(start_position)
            self.assertEqual(new_position, (start_position[0], start_position[1] + 1))
        else:
            with self.assertRaises(GameOverException):
                self.game.move_right(start_position)

    def test_move_left(self):
        start_position = self.game.player_position
        if start_position[1] - 1 >= 0 and self.game.board[start_position[0]][start_position[1] - 1] not in ['X', 'B']:
            new_position = self.game.move_left(start_position)
            self.assertEqual(new_position, (start_position[0], start_position[1] - 1))
        else:
            with self.assertRaises(GameOverException):
                self.game.move_left(start_position)

    def test_move_up(self):
        start_position = self.game.player_position
        if start_position[0] - 1 >= 0 and self.game.board[start_position[0] - 1][start_position[1]] not in ['X', 'B']:
            new_position = self.game.move_up(start_position)
            self.assertEqual(new_position, (start_position[0] - 1, start_position[1]))
        else:
            with self.assertRaises(GameOverException):
                self.game.move_up(start_position)

    def test_move_down(self):
        start_position = self.game.player_position
        if start_position[0] + 1 < self.game.rows and self.game.board[start_position[0] + 1][start_position[1]] not in ['X', 'B']:
            new_position = self.game.move_down(start_position)
            self.assertEqual(new_position, (start_position[0] + 1, start_position[1]))
        else:
            with self.assertRaises(GameOverException):
                self.game.move_down(start_position)

    def test_victory_condition(self):
        # Ustawiamy pozycję gracza tuż obok punktu B
        if self.game.stop[1] > 0:
            self.game.player_position = (self.game.stop[0], self.game.stop[1] - 1)
            direction = 'right'
        else:
            self.game.player_position = (self.game.stop[0] - 1, self.game.stop[1])
            direction = 'down'
        
        with self.assertRaises(GameOverException) as cm:
            self.game.move(direction)
        self.assertEqual(cm.exception.args[0], "Win")

    def test_loss_condition(self):
        obstacle_position = next((x, y) for x, row in enumerate(self.game.board) for y, cell in enumerate(row) if cell == 'X')
        self.game.player_position = (obstacle_position[0], obstacle_position[1] - 1 if obstacle_position[1] > 0 else obstacle_position[1] + 1)
        with self.assertRaises(GameOverException) as cm:
            self.game.move('right' if self.game.player_position[1] < obstacle_position[1] else 'left')
        self.assertEqual(cm.exception.args[0], "Loss")

    def test_out_of_bounds_condition(self):
        self.game.player_position = (0, 0)
        with self.assertRaises(GameOverException) as cm:
            self.game.move('left')
        self.assertEqual(cm.exception.args[0], "Loss")
        self.game.player_position = (0, 0)
        with self.assertRaises(GameOverException) as cm:
            self.game.move('up')
        self.assertEqual(cm.exception.args[0], "Loss")

if __name__ == '__main__':
    unittest.main()
