from game.scrabble import ScrabbleGame

class Main:

    def main():

        print("Bienvenido!")

        while True:

            try: 

                players_count = int(input("Ingrese cantidad de jugadores: "))

                if players_count <= 1 or players_count > 4:

                    raise ValueError

                break

            except ValueError:

                print("Valor invalido")

        scrabble_game = ScrabbleGame(players_count=players_count)

        print("Cantidad de jugadores: ",len(scrabble_game.players))

        scrabble_game.next_turn()

        #TODO while playing: loop por turno de jugador hasta que termine el juego

        print(f"Turno del jugador {scrabble_game.current_player.id}")

        word = input("Ingrese palabra: ")

        location_x = input("Ingrese posicion X: ")

        location_y = input("Ingrese posicion Y: ")

        location = (location_x, location_y)

        orientation = input("Ingrese orientacion (V/H)")

        scrabble_game.validate_word(word, location, orientation)



        # def main():
        # player_count = get_player_count()
        # game = ScrabbleGame(player_count)
        # while game.is_playing():
        #     show_board(game.get_board())
        #     show_player(*game.get_current_player())
        #     word, coords, orientation = get_inputs()
        #     try:
        #         game.play(word, coords, orientation)
        #     except Exception as e:
        #         print(e)



    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )


        


    if __name__ == '__main__':

        main()

