from game.scrabble import ScrabbleGame

def get_players_count():
    while True:
        try:
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Error Ingrese de 2 a 4 jugadores")
    return players_count

def set_player_nicknames(scrabbleGame):
    for i in range(len(scrabbleGame.players)):
        scrabbleGame.players[i].set_nickname()

def handle_option(scrabbleGame, option):
    if option == '1':
        scrabbleGame.show_board()
    elif option == '2':
        scrabbleGame.show_score()
    elif option == '3':
        print('Sus fichas son: ')
        scrabbleGame.display_tiles(scrabbleGame.players[scrabbleGame.current_player])   
    elif option == '4':
        put_word(scrabbleGame)
    elif option == '5':
        scrabbleGame.bag_tiles.put(scrabbleGame.players[scrabbleGame.current_player].tiles)
        scrabbleGame.bag_tiles.take(len(scrabbleGame.players[scrabbleGame.current_player].tiles))
        scrabbleGame.ask_tiles_to_change()
    elif option == '6':
        scrabbleGame.next_turn()
    elif option == '7':
        scrabbleGame.exchange_wildtile() 
    elif option == '8': 
        scrabbleGame.end()
        return False
    else:
        print ('------------------------------------------------------------------------------------------------------\n')
        print("Opción inválida")
        print ('------------------------------------------------------------------------------------------------------\n')
    return True

def main():
    print("Bienvenido!")
    players_count = get_players_count()
    scrabbleGame = ScrabbleGame(players_count=players_count)
    print("Cantidad de jugadores: ",len(scrabbleGame.players))
    set_player_nicknames(scrabbleGame)
    while(True):
        if scrabbleGame.end_game() == True:
            print("La bolsa de fichas esta vacia, el juego ha terminado.\n")
            scrabbleGame.end()
            break
        print('+' * 100)
        print('~' * 100)
        print('Scrabble')
        print(f"Turno de {scrabbleGame.players[scrabbleGame.current_player].nickname} \n")
        print('_' * 15)
        print('--Menu--')
        print('1. Mostrar Tablero')
        print('2. Mostrar puntos')
        print('3. Mostrar mis fichas')
        print('4. Colocar palabra')
        print('5. Cambiar fichas')
        print('6. Pasar turno')
        print('7. Cambiar comodin')
        print('8. Terminar juego')
        print('+' * 100)
        print('Sus fichas son:')
        scrabbleGame.display_tiles(scrabbleGame.players[scrabbleGame.current_player])
        option = input("\nIngrese una opción: ")
        if not handle_option(scrabbleGame, option):
            break

def put_word(scrabbleGame):
    word = input("Ingrese la palabra (0 para volver): ")
    if word == '0':
        return
    word = word.upper()
    try:
        location_x = input("Ingrese posicion X: ")
        location_y = input("Ingrese posicion Y: ")
        orientation = input("Ingrese orientacion (V/H): ")
        location = (location_x, location_y)
        if not location_x.isdigit() or not location_y.isdigit():
            raise ValueError
    except ValueError:
        print("Por favor, ingrese un número válido para la posición X y Y.")
        return put_word(scrabbleGame)
    orientation = orientation.upper()
    if scrabbleGame.board.validate_word_placement(word, location, orientation, scrabbleGame):
        scrabbleGame.board.put_word(scrabbleGame.create_tile_list(word,scrabbleGame.bag_tiles), location, orientation)
        scrabbleGame.players[scrabbleGame.current_player].remove_tiles(word)
        scrabbleGame.players[scrabbleGame.current_player].increse_score(scrabbleGame.board.calculate_word_value(scrabbleGame.create_cell_list(word, location, orientation)))  
    else:
        print("Palabra invalida")
        put_word(scrabbleGame)


if __name__ == '__main__':
    main()