from random import randint # randint function need to AI turn
from external_logic.show_func import show_my_gameboard

class Ship:
    """Warship class. Has 6 main attr."""

    def __init__(self, ship_length: int, dot_bow: tuple,
                direction: str, hp: int, owner: str, coordinates: list) -> None:
        """Coordinates is list with tuple objects."""
        self.ship_length = ship_length
        self.dot_bow = dot_bow
        self.direction = direction
        self.hp = hp
        self.owner = owner
        self.coordinates = coordinates

    def change_hp_value (self, hp: int):
        """Change HP for class - object."""
        self.hp = hp

def input_warship_bow_coordinate (warship_length: int, player) -> list:
    """Return list with dates of creates ship. First value in list is tuple with coordinate,\
    first value in tuple is string, second value is column. Second value in list is direction.\
    Third value is warship length. Last value is player."""
    if warship_length == 1:
        direction = "horizontal"
    else:
        if player == "AI":
            direction = randint(1, 2)
            if direction == 1:
                direction = "horizontal"
            else:
                direction = "vertical"
        else:
            for input_try in range(1, 100):
                try:
                    direction = input("Choose a position for the ship:\n\
1 - horizontal\n2 - vertical\n:")
                    if direction == "1":
                        direction = "horizontal"
                        break
                    if direction == "2":
                        direction = "vertical"
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    if player != 'AI':
                        print(f"You input incorrect value.\
Its your {input_try} try. Please try again.")
    if direction == "horizontal":
        for input_try in range (1, 100):
            try:
                if player == "AI":
                    horizontal_coordinate = randint(1, 6)
                    break
                else:
                    horizontal_coordinate = input("Enter string number for your ship bow (1 - 6): ")
                    if horizontal_coordinate in ["1", "2", "3", "4", "5", "6"]:
                        horizontal_coordinate = int(horizontal_coordinate)
                        break
                    else:
                        raise ValueError()
            except ValueError:
                if player != "AI":
                    print(f"You input incorrect value. Its your {input_try} try. Please try again.")
        for input_try in range (1, 100):
            try:
                if player == "AI":
                    vertical_coordinate = randint(1, (6 - warship_length + 1))
                    break
                else:
                    vertical_coordinate = input(f"Enter column number for your\
ship bow (1 - {6 - warship_length + 1}): ")
                    check_list = [str(i) for i in range (1, (6 - warship_length + 2))]
                    if vertical_coordinate in check_list:
                        vertical_coordinate = int(vertical_coordinate)
                        break
                    else:
                        raise ValueError()
            except ValueError:
                if player != "AI":
                    print(f"You input incorrect value. Its your {input_try} try. Please try again.")

    if direction == "vertical":
        for input_try in range (1, 100):
            try:
                if player == "AI":
                    horizontal_coordinate = randint(1, (6 - warship_length + 1))
                    break
                else:
                    horizontal_coordinate = input(f"Enter string number for your ship bow (1 - {6 - warship_length + 1}): ")
                    check_list = [str(i) for i in range (1, (6 - warship_length + 2))]
                    if horizontal_coordinate in check_list:
                        horizontal_coordinate = int(horizontal_coordinate)
                        break
                    else:
                        raise ValueError()
            except ValueError:
                if player != "AI":
                    print(f"You input incorrect value. Its your {input_try} try. Please try again.")
        for input_try in range (1, 100):
            try:
                if player == "AI":
                    vertical_coordinate = randint(1, 6)
                    break
                else:
                    vertical_coordinate = input("Enter column number for your ship bow (1 - 6): ")
                    if vertical_coordinate in ["1", "2", "3", "4", "5", "6"]:
                        vertical_coordinate = int(vertical_coordinate)
                        break
                    else:
                        raise ValueError()
            except ValueError:
                if player != "AI":
                    print(f"You input incorrect value. Its your {input_try} try. Please try again.")
    warship_coordinate = (horizontal_coordinate, vertical_coordinate)
    return [warship_coordinate, direction, warship_length, player]

def is_this_place_empty_for_ship(input_data: list, game_board: list) -> bool:
    """Check board for placing warship. If its possible return true."""
    dot_bow = input_data[0]
    dot_bow_line = dot_bow[0]
    dot_bow_column = dot_bow[1]
    direction = input_data[1]
    check_coordinate_list = []
    ship_length = input_data[2]
    player = input_data [3]
    if direction == 'horizontal':
        if dot_bow_line == 1:
            dot_bow_line_min_max = [dot_bow_line, (dot_bow_line + 2)]
        elif dot_bow_line == 6:
            dot_bow_line_min_max = [(dot_bow_line - 1), dot_bow_line + 1]
        else:
            dot_bow_line_min_max = [(dot_bow_line - 1), (dot_bow_line + 2)]
        if dot_bow_column == 1:
            dot_bow_column_min_max = [dot_bow_column, (dot_bow_column + ship_length + 1)]
        elif dot_bow_column == 4:
            dot_bow_column_min_max = [(dot_bow_column - 1), (dot_bow_column + ship_length + 1)]
        else:
            dot_bow_column_min_max = [(dot_bow_column - 1), (dot_bow_column + ship_length + 1)]

    if direction == "vertical":
        if dot_bow_line == 1:
            dot_bow_line_min_max = [dot_bow_line, (dot_bow_line + ship_length + 1)]
        elif dot_bow_line == 4:
            dot_bow_line_min_max = [(dot_bow_line - 1), (dot_bow_line + ship_length + 1)]
        else:
            dot_bow_line_min_max = [(dot_bow_line - 1), (dot_bow_line + ship_length + 1)]
            
        if dot_bow_column == 1:
            dot_bow_column_min_max = [dot_bow_column, (dot_bow_column + 2)]
        elif dot_bow_column == 6:
            dot_bow_column_min_max = [(dot_bow_column - 1), dot_bow_column + 1]
        else:
            dot_bow_column_min_max = [(dot_bow_column - 1), (dot_bow_column + 2)]
    for line in range(dot_bow_line_min_max[0], dot_bow_line_min_max[1]):
        for column in range(dot_bow_column_min_max[0], dot_bow_column_min_max[1]):
            check_coordinate_list.append((line, column))
    for coordinate in check_coordinate_list:
        for dot in game_board:
            if dot.coordinate == coordinate:
                status = dot.check_coordinate_on_field(player)
                if status != "empty":
                    return False
    return True

def list_with_all_ship_coordinate(input_data: list) -> list:
    """Return list with all coordinates of ship."""
    dot_bow = input_data[0]
    line = dot_bow[0]
    column = dot_bow[1]
    direction = input_data[1]
    warship_coordinates_list = []
    ship_length = input_data[2]
    if direction == "horizontal":
        def create_list_if_direct_horizontal(ship_length, variable):
            if ship_length == 0:
                return
            else:
                warship_coordinates_list.append((line, column + variable))
                create_list_if_direct_horizontal(ship_length - 1, variable + 1)
        create_list_if_direct_horizontal(ship_length, 0)    
    else:
        def create_list_if_direct_vertical(ship_length, variable):
            if ship_length == 0:
                return
            else:
                warship_coordinates_list.append((line + variable, column))
                create_list_if_direct_vertical(ship_length - 1, variable + 1)
        create_list_if_direct_vertical(ship_length, 0)
    return warship_coordinates_list

def create_ship (warship_length: int, game_board: list, player: str) -> list:
    """Create Ship class object for player."""
    for input_try in range(1, 100):
        try:
            created_ship = input_warship_bow_coordinate (warship_length, player)
            if is_this_place_empty_for_ship(created_ship, game_board) is True:
                break
            else:
                raise ValueError()
        except ValueError:
            if player != "AI":
                show_my_gameboard(game_board, player)
                print(f"You try to create your ship near your another ship.\
Its your {input_try} try. Please try again.")
    list_with_coordinates = list_with_all_ship_coordinate(created_ship)
    for coordinate in list_with_coordinates:
        for dot in game_board:
            if dot.coordinate == coordinate:
                dot.change_dot_status ('ship', player)
    final_object_ship = Ship(warship_length, created_ship[0], created_ship[1],
                              warship_length, player, list_with_coordinates)
    print(created_ship)
    if player != "AI":
        print('Your warship is created.')
    return final_object_ship

def create_all_ships_for_player (game_board: list, player: str) -> list:
    """Create list with all warships for one of player. If player = 'AI',\
warship has been created with random. """

    if player != "AI":
        print("Let's create your ships. Ships are placed from left to right, from top to bottom.\
Distance between ships must be at least one cell.")
        show_my_gameboard(game_board, player)
        print("First we create three deck warship.")
    three_deck_ship = create_ship(3, game_board, player)
    if player != "AI":
        print("Second we create 2 two deck warships.")
    first_two_deck_ship = create_ship(2, game_board, player)
    if player != "AI":
        print("Lets create another one.")
    second_two_deck_ship = create_ship(2, game_board, player)
    if player != "AI":
        print("Now we ready to create 3 one deck warships. Let's create first of them.")
    first_one_deck_ship = create_ship(1, game_board, player)
    if player != "AI":
        print("Now let's create second one.")
    second_one_deck_ship = create_ship(1, game_board, player)
    if player != "AI":
        print("Now let's create last one.")
    third_one_deck_ship = create_ship(1, game_board, player)

    list_with_all_warships = [three_deck_ship, first_two_deck_ship, second_two_deck_ship,
                              first_one_deck_ship, second_one_deck_ship, third_one_deck_ship]

    return list_with_all_warships
