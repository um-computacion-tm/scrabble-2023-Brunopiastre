from game.scrabble import ScrabbleGame
from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles


def main():
    player = Player()
    bagtiles = BagTiles()
    board = Board() 
    print("Bienvenido!")
    while True:
        try:
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Error Ingrese de 2 a 4 jugadores")
    scrabbleGame = ScrabbleGame(players_count=players_count)
    print("Cantidad de jugadores: ",len(scrabbleGame.players))

    for i in range(len(scrabbleGame.players)):
        scrabbleGame.players[i].set_nickname()
    while(True):

        print('+' * 100)
        print('~' * 100)
        print('Scrabble')
        print(f"Turno del jugardor {scrabbleGame.players[scrabbleGame.current_player].nickname} \n")
        print('_' * 15)
        print('--Menu--')
        print('1. Mostrar Tablero')
        print('2. Mostrar puntos')
        print('3. Mostrar mis fichas')
        print('4. Colocar palabra')
        print('5. Cambiar fichas')
        print('6. Pasar turno')
        print('7. Terminar juego')
        print('+' * 100)
        option = input("Ingrese una opción: ")


        if option == '1':
            show_board(board)
        elif option == '2':
            scrabbleGame.show_score()
        elif option == '3':
            print('Sus fichas son: ')
            scrabbleGame.display_tiles(player)
        elif option == '4':
            put_word(scrabbleGame)
        elif option == '5':
            bagtiles.put(player.tiles)
            bagtiles.take(len(player.tiles))
        elif option == '6':
            scrabbleGame.next_turn()
        elif option == '7':   
            scrabbleGame.end_game()


        else:
            print ('------------------------------------------------------------------------------------------------------\n'
           )
            print("Opción inválida")
            print ('------------------------------------------------------------------------------------------------------\n'
           )

def put_word(scrabbleGame):
    word = input("Ingrese la palabra")
    location_x = input("Ingrese posicion X: ")
    location_y = input("Ingrese posicion Y: ")
    location = (location_x, location_y)
    orientation = input("Ingrese orientacion (V/H)")
    scrabbleGame.board.validate_word_inside_board(word, location, orientation)


def show_board(board):
    print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
    for row_index, row in enumerate(board.grid):
        print(
            str(row_index).rjust(2) +
            '| ' +
            ' '.join([repr(cell) for cell in row])
        )
        

def get_player_count():
    while True:
        try:
            player_count = int(input('Cantidad de jugadores (2-4): '))
            if 2 <= player_count <= 4:
                return player_count
            else:
                raise ValueError("Por favor, ingrese un número entre 2 y 4.")
        except ValueError as e:
            print(f'Error: {e}')




if __name__ == '__main__':
    main()