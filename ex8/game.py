#############################################################
# FILE : ship.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex8 2016-2017
# DESCRIPTION :
# a battle ship Game Class, runs a battle ship game
############################################################
############################################################
# Imports
############################################################
import game_helper as gh

############################################################
# conduct the game using ship class methods to control it's
# ships. can play one round and an entire game (several rounds)
############################################################
BOMB_LIFETIME = 3
BOMB_EXP = 0


class Game:
    """
    A class representing a battleship game.
    A game is composed of ships that are moving on a square board and a user
    which tries to guess the locations of the ships by guessing their
    coordinates.
    """

    def __init__(self, board_size, ships):
        """
        Initialize a new Game object.
        :param board_size: Length of the side of the game-board.
        :param ships: A list of ships (of type Ship) that participate in the
            game.
        :return: A new Game object.
        """
        self._bs = board_size
        self._ships = ships
        self._bombs = {}
        self._hits_coors = []
        self._hits = []
        self._ships_coors = self.__initialize_ships_coors()

    def __initialize_ships_coors(self):
        """
        :return: create a list of all ship's valid (un-damaged) coordinates
        """
        ships_coors = []
        for ship in self._ships:
            for coordinate in ship.coordinates():
                if coordinate not in self._hits_coors:
                    ships_coors.append(coordinate)
        return ships_coors

    def __play_one_round(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        The function runs one round of the game :
            1. Get user coordinate choice for bombing.
            2. Move all game's ships.
            3. Update all ships and bombs.
            4. Report to the user the result of current round (number of hits and
             terminated ships)
        :return:
            (some constant you may want implement which represents) Game status :
            GAME_STATUS_ONGOING if there are still ships on the board or
            GAME_STATUS_ENDED otherwise.
        """
        target = gh.get_target(self._bs)
        self._bombs[target] = BOMB_LIFETIME
        self.move_ships()
        self._ships_coors = self.__initialize_ships_coors()
        self._hits = self.update_hits(target)
        gh.board_to_string(self._bs, self._hits, self._bombs, self._hits_coors, self._ships_coors)
        terminations = self.update_ships()
        gh.report_turn(len(self._hits), terminations)

    def move_ships(self):
        """
        moves all un-damaged ships according to ship's rules
        :return: None
        """
        for ship in self._ships:
            if not ship.get_hit():
                ship.move()

    def update_hits(self, target):
        """
        checks for hits in this turn, and updates the game accordingly: ships and bombs
        :param target: this turn user entry for a target
        :return: a list of all ship's hit-coordinates of this turn
        """
        hits = ()
        for pos in self._bombs.keys():
            for ship in self._ships:
                if ship.hit(pos):  # got hit 1st time
                    if not ship.terminated(): # an old terminated ship shouldn't appear as 'hit'
                        self._hits_coors.append(pos)
                    self._ships_coors.remove(pos)
                    hits += (pos,)
            if pos != target:
                self._bombs[pos] -= 1
        for bomb in hits:
            self._bombs[bomb] = BOMB_EXP
        self._bombs = {pos: val for pos, val in self._bombs.items() if val > BOMB_EXP}
        return list(hits)

    def update_ships(self):
        """
        updates game's list of ships according, after terminations
        :return: num of terminated ships this turn (int)
        """
        new_ships = [ship for ship in self._ships if not ship.terminated()]
        terminations = len(self._ships) - len(new_ships)
        self._ships = new_ships
        return terminations

    def __repr__(self):
        """
        Return a string representation of the board's game.
        :return: A tuple converted to string (that is, for a tuple x return
            str(x)). The tuple should contain (maintain
        the following order):
            1. Board's size.
            2. A dictionary of the bombs found on the board, mapping their
                coordinates to the number of remaining turns:
                 {(pos_x, pos_y) : remaining turns}
                For example :
                 {(0, 1) : 2, (3, 2) : 1}
            3. A list of the ships found on the board (each ship should be
                represented by its __repr__ string).
        """
        return str((self._bs, self._bombs, self._ships))

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        gh.report_legend()
        gh.board_to_string(self._bs, self._hits, self._bombs, self._hits_coors, self._ships_coors)
        while self._ships_coors != []:
            self.__play_one_round()
        gh.report_gameover()

############################################################
# An example usage of the game
############################################################
if __name__ == "__main__":
    game = Game(5, gh.initialize_ship_list(4, 2))
    game.play()
