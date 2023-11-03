import random
from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles
from game.tile import Tile


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())

        self.current_player = 0



    def next_turn(self):
        self.players[self.current_player].tiles.extend(self.bag_tiles.take(7 - len(self.players[self.current_player].tiles)))
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
        return [bag_tiles.get_tile(letter) for letter in word]

    

    def show_board(self):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(self.board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )
    

    def create_cell_list(self, word, location, orientation):
        x, y = map(int, location)
        grid = self.board.grid

        if orientation == 'H':
            cells = [grid[x][y + i] for i in range(len(word))]
        else:
            cells = [grid[x + i][y] for i in range(len(word))]

        return cells
    


    def exchange_wildtile(self):
        player = self.players[self.current_player]
        wildtile = next((tile for tile in player.tiles if tile.letter == '*'), None)

        while wildtile:
            new_letter = input("\nIngrese la nueva letra: ").upper()
            new_tile = self.bag_tiles.get_tile(new_letter)

            if new_tile:
                player.tiles.remove(wildtile)
                player.tiles.append(new_tile)
                return

            print("\nPor favor, ingrese una ficha válida.")

        print("\nNo tiene comodines.")


    def ask_tiles_to_change(self):
        tiles_to_change = input("\nIngrese las fichas que desea cambiar separadas por comas (0 para volver):  ")
        if tiles_to_change == '0':
            return
        tiles_to_change = tiles_to_change.replace(' ', '')
        tiles_to_change = tiles_to_change.upper().split(',')
        tiles = []
        try:
            for i in tiles_to_change:
                tiles.append(self.bag_tiles.get_tile(i))
            for tile in tiles:
                found = False
                for player_tile in self.players[self.current_player].tiles:
                    if tile.letter == player_tile.letter:
                        found = True
                        break
                if not found:
                    print("Ficha no encontrada: " + tile.letter)
                    self.ask_tiles_to_change()
            
        except AttributeError:
            print("\nPor favor, ingrese una ficha válida.")
            self.ask_tiles_to_change()
        
        self.bag_tiles.put(tiles)
        random.shuffle(self.bag_tiles.tiles)
        new_tiles = self.bag_tiles.take(len(tiles))
        self.players[self.current_player].tiles.extend(new_tiles)
        self.players[self.current_player].remove_tiles(tiles_to_change)
        self.next_turn()


    def end(self):
        print("Fin del juego\n")
        print("Los puntajes finales son:")
        print("Jugador      Puntaje")
        print("-------      -------")
        max_score = 0
        i = 0
        for player in self.players:
            player.id = self.current_player + i
            i += 1
            if player.score > max_score:
                max_score = player.score
        for player in self.players:
            print(f"{'Jugador'} {player.id}       {player.score}")
            if player.score == max_score:
                id_winner = player.id
        print(f"{'Jugador'} {id_winner} es el ganador!")
        