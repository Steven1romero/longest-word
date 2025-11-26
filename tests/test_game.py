from longest_word.game import Game


class TestGame:
    def test_game_initialization(self):
        game = Game()
        grid = game.grid

        assert isinstance(grid, list)
        assert len(grid) == 9
        assert all(isinstance(letter, str) for letter in grid)
        assert all(len(letter) == 1 for letter in grid)

    def test_valid_word_in_grid(self):
        game = Game()
        game.grid = list("OQUWRBAZE")  # grid fijo para pruebas

        assert game.is_valid("BAROQUE") is True

    def test_invalid_word_not_in_grid(self):
        game = Game()
        game.grid = list("OQUWRBAZE")

        assert game.is_valid("HELLO") is False

