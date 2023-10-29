from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())

        self.current_player = 0



    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)


    def show_score(self):
        print("Su puntaje es :",self.players[self.current_player].score)

    def display_tiles(self, player):
        for i in player.tiles:
            print(f'[{i.letter},{i.value}]', end=' ')  


    def end_game(self):
        if len(self.bag_tiles.tiles) == 0:
                return True
        return False
    


    def create_tile_list(self, word, bag_tiles):
        tile_list = []
        for letter in word:
            tile = bag_tiles.get_tile(letter)
            tile_list.append(tile)
        return tile_list
    

    def show_board(self):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(self.board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )
    