from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles


class ScrabbleGame:

    def __init__(self, players_count: int):

        self.board = Board()

        self.bag_tiles = BagTiles()

        self.players:list[Player] = []

        for _ in range(players_count):

            self.players.append(Player())


        self.current_player = None


    def next_turn(self):

        if self.current_player is None:

            self.current_player = self.players[0]

        elif self.players.index(self.current_player) != len(self.players) -1:

            #index = index del current player + 1

            #len(self.players)

            index = self.players.index(self.current_player) + 1

            self.current_player = self.players[index]

        else:
            self.current_player = self.players[0]


