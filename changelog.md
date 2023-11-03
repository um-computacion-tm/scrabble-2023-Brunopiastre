# Changelog

## 3/11/23
### Added
+ Main
    - Main test
    
+ Scrabble
    - ask_tiles_to_change Tests
    - End method
## 1/11/23
### Added

### Fixed 
+ Board
    - Tests 

+ Dictionary
    - Tests

+ Board
    - test_validate_word_placement_not_empty


+ Pĺayer
    - get_connected_tile
    - test_validate_tiles changed
    - test_get_connected_tile


+ Scrabble 
    - exchange_wildtile method
    - test_exchange_wildtile
    - test_exchange_wildtile_wrong

+ Dockerfile

## 31/10/23
### Added
+ Scrabble 
    - create_cell_list method & test
    - create_cell_list_vertical test
    - create_cell_list_horizontal test
    
+ Player
    - Increase score method & tests
+ Scrabble
    - Create tile list method 
    
## 30/10/23
### Added

+ Board
    - validate_word_placement method 
    - put_word method
    - test_put_word_horizontal
    - test_put_word_vertical 
## 29/10/23
### Added
+ BagTile
    - Get_tile method and test

+ Scrabble
    - show board method & test 

+ Tile
    - repr method & test
## 28/10/23
### Added 
+ Main
    - Main method 

## 27/10/23
### Added
+ Player
    - set_nickname method & test

+ Board
    - triple_word_multiplier
    - double_word_multiplier
    - triple_letter_multiplier
    - double_letter_multiplier
    

## 26/10/23
### Added 
+ Scrabble 
    - end_game method & test
    - display_tiles method & test
    - show_score method & test

## 24/10/23
### Added
+ Cell
    - test_repr
    - test_repr2
    - test_repr3
    - test_repr4
### Fixed
+ Cell
    - repr
## 21/10/23
### Added
+ Board
    - test_place_word_board_vertical_inside_fine
    - test_place_word_board_horizontal_center_wrong
### changed
+ Board 
    - Duplicated code deleted
## 20/10/23
### Added
+ Board
    - test_place_word_empty_board_horizontal_inside_fine
    - test_place_word_empty_board_horizontal_inside_wrong

## 19/10/23
### Added
+ Board 
    - Clear cell method 
    - validate_word_is_connected method 
    - test_place_word_not_empty_conected_board_horizontal_fine
    - test_place_word_not_empty_not_conected_board_horizontal_wrong
    - test_place_word_not_empty_conected_board_vertical_fine
    - test_place_word_not_empty_not_conected_board_vertical_wrong
### Fixed
+ BagTiles
    - Put test fixed
### changed
+ Cell class

## 18/10/23
### Added
+ Board 
    + Added Validate word test 
## 17/10/23
+ Cell
    - Added calculate word value test
## 15/10/23
### Fixed
- Board
    + test test_word_inside_board is working now
    + test_word_out_of_board is working now

## 13/10/23
### Fixed
- Board
    + test_board_is_not_empty is working now
## 12/10/23
### Changed
- Cli
    + Unificated the Cli and main class 
- Endgame
    + Eliminated class endgame
## 11/10/23
### Added
- Cell
    + Added repr method
- Tile 
    + Added repr method
## 10/10/23
### Added
- Main
    + Created the show_board method
## 9/10/23
### Added
- Cli
    + Created the cli class and it test
    + created the get_player_count & test
## 8/10/23
### Added
- Main
    + Created the main class and it tests
### Fixed
- Tile
    + Fixed the Variable tile in test_tile
## 7/10/23
### changed
- Board
    + modified test_board_is_empty
    + test_board_is_not_empty, but is not working 
### Added
- Board 
    + created test_place_word_empty_board_horizontal_fine
    + created test_place_word_empty_board_horizontal_wrong, but is not working 
    + created test_place_word_empty_board_vertical_fine
    + created test_place_word_empty_board_vertical_wrong, but is not working 
## 6/10/23
### Added 
- Board
    + Added validate_word_inside_board method & test_word_inside_board test
    + Added word_out_of_board test
## 5/10/23
### Added 
- Player
    + Implementation of exchange_tiles method & test
## 4/10/23
### Fixed 
- Board
    + Empty method & test

## 3/10/23
### Added
- Player
    + Added player test

### Fixed 
- Changelog improved! better visualization now

## 2/10/23
### Added
- Player
    + Added get tiles  method and test   

## 1/10/23
### Added
- Cell
    + Added calculate_word method and test


---
## before october
### Addd 

- Board
    + Added empty method
        * Added test_board_is_empty, not working 
        * Added test_board_is_not_empty
    + Added Check_word method   
    + Added calculate_word_value method and test.
- Scrabble
    + Added Game over method and test
    + Added next_turn method and test


- Added dictionary class
- Added dictionary Test

- Added main class

- Added the Tile and BagTile classes
- Added the Tile and BagTile Tests

- Added the player class
- Added the player test

- Added the cell class
- Added the cell test

- Added the board class
- Added the board test

- Added the ScrabbleGame class
- Added the ScrabbleGame test



### Changed
- Modified scrabble.py to models.py
- Modified test_scrabble.py to test_models.py 
- Divided models class into Tiles class and BagTiles class 
. Player actualization
### Fixed

- Uppercase names were changed to lowercase names
- Fixed an instance misstake
### Date

- 1/10/23
- 30/09/23
- 30/09/23
- 29/09/23
- 28/09/23
- 27/09/23
- 25/09/23
- 24/09/23
- 24/09/23
- 24/09/23
- 24/09/23
- 24/09/23
- 24/09/23
- 12/09/23
- 12/09/23
- 08/09/23
- 30/08/23
- 28/08/23
- 28/08/23
- 28/08/23
- 28/08/23
- 28/08/23
- 27/08/23