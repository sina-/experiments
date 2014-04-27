import curses
import time
import random

class ASCIIBird(object):
    def __init__(self):
        self.begin_x = 0
        self.begin_y = 0
        self.height = 10
        self.width = 20 
        self.current_x = 0
        self.current_y = 5
        self.turn_counter = 0
        self.max_num_walls = 3
        self.game_speed = 10

        self.stdscr = curses.initscr()
        self.stdscr.nodelay(1)
        self.win = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)
        """ hide the blinking cursor """
        curses.curs_set(0)
        curses.noecho()

        """ keys identifies the rows and values are list of chars identifying columns """
        self.field = {}
        """ keys identifying the location of the wall on x axis
            values are tuples with first element identifying height, and second element specifiying top, 0, or bottom, 1 """
        self.walls = {}

        self.player_char = 'x'
        self.field_char = '.'
        self.wall_char = '#'

        self._init_field()

        self.game_on = True


    def _bound_correction(self, position, limit):
        return position if position < limit or position < 0 else 0


    def _check_collision(self):
        return self.field[self.current_y][self.current_x] == self.wall_char


    def _get_input(self):
        user_input = self.stdscr.getch()
        if user_input == ord('w') or user_input == ord('k'):
            self.current_y -= 1
        elif user_input == ord('s') or user_input == ord('j'):
            self.current_y += 1
        elif user_input == ord('d') or user_input == ord('l'):
            self.current_x += 1
        elif user_input == ord('a') or user_input == ord('h'):
            self.current_x -= 1


    def _init_field(self):
        self.field = {i:[self.field_char]*self.width for i in xrange(self.height)}


    def _update(self):
        self._update_walls()
        self._update_location()
        self._update_field()
        self.turn_counter += 1


    def _update_walls(self):
        """ spawn a new wall """
        if self.turn_counter % (self.width / self.max_num_walls) == 0:
            wall_height = random.randint(2, 5)
            wall_location = random.randint(0, 1)
            self.walls[self.width] = (wall_height, wall_location)

        """ advance the wall by one block """
        self.walls = {x-1: height_tuple for x, height_tuple in self.walls.iteritems()}

        """ remove out-of-field-range walls """
        for wall in dict(self.walls).iterkeys():
            if wall >= self.width or wall < 0:
                del self.walls[wall]


    def _update_location(self):
#        self.current_x += 1
#        self.current_y += 1
        self.current_x = self._bound_correction(self.current_x, self.width)
        self.current_y = self._bound_correction(self.current_y, self.height)


    def _update_field(self):
        self._init_field()
        for brick_x, height_tuple in self.walls.iteritems():
            for brick_y in xrange(height_tuple[0]):
                """ decide the wall location, top or bottom """
                if height_tuple[1]:
                    self.field[brick_y][brick_x] = self.wall_char
                else:
                    self.field[self.height - brick_y - 1][brick_x] = self.wall_char

        if self._check_collision():
            self.win.erase()
            curses.endwin()
            self.game_on = False

        self.field[self.current_y][self.current_x] = self.player_char


    def _draw(self):
        for y, row in self.field.iteritems():
            for x, element in enumerate(row):
                """ the try statement is to avoid moving the cursor out-of-range when x == self.width - 1
                    check http://ubuntuforums.org/showthread.php?t=1306504 for the issue """
                try:
                    self.win.addch(y, x, element)
                except curses.error: 
                    pass
        self.win.refresh()


    def _draw_test(self):
        for i in self.field.itervalues():
            print i


    def play(self):
        while self.game_on:
            self._get_input()
            self._update()
            self._draw()
            time.sleep(1 / float(self.game_speed))
        print("Game over, you hit the wall!")


def main():
    ascii_bird = ASCIIBird()
    ascii_bird.play()


if __name__=='__main__':
    main()
