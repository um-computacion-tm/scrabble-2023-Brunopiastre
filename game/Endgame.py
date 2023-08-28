class GameEndConditions:

    def __init__(self, bag_tiles, players):
        self.bag_tiles = bag_tiles
        self.players = players

    def tiles_depleted(self):
        return len(self.bag_tiles.tiles) == 0

    def all_possible_words_formed(self):
        # Logic to check if a player has formed all possible words
        # based on the current state of the game board.
        pass

    def players_agree_to_end(self):
        # Logic to check if players have collectively agreed to end the game.
        # This could involve a voting mechanism or any other criteria.
        pass

    def check_game_end(self):
        return self.tiles_depleted() or self.all_possible_words_formed() or self.players_agree_to_end()
