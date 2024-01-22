from iternal_logic.board import create_game_board
from iternal_logic.ship import create_all_ships_for_player
from external_logic.turn_logic import player_turn


game_board = create_game_board()

print("Welcome to the Warship game!")
for input_try in range (1, 100):
    try:
        one_or_two_players = input("Chose number of players:\n1 - one player\n2 - two players\n")
        if one_or_two_players in ["1", "2"]:
            one_or_two_players = int(one_or_two_players)
            break
        else:
            raise ValueError()
    except ValueError:
        print(f"You input incorrect value. Its your {input_try} try. Please try again.")
if  one_or_two_players == 1:
    FIRST_PLAYER = "first player"
    SECOND_PLAYER = "AI"
else: 
    FIRST_PLAYER = "first player"
    SECOND_PLAYER = "second player"

first_player_warships = create_all_ships_for_player(game_board, FIRST_PLAYER)
second_player_warships = create_all_ships_for_player(game_board, SECOND_PLAYER)
message = "Its first player turn!"
while (bool(first_player_warships)) == (bool(second_player_warships)):

    message = player_turn(FIRST_PLAYER, game_board, second_player_warships, message)
    message = player_turn(SECOND_PLAYER, game_board, first_player_warships, message)

if bool(first_player_warships) is True:
    print("Second player win.")
else:
    print("First player win.")

