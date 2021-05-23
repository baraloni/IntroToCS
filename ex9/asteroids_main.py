##############################################################################################
# FILE : ex9.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION :
#   def __init__:
# A constructor for a GameRunner object
#   def move_object:
# changes position of the given object
#   def run:
# runs the game
#   def _do_loop:
# runs the game loop in loops
#   def asteroid_split_to_one:
# creates a new, smaller asteroid which takes characters of the original
# asteroid and torpedo that hit it. the asteroid registers in Screen and
# GameRunner
#   def ship_part:
# conduct the ships movements, updates rotation speed and location
#   def asteroid_part:
# conduct all movement of all asteroids.
#   def torpedo_part:
# conducts all creation, registration, movements and disposal of
# torpedoes
#   def collision_ship_asteroid:
# when asteroid hits our ship: updates status of ship: lives, and of
# asteroid: registration
#   def collision_torpedo_asteroid:
# when torpedo hits asteroid: updates score, asteroid splits, updates
# torpedo and asteroids registration status
# def main:
# runs the game
####################################################################################

from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
from random import randint
import sys
import math

DEFAULT_ASTEROIDS_NUM = 3

LOSING_LIFE_TITLE = 'BE CAREFUL!'
LOSING_LIFE_MSG = 'You got hit by an asteroid!\nYou lost 1 life point.'

WIN_TITLE = 'HURRAY! :)'
WIN_MSG = 'You managed to survive the asteroid attack\nWELL DONE!'

LOSE_TITLE = 'OH NO...'
LOSE_MSG = "You're out of lives.\nBETTER LUCK NEXT TIME!"


class GameRunner:
    """
    Class GameRunner description:
    A class representing an Asteroids game.
    A game is composed of asteroids that are moving on a square board and a
    space ship controlled by user with the array keys, which can rotate,
    accelerate and fire torpedoed to destroy the asteroids.
    """
    SCORE = 0
    DEGREES = 7


    def __init__(self, asteroids_amnt):
        """
        A constructor for a GameRunner object
        :param asteroids_amnt: int, asteroids to start the game with
        """
        self._screen_max_x = Screen.SCREEN_MAX_X
        self._screen_max_y = Screen.SCREEN_MAX_Y
        self._screen_min_x = Screen.SCREEN_MIN_X
        self._screen_min_y = Screen.SCREEN_MIN_Y
        self._delta_x = self._screen_max_x - self._screen_min_x
        self._delta_y = self._screen_max_y - self._screen_min_y

        self._screen = Screen()

        self._my_ship = Ship(randint(self._screen_min_x, self._screen_max_x),
                            randint(self._screen_min_y, self._screen_max_y))

        self._asteroids = []
        for num in range(asteroids_amnt):
            self._asteroids.append(Asteroid(randint(self._screen_min_x,
                        self._screen_max_x), randint(self._screen_min_y,
                        self._screen_max_y), randint(10,30), randint(10,30),
                                           Asteroid._SIZE))
        for asteroid in self._asteroids:
            self._screen.register_asteroid(asteroid , asteroid.get_size())

    def move_object(self, obj):
        """
        changes position of the given object
        :param object: object from class Ship Torpedo or Asteroid
        :param x: int, self.x of the object: location on X axis
        :param y: int, self.y f the object: location on Y axis
        """
        new_coor_x = (obj.get_speed_x() + obj.get_coordinate_x() -
                      self._screen_min_x) % self._delta_x + self._screen_min_x
        new_coor_y = (obj.get_speed_y() + obj.get_coordinate_y() -
                      self._screen_min_y) % self._delta_y + self._screen_min_y
        obj.set_coordinate_x(new_coor_x)
        obj.set_coordinate_y(new_coor_y)

    def run(self):
        """
        runs the game
        """
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        """
        runs the game loop in loops
        """
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def asteroid_split_to_one(self, asteroid, torpedo, dir):
        """
        creates a new, smaller asteroid which takes characters of the original
        asteroid and torpedo that hit it. the asteroid registers in Screen and
        GameRunner
        :param asteroid: a given instance of Asteroid Class
        :param torpedo: a given instance of Torpedo Class
        :param dir: direction of the new asteroid : 1 or -1.
        """
        new_speed_x = (torpedo.get_speed_x() + dir*asteroid.get_speed_x()) /\
            ((asteroid.get_speed_x()**2 + asteroid.get_speed_y()**2)**(1/2))
        new_speed_y = (torpedo.get_speed_y() + dir*asteroid.get_speed_y()) /\
            ((asteroid.get_speed_x()**2 + asteroid.get_speed_y()**2)**(1/2))
        baby_asteroid = Asteroid(asteroid.get_coordinate_x(),
                    asteroid.get_coordinate_y(), new_speed_x, new_speed_y,
                                 (asteroid.get_size()-1))
        self._asteroids.append(baby_asteroid)
        self._screen.register_asteroid(baby_asteroid, baby_asteroid.get_size())

    def ship_part(self):
        """
        conduct the ships movements, updates rotation speed and location
        """
        if self._screen.is_up_pressed():
            self._my_ship.accelerate()
        elif self._screen.is_right_pressed():
            self._my_ship.set_heading(-self.DEGREES)
        elif self._screen.is_left_pressed():
            self._my_ship.set_heading(self.DEGREES)
        self.move_object(self._my_ship)
        self._screen.draw_ship(self._my_ship.get_coordinate_x(),
                self._my_ship.get_coordinate_y(), self._my_ship.get_heading())

    def asteroid_part(self):
        """
        conduct all movement of all asteroids.
        """
        for asteroid in self._asteroids:
            self.move_object(asteroid)
            self._screen.draw_asteroid(asteroid, asteroid.get_coordinate_x(),
                                       asteroid.get_coordinate_y())

    def torpedo_part(self):
        """
        conducts all creation, registration, movements and disposal of
        torpedoes
        """
        if self._screen.is_space_pressed() and len(self._my_ship.get_torpedo_list())\
                < self._my_ship.get_torpedo_limit():
            torpedo = self._my_ship.make_torpedo()
            self._screen.register_torpedo(torpedo)
        for torpedo in self._my_ship.get_torpedo_list():
            self.move_object(torpedo)
            self._screen.draw_torpedo(torpedo, torpedo.get_coordinate_x(),
                                      torpedo.get_coordinate_y(), torpedo.get_heading())
            if torpedo.get_round() == torpedo.get_lifetime():
                self._screen.unregister_torpedo(torpedo)
                self._my_ship.remove_torpedo(torpedo)
            else:
                torpedo.add_round_count()

    def collision_ship_asteroid(self):
        """
        when asteroid hits our ship: updates status of ship: lives, and of
        asteroid: registration
        """
        for asteroid in self._asteroids:
            if asteroid.has_intersection(self._my_ship):
                self._my_ship.set_life()
                self._screen.show_message(LOSING_LIFE_TITLE, LOSING_LIFE_MSG)
                self._screen.remove_life()
                self._screen.unregister_asteroid(asteroid)
                self._asteroids.remove(asteroid)

    def collision_torpedo_asteroid(self):
        """
        when torpedo hits asteroid: updates score, asteroid splits, updates
        torpedo and asteroids registration status
        """
        for torpedo in self._my_ship.get_torpedo_list():
            for asteroid in self._asteroids:
                if asteroid.has_intersection(torpedo):
                    self.SCORE += asteroid.get_size() * 10
                    self._screen.set_score(self.SCORE)
                    if asteroid.get_size() > 1:
                        self.asteroid_split_to_one(asteroid, torpedo, 1)
                        self.asteroid_split_to_one(asteroid, torpedo, -1)
                    self._screen.unregister_asteroid(asteroid)
                    self._asteroids.remove(asteroid)
                    if torpedo in self._my_ship.get_torpedo_list():
                    # when torpedo hits 2 asteroids simultaneously
                        self._screen.unregister_torpedo(torpedo)
                        self._my_ship.remove_torpedo(torpedo)

    def _game_loop(self):
        # exits:
        if self._asteroids == []:
            self._screen.show_message(WIN_TITLE, WIN_MSG)
            self._screen.end_game()
            sys.exit()
        elif self._my_ship.get_life() < 1:
            self._screen.show_message(LOSE_TITLE, LOSE_MSG)
            self._screen.end_game()
            sys.exit()
        elif self._screen.should_end():
            self._screen.end_game()
            sys.exit()
        # game conducting:
        self.ship_part()
        self.asteroid_part()
        self.collision_ship_asteroid()
        self.torpedo_part()
        self.collision_torpedo_asteroid()

def main(amnt):
    """
    runs the game
    :param amnt: asteroids instances amount in int
    :return:
    """
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )
