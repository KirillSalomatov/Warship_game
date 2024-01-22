class Board:
    """Class represented a game board objects. Every object is dot on game board."""

    def __init__(self, coordinate: tuple, status_1_player: str, status_2_player:str) -> object:
        self.coordinate = coordinate
        self.status_1_player = status_1_player
        self.status_2_player = status_2_player

    def check_coordinate_on_field (self, player: str):
        """Return coordinate status on field. Names of players always\
        is 'first player' or 'second player' or 'AI'."""

        if player == "first player":
            return self.status_1_player
        if player in ["second player", "AI"]:
            return self.status_2_player
        return None

    def change_dot_status (self, new_status: str, player: str):
        """Change dot status. Possible value for player: 'first player', 'second player'\
            ,'AI'. Possible value for new_status: 'ship', 'hit', 'miss'."""

        if player == "first player":
            if new_status == "ship":
                self.status_1_player = new_status
            else:
                self.status_2_player = new_status
        else:
            if new_status == "ship":
                self.status_2_player = new_status
            else:
                self.status_1_player = new_status

def create_game_board() -> list:
    """Return list with dot objects."""

    def create_list_with_coordinates() -> list:
        """Return all posible variants of coordinates on game board."""
        list_with_coordinates = []
        for horizontal_coordinate in range (1, 7):
            for vertical_coordinate in range (1, 7):
                list_with_coordinates.append((horizontal_coordinate, vertical_coordinate))
        return list_with_coordinates

    list_1 = create_list_with_coordinates()
    game_board = [Board(i, "empty", "empty") for i in list_1]
    return game_board
