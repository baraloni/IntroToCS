##############################################################################################
# FILE : ex9.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION :
# def __init__:
#    A constructor for a Ship object
# def accelerate:
#    changes the speed of the ship.
# def make_torpedo:
#    Creates a Torpedo instance and saves it to an inner list.
#    :return: Torpedo object created
# def remove_torpedo:
#    remove the given torpedo instance from the Ships inner list, that
#    monitors its torpedoes.
# def get_torpedo_list:
#    access to the ships torpedoes list that in air
#    :return: list of Torpedo class instances
# def get_torpedo_limit:
#    access to the ships attribute torpedoes limit at a time
#    :return: int, ships torpedo limit
# def get_radius:
#    access to find out the ships attribute: radius
#    :return:int, radius value ,  attribute of the ship
# def get_life:
#    access to find out the ships attribute: life
#    :return:int, life attribute of the ship
# def set_life:
#    reduce 1 life point from ships life attribute
# def get_heading:
#    access to find out the ships attribute: heading in degrees
#    :return: float, heading attribute of the ship (degrees)
# set_heading:
#    changes the ships heading attribute by adding the parameter degrees
# def get_coordinate_x:
#    access to find out the ships attribute: coordinate on X axis
#    :return: int, coordinate on X axis of the ship
# def set_coordinate_x:
#    changes the ships coordinate on X axis to the parameter given
#    :param new_coor_x: int
# def get_coordinate_y:
#    access to find out the ships attribute: coordinate on Y axis
#    :return: int, coordinate on Y axis of the ship
# def set_coordinate_y:
#    changes the ships coordinate on Y axis to the parameter given
#    :param new_coor_y: int
# def get_speed_x(self):
#    access to find out the ships attribute: speed on X axis
#    :return: int, speed on X axis of the ship
# def set_speed_x(self, new_speed_x):
#    changes the ships speed on X axis to the parameter given
#    :param new_speed_x: float
# def get_speed_y(self):
#    access to find out the ships attribute: speed on Y axis
#    :return: int, speed on Y axis of the ship
# def set_speed_y(self, new_speed_y):
#    changes the ships speed on Y axis to the parameter given
###################################################################################





import math
from torpedo import Torpedo


class Ship:
    """
    Class Ship description:
    A class representing a space ship in an Asteroids game.
    A ship is 1-dimensional object that can rotate accelerate and fire
    torpedoes (objects from Torpedo class), up to 15 at a time.
    If a ship is hit by an asteroid it loses one life point, out of 3.
    A ship that lost all life points is terminated.
    """
    TORPEDOES_LIMIT = 15
    HEADING = 0
    RADIUS = 1
    LIFE = 3
    ACC_FAC = 2  # acceleration factor for torpedo

    def __init__(self, x, y, speed_x=0, speed_y=0):
        """
        A constructor for a Ship object
        :param x: int representing the ships location on X axis
        :param y: int representing the ships location on Y axis
        :param speed_x: int, ships speed on X axis
        :param speed_y: int, ships speed on Y axis
        """
        self._x = x
        self._y = y
        self._speed_x = speed_x
        self._speed_y = speed_y
        self._torpedoes = []

    def accelerate(self):
        """
        changes the speed of the ship.
        """
        new_speed_x = self.get_speed_x() + math.cos(2 * math.pi *
                                                (self.get_heading() / 360))
        new_speed_y = self.get_speed_y() + math.sin(2 * math.pi *
                                                (self.get_heading() / 360))
        self.set_speed_x(new_speed_x)
        self.set_speed_y(new_speed_y)

    def make_torpedo(self):
        """
        Creates a Torpedo instance and saves it to an inner list.
        :return: Torpedo object created
        """
        new_speed_x = self.get_speed_x() + self.ACC_FAC * math.cos(2 *
                                        math.pi * (self.get_heading() / 360))
        new_speed_y = self.get_speed_y() + self.ACC_FAC * math.sin(2 *
                                        math.pi * (self.get_heading() / 360))
        torpedo = Torpedo(self.get_coordinate_x(), self.get_coordinate_y(),
                          new_speed_x, new_speed_y, self.get_heading())
        self._torpedoes.append(torpedo)
        return torpedo

    def remove_torpedo(self, torpedo):
        """
        remove the given torpedo instance from the Ships inner list, that
        monitors its torpedoes.
        :param torpedo: torpedo object
        """
        self._torpedoes.remove(torpedo)

    def get_torpedo_list(self):
        """
        access to the ships torpedoes list that in air
        :return: list of Torpedo class instances
        """
        return self._torpedoes

    def get_torpedo_limit(self):
        """
        access to the ships attribute torpedoes limit at a time
        :return: int, ships torpedo limit
        """
        return self.TORPEDOES_LIMIT

    def get_radius(self):
        """
        access to find out the ships attribute: radius
        :return:int, radius value ,  attribute of the ship
        """
        return self.RADIUS

    def get_life(self):
        """
        access to find out the ships attribute: life
        :return:int, life attribute of the ship
        """
        return self.LIFE

    def set_life(self):
        """
        reduce 1 life point from ships life attribute
        """
        self.LIFE -= 1

    def get_heading(self):
        """
        access to find out the ships attribute: heading in degrees
        :return: float, heading attribute of the ship (degrees)
        """
        return self.HEADING

    def set_heading(self,degrees):
        """
        changes the ships heading attribute by adding the parameter degrees
        :param degrees: int or float
        """
        self.HEADING = self.HEADING + degrees

    def get_coordinate_x(self):
        """
        access to find out the ships attribute: coordinate on X axis
        :return: int, coordinate on X axis of the ship
        """
        return self._x

    def set_coordinate_x(self, new_coor_x):
        """
        changes the ships coordinate on X axis to the parameter given
        :param new_coor_x: int
        """
        self._x = new_coor_x

    def get_coordinate_y(self):
        """
        access to find out the ships attribute: coordinate on Y axis
        :return: int, coordinate on Y axis of the ship
        """
        return self._y

    def set_coordinate_y(self, new_coor_y):
        """
        changes the ships coordinate on Y axis to the parameter given
        :param new_coor_y: int
        """
        self._y = new_coor_y

    def get_speed_x(self):
        """
        access to find out the ships attribute: speed on X axis
        :return: int, speed on X axis of the ship
        """
        return self._speed_x

    def set_speed_x(self, new_speed_x):
        """
        changes the ships speed on X axis to the parameter given
        :param new_speed_x: float
        """
        self._speed_x = new_speed_x

    def get_speed_y(self):
        """
        access to find out the ships attribute: speed on Y axis
        :return: int, speed on Y axis of the ship
        """
        return self._speed_y

    def set_speed_y(self, new_speed_y):
        """
        changes the ships speed on Y axis to the parameter given
        :param new_speed_y: float
        """
        self._speed_y = new_speed_y

