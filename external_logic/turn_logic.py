from random import randint
from external_logic.show_func import show_my_gameboard, show_my_turns

def input_turn_coordinates(player: str, game_board: list) -> tuple:
    """Function for input coordinates. Return tuple object,\
          first value is string, second value is column."""

    def input_coordinates() -> tuple:
        for input_try in range (1, 100):
            try:
                if player == "AI":
                    horizontal_coordinate = randint(1, 6)
                    break
                else:
                    horizontal_coordinate = input("Enter string number (1 - 6): ")
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
                    vertical_coordinate = randint(1, 6)
                    break
                else:
                    vertical_coordinate = input("Enter column number (1 - 6): ")
                    if vertical_coordinate in ["1", "2", "3", "4", "5", "6"]:
                        vertical_coordinate = int(vertical_coordinate)
                        break
                    else:
                        raise ValueError()
            except ValueError:
                if player != "AI":
                    print(f"You input incorrect value. Its your {input_try} try. Please try again.")

        coordinate = (horizontal_coordinate, vertical_coordinate)
        return coordinate

    def check_turn_coordinate (coordinate: tuple) -> bool:
        """Return true if its possible to make this turn."""
        if player == "first player":
            for dot in game_board:
                if dot.coordinate == coordinate:
                    status = dot.check_coordinate_on_field("second player")
                    if status in ["miss", "hit"]:
                        return False
                    else:
                        return True
        else:
            for dot in game_board:
                if dot.coordinate == coordinate:
                    status = dot.check_coordinate_on_field("first player")
                    if status in ['miss', 'hit']:
                        return False
                    else:
                        return True

    for input_try in range (1, 100):
        try:
            coordinate = input_coordinates()
            check = check_turn_coordinate(coordinate)
            if check is True:
                break
            else:
                raise ValueError()
        except ValueError:
            if player != "AI":
                print(f"You already move on this coordinates.\
Its your {input_try} try. Please try again.")
    return coordinate

def player_turn (player: str, game_board: list, list_of_enemy_warships: list,
                  message_of_previous_turn: str) -> str:
    """Main function for our game. Its player turn. Return message for next player."""
    if player != "AI":
        show_my_gameboard(game_board, player)
        print(message_of_previous_turn)
    coordinate = input_turn_coordinates (player, game_board)
    message = ""
    if player == "first player":
        opposite_player = "second player"
    else:
        opposite_player = "first player"
    for dot in game_board:
        if dot.coordinate == coordinate:
            status = dot.check_coordinate_on_field(opposite_player)
            if status == "empty":
                dot.change_dot_status("miss", player)
                if player != "AI":
                    print("You missed.")
                    show_my_turns(game_board, player)
                message = "Your opponent missed!"
                break
            if status == "ship":
                dot.change_dot_status("hit", player)
                for warship in list_of_enemy_warships:
                    if dot.coordinate in warship.coordinates:
                        warship.hp = warship.hp - 1
                        if player != "AI":
                            show_my_turns(game_board, player)
                            print("You hit opponent's warship.")
                        message = f"Your {warship.ship_length} - deck warship was hitted."
                        if warship.hp == 0:
                            list_of_enemy_warships.remove(warship)
                            if player != "AI":
                                show_my_turns(game_board, player)
                                print(f"You desroyed {warship.ship_length} - deck opponent warship.")
                            message = f"Your {warship.ship_length} - deck warship was destroyed."
                            break
                        else:
                            break
                break
    return message
