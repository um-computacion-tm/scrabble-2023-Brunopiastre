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
        if self.current_player == len(self.players) - 1:
            self.current_player = 0
        else:
            self.current_player += 1




    def game_over(self):
        return not self.bag_tiles
    

    def show_score(self):
        print("Su puntaje es :",self.players[self.current_player].score)

    def display_tiles(self, player):
        for i in player.tiles:
            print(f'[{i.letter},{i.value}]', end=' ')  


    def end_game(self):
        if len(self.bag_tiles.tiles) == 0:
                return True
        return False