##############################################################################################
# FILE : ex9.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION :
#   def __init__:
# A constructor for a Torpedo object
#   def get_lifetime:
# access to the torpedoes lifetime attribute
# :return: int, the torpedo lifetime
#   def get_radius:
# access to the torpedoes radius attribute
# :return: int, radius of torpedo
#   def get_heading:
# access to find out the torpedos attribute: heading
# :return: float, heading of torpedo in degrees
#   def get_coordinate_x:
# access to find out the torpedoes attribute: coordinate on X axis
# :return: int, coordinate on X axis of the torpedoes
#   def set_coordinate_x:
# changes the torpedoes coordinate on X axis to the parameter given
#   def get_coordinate_y:
# access to find out the torpedoes attribute: coordinate on Y axis
# :return: int, coordinate on Y axis of the torpedo
#   def set_coordinate_y:
# changes the torpedoes coordinate on Y axis to the parameter given
#   def get_speed_x:
# access to find out the torpedoes attribute: speed on X axis
# :return: int, speed on X axis of the torpedo
#   def set_speed_x:
# changes the torpedoes speed on X axis to the parameter given
#   def get_speed_y:
# access to find out the torpedoes attribute: speed on Y axis
# :return: int, speed on Y axis of the torpedo
#   def set_speed_y:
# changes the torpedoes speed on Y axis to the parameter given
#################################################################################




class Torpedo:
    """
    Class Torpedo description:
    A class representing a Torpedo in an Asteroids game.
    A torpedo is 1-dimensional object used by Ship Class that moves. it has a
    direction and speed that get set by ships data. it can change an asteroid
    instance when it hit it. and its lifetime is 200 rounds, or until it hits
    asteroid.
    """
    RADIUS = 4
    LIFETIME = 200

    def __init__(self, x, y, speed_x, speed_y, heading):
        """
        A constructor for a Torpedo object
        :param x: int representing the torpedoes location on X axis
        :param y: int representing the torpedoes location on Y axis
        :param speed_x: int, torpedo's speed on X axis
        :param speed_y: int, torpedo's speed on Y axis
        :param heading: int, the heading of torpedo in degrees
        """
        self._x = x
        self._y = y
        self._speed_x = speed_x
        self._speed_y = speed_y
        self._heading = heading
        self._round = 0

    def add_round_count(self):
        self._round += 1

    def get_round(self):
        return self._round

    def get_lifetime(self):
        """
        access to the torpedoes lifetime attribute
        :return: int, the torpedo lifetime
        """
        return self.LIFETIME

    def get_radius(self):
        """
        access to the torpedoes radius attribute
        :return: int, radius of torpedo
        """
        return self.RADIUS

    def get_heading(self):
        """
        access to find out the torpedos attribute: heading
        :return: float, heading of torpedo in degrees
        """
        return self._heading

    def get_coordinate_x(self):
        """
        access to find out the torpedoes attribute: coordinate on X axis
        :return: int, coordinate on X axis of the torpedoes
        """
        return self._x

    def set_coordinate_x(self, new_coor_x):
        """
        changes the torpedoes coordinate on X axis to the parameter given
        :param new_coor_x: int
        """
        self._x = new_coor_x

    def get_coordinate_y(self):
        """
        access to find out the torpedoes attribute: coordinate on Y axis
        :return: int, coordinate on Y axis of the torpedoes
        """
        return self._y

    def set_coordinate_y(self, new_coor_y):
        """
        changes the torpedoes coordinate on Y axis to the parameter given
        :param new_coor_y: int
        """
        self._y = new_coor_y

    def get_speed_x(self):
        """
        access to find out the torpedoes attribute: speed on X axis
        :return: int, speed on X axis of the torpedo
        """
        return self._speed_x

    def set_speed_x(self, new_speed_x):
        """
        changes the torpedoes speed on X axis to the parameter given
        :param new_speed_x: float
        """
        self._speed_x = new_speed_x

    def get_speed_y(self):
        """
        access to find out the torpedoes attribute: speed on Y axis
        :return: int, speed on Y axis of the torpedo
        """
        return self._speed_y

    def set_speed_y(self, new_speed_y):
        """
        changes the torpedoes speed on Y axis to the parameter given
        :param new_speed_y: float
        """
        self._speed_y = new_speed_y
