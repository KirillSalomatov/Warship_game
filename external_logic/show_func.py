"""Module providing a functions wich displayed game board on the terminal."""

def choose_icon(coordinate: tuple, game_board: list, player: str) -> str:
    """Return status icon for print."""
    for dot in game_board:
        if dot.coordinate == coordinate:
            status = dot.check_coordinate_on_field(player)
            break
    if status == 'empty':
        icon = "О"
    elif status == "ship":
        icon = "■"
    elif status == "miss":
        icon = "T"
    elif status == "hit":
        icon = "X"
    return icon

def show_my_gameboard(game_board: list, player):
    """Print game board for player."""
    print('\n   | 1 | 2 | 3 | 4 | 5 | 6 |\n')
    num_of_string = 1
    for horizontal_coordinate in range (1, 7):
        print(" " + str(num_of_string), end=" |")
        for vertical_coordinate in range (1, 7):
            icon = choose_icon((horizontal_coordinate, vertical_coordinate), game_board, player)
            print(" " + icon, end=" |")
        print('\n')
        num_of_string += 1

def show_my_turns (game_board: list, player: str):
    """Print opponents game board. Dont show opponents warships."""

    if player == "first player":
        player_forshow = "second player"
    else:
        player_forshow = "first player"

    print('\n   | 1 | 2 | 3 | 4 | 5 | 6 |\n')
    num_of_string = 1
    for horizontal_coordinate in range (1, 7):
        print(" " + str(num_of_string), end=" |")
        for vertical_coordinate in range (1, 7):
            icon = choose_icon((horizontal_coordinate, vertical_coordinate),
                                game_board, player_forshow)
            if icon == "■":
                icon = "О"
            print(" " + icon, end=" |")
        print('\n')
        num_of_string += 1
