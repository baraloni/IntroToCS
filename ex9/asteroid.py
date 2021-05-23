##############################################################################################
# FILE : ex9.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION :
#   def __init__:
# A constructor for an Asteroid object
#   def has_intersection:
# checks for a collision between asteroid and obj
# :return: True if collision occurred, False otherwise
#   def get_radius:
# access to find out the asteroid attribute: radius
# :return:int, radius value ,  attribute of the asteroid
#   def get_size:
# access to find out the asteroid attribute: size
# :return: int, the size of the asteroid 1<size<3
#   def get_coordinate_x:
# access to find out the asteroids attribute: coordinate on X axis
# :return: int, coordinate on X axis of the asteroid
#   def set_coordinate_x:
# changes the asteroids coordinate on X axis to the parameter given
#   def get_coordinate_y:
# access to find out the asteroids attribute: coordinate on Y axis
# :return: int, coordinate on Y axis of the asteroid
#   def set_coordinate_y(self, new_coor_y):
# changes the asteroids coordinate on Y axis to the parameter given
#   def get_speed_x:
# access to find out the asteroids attribute: speed on X axis
# :return: int, speed on X axis of the asteroid
#   def set_speed_x:
# changes the asteroids speed on X axis to the parameter given
#   def get_speed_y:
# access to find out the asteroids attribute: speed on Y axis
# :return: int, speed on Y axis of the asteroid
#   def set_speed_y(self, new_speed_y):
# changes the asteroids speed on Y axis to the parameter given
#########################################################################

class Asteroid:
    """
    Class Asteroid description:
    A class representing an asteroid in an Asteroids game.
    An asteroid is 1-dimensional object that moves. it has a default
    size (3 of 3) and direction. whenever it get hit by a torpedo it splits
    into 2 smaller asteroids, when an asteroid in its smaller formation is hit it
    is terminated. if it hits a space ship it is terminated.
    """
    _SIZE = 3
    RADIUS_COEF = 10
    RADIUS_FACTOR = -5

    def __init__(self, x, y, speed_x, speed_y, size=_SIZE):
        """
        A constructor for an Asteroid object
        :param x: int representing the asteroid's location on X axis
        :param y: int representing the asteroid's location on Y axis
        :param speed_x: int, asteroids speed on X axis
        :param speed_y: int, asteroids speed on Y axis
        :param size: int 1<size<3, default is 3
        """
        self._x = x
        self._y = y
        self._speed_x = speed_x
        self._speed_y = speed_y
        self._size = size
        self._radius = (self._size * self.RADIUS_COEF) + self.RADIUS_FACTOR

    def has_intersection(self, obj):
        """
        checks for a collision between asteroid and obj
        :param obj: an instance from another class: Ship or Torpedo
        :return: True if collision occurred, False otherwise
        """
        distance = ((obj._x - self._x)**2 + (obj._y - self._y)**2)**(1/2)
        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False

    def get_radius(self):
        """
        access to find out the asteroid attribute: radius
        :return:int, radius value ,  attribute of the asteroid
        """
        return self._radius

    def get_size(self):
        """
        access to find out the asteroid attribute: size
        :return: int, the size of the asteroid 1<size<3
        """
        return self._size

    def get_coordinate_x(self):
        """
        access to find out the asteroids attribute: coordinate on X axis
        :return: int, coordinate on X axis of the asteroid
        """
        return self._x

    def set_coordinate_x(self, new_coor_x):
        """
        changes the asteroids coordinate on X axis to the parameter given
        :param new_coor_x: int
        """
        self._x = new_coor_x

    def get_coordinate_y(self):
        """
        access to find out the asteroids attribute: coordinate on Y axis
        :return: int, coordinate on Y axis of the asteroid
        """
        return self._y

    def set_coordinate_y(self, new_coor_y):
        """
        changes the asteroids coordinate on Y axis to the parameter given
        :param new_coor_y: int
        """
        self._y = new_coor_y

    def get_speed_x(self):
        """
        access to find out the asteroids attribute: speed on X axis
        :return: int, speed on X axis of the asteroid
        """
        return self._speed_x

    def set_speed_x(self, new_speed_x):
        """
        changes the asteroids speed on X axis to the parameter given
        :param new_speed_x: float
        """
        self._speed_x = new_speed_x

    def get_speed_y(self):
        """
        access to find out the asteroids attribute: speed on Y axis
        :return: int, speed on Y axis of the asteroid
        """
        return self._speed_y

    def set_speed_y(self, new_speed_y):
        """
        changes the asteroids speed on Y axis to the parameter given
        :param new_speed_y: float
        """
        self._speed_y = new_speed_y