#############################################################
# FILE : ship.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex8 2016-2017
# DESCRIPTION :
# Ship and Direction Classes, for a battle ship game.
############################################################
import ship_helper as sh
############################################################
# Helper class
# representing a valid direction for ships in battle ship game
############################################################


class Direction:
    """
    Class representing a direction in 2D world.
    You may not change the name of any of the constants (UP, DOWN, LEFT, RIGHT,
     NOT_MOVING, VERTICAL, HORIZONTAL, ALL_DIRECTIONS), but all other
     implementations are for you to carry out.
    """
    UP = '1'
    DOWN = '2'
    LEFT = '3'
    RIGHT = '4'
    NOT_MOVING = '9'

    VERTICAL = (UP, DOWN)
    HORIZONTAL = (LEFT, RIGHT)

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)

############################################################
# controls all ship characteristics & operations
# a Ship obj has a length, position on board direction, and it
# can move, change direction when meet the end of the game board.
# it can be hit (in that case it stops moving) and terminated.
# it holds all information on it's hits - which cell from it's cells
# and changes it according to game events.
############################################################


class Ship:
    """
    A class representing a ship in Battleship game.
    A ship is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A ship sails on its vertical\horizontal axis back and
    forth until reaching the board's boarders and then changes its direction to
    the opposite (left <--> right, up <--> down).
    If a ship is hit in one of its coordinates, it ceases its movement in all
    future turns.
    A ship that had all her coordinates hit is considered terminated.
    """

    def __init__(self, pos, length, direction, board_size):
        """
        A constructor for a Ship object
        :param pos: A tuple representing The ship's head's (x, y) position
        :param length: Ship's length
        :param direction: Initial direction in which the ship is sailing
        :param board_size: Board size in which the ship is sailing
        """
        self._pos = pos
        self._x_pos, self._y_pos = self._pos
        self._len = length
        self._dir = direction
        self._bs = board_size
        self._is_hit = False
        self._hit_coors = []
        self._coordinates = self.coordinates()

    def __repr__(self):
        """
        Return a string representation of the ship.
        :return: A tuple converted to string (that is, for a tuple x return
            str(x)).
        The tuple's content should be (in the exact following order):
            1. A list of all the ship's coordinates.
            2. A list of all the ship's hit coordinates.
            3. Last sailing direction.
            4. The size of the board in which the ship is located.
        """
        dir_str = sh.direction_repr_str(Direction, self.direction())
        info = (self.coordinates(), self._hit_coors, dir_str, self._bs)
        return str(info)

    def move(self):
        """
        Make the ship move one board unit.
        Movement is in the current sailing direction, unless such movement would
        take the ship outside of the board, in which case the ship switches
        direction and sails one board unit in the new direction.
        :return: A direction object representing the current movement direction.
        """
        if (self._dir is Direction.UP) and (self._y_pos is 0):
            self._dir = Direction.DOWN
        elif (self._dir is Direction.DOWN) and (self._y_pos+self._len is self._bs):
            self._dir = Direction.UP
        elif (self._dir is Direction.LEFT) and (self._x_pos is 0):
            self._dir = Direction.RIGHT
        elif (self._dir is Direction.RIGHT) and (self._x_pos+self._len is self._bs):
            self._dir = Direction.LEFT
        self.change_pos(self._dir)
        return self._dir

    def change_pos(self, direction):
        """
        changes the position if ships' start coordinated (therefore moving it)
        :param direction: a Direction object
        :return: None
        """
        if direction == Direction.UP:
            self._y_pos -= 1
        elif direction == Direction.DOWN:
            self._y_pos += 1
        elif direction == Direction.LEFT:
            self._x_pos -= 1
        elif direction == Direction.RIGHT:
            self._x_pos += 1
        self._coordinates = self.coordinates()

    def hit(self, pos):
        """
        Inform the ship that a bomb hit a specific coordinate. The ship updates
         its state accordingly.
        If one of the ship's body's coordinate is hit, the ship does not move
         in future turns. If all ship's body's coordinate are hit, the ship is
         terminated and removed from the board.
        :param pos: A tuple representing the (x, y) position of the hit.
        :return: True if the bomb generated a new hit in the ship, False
         otherwise.
        """
        if (pos in self._coordinates) and (pos not in self._hit_coors):
            self._is_hit = True
            self._hit_coors.append(pos)
            return True
        return False

    def terminated(self):
        """
        :return: True if all ship's coordinates were hit in previous turns, False
        otherwise.
        """
        for coordinate in self._coordinates:
            if coordinate not in self._hit_coors:
                return False
        return True

    def __contains__(self, pos):
        """
        Check whether the ship is found in a specific coordinate.
        :param pos: A tuple representing the coordinate for check.
        :return: True if one of the ship's coordinates is found in the given
        (x, y) coordinate, False otherwise.
        """
        if pos in self._coordinates:
            return True
        return False

    def coordinates(self):
        """
        Return ship's current coordinates on board.
        :return: A list of (x, y) tuples representing the ship's current
        occupying coordinates.
        """
        ships_coors = []
        if self._dir in (Direction.UP, Direction.DOWN):
            for val in range(self._len):
                new_y = self._y_pos + val
                ships_coors.append((self._x_pos, new_y))
        elif self._dir in (Direction.LEFT, Direction.RIGHT):
            for val in range(self._len):
                new_x = self._x_pos + val
                ships_coors.append((new_x, self._y_pos))
        return ships_coors

    def damaged_cells(self):
        """
        Return the ship's hit positions.
        :return: A list of tuples representing the (x, y) coordinates of the
         ship which were hit in past turns (If there are no hit coordinates,
         return an empty list). There is no importance to the order of the
         values in the returned list.
        """
        return self._hit_coors

    def direction(self):
        """
        Return the ship's current sailing direction.
        :return: One of the constants of Direction class :
         [UP, DOWN, LEFT, RIGHT] according to current sailing direction or
         NOT_MOVING if the ship is hit and not moving.
        """
        if self._is_hit:
            return Direction.NOT_MOVING
        return self._dir

    def cell_status(self, pos):
        """
        Return the status of the given coordinate (hit\not hit) in current ship.
        :param pos: A tuple representing the coordinate to query.
        :return:
            if the given coordinate is not hit : False
            if the given coordinate is hit : True
            if the coordinate is not part of the ship's body : None 
        """
        if pos in self._coordinates:
            if pos in self._hit_coors:
                return True
            return False
        return None

    def get_hit(self):
        """
        :return: True if one or more of the ship's coordinates is hit,
        False otherwise
        """
        return self._is_hit

