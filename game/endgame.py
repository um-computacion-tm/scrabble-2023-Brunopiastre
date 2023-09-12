from game.board import Board
from game.bagtiles import BagTiles
from game.player import Player


class endgame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())





#           Una vez que ya tenga el diccionario en la clase player puedo hacer la proxima, que va a servir para mandarle todas
#           las palabras que el jugador haya formado y verificarlas


  
# Ejemplo de cómo usar la lógica de verificación de palabras en el juego
def main():
    players_count = 2
    game = ScrabbleGame(players_count)

    while not game.check_game_end():
        # Lógica para turnos de jugadores, colocación de fichas en el tablero, etc.

        for player in game.players:
            if game.check_player_formed_all_words(player):
                print("¡El jugador ha formado todas las palabras posibles!")

                if __name__ == "__main__":
                    main()



















    def check_game_end(self):
        if self.bag_tiles.is_empty():
            return True
        for player in self.players:
            if self.check_player_formed_all_words(player):
                return True
        return False

# Aquí deberías implementar la lógica real para verificar si un jugador ha formado todas las palabras posibles.
# Deberías usar la clase Player y las propiedades relacionadas con las letras del jugador.





#Esta es la aplicacion del metodo de arriba (check_game_end)


# Ejemplo de cómo usar la clase ScrabbleGame y verificar si el juego ha finalizado
def main():
    players_count = 2  # Cambia esto al número de jugadores que participarán en el juego, Habbria que poner algo al inicio del juego que indique el numero de jugadores
    game = endgame(players_count)

    while not game.check_game_end():
        # Continuar con el juego    
        
        if __name__ == "__main__":
            main()

