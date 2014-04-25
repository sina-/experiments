import curses
import time

class ASCIIBird(object):
    def __init__(self):
        self.begin_x = 0
        self.begin_y = 0
        self.height = 10
        self.width = 20 
        self.stdscr = curses.initscr()
        self.win = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)
        #Hide the blinking cursor
        curses.curs_set(0)
        self.field = {i:['.']*self.width for i in xrange(self.height)}
        self.current_x = 0
        self.current_y = 0


    def _get_input(self):
        pass


    def _calc_location(self):
        self.old_x = self.current_x
        self.old_y = self.current_y
        self.current_x += 1
        self.current_y += 1
        self.current_x = self.current_x if self.current_x < self.width or self.current_x < 0 else 0
        self.current_y = self.current_y if self.current_y < self.height or self.current_y < 0 else 0


    def _update_field(self):
        self.field[self.old_y][self.old_x] = '.'
        self.field[self.current_y][self.current_x] = 'x'


    def _draw(self):
        for y, row in enumerate(self.field.itervalues()):
            for x, element in enumerate(row):
                #the try statement is to skip the last column since it fails advancing the cursor outside when we stil on the last column
                #check http://ubuntuforums.org/showthread.php?t=1306504
                try:
                    self.win.addch(y, x, element)
                except curses.error: 
                    pass
        self.win.refresh()


    def _draw_test(self):
        for i in self.field.itervalues():
            print i

    def play(self):
        while True:
            self._get_input()
            self._calc_location()
            self._update_field()
            self._draw()
            #self._draw_test()
            time.sleep(0.1)


def main():
    ascii_bird = ASCIIBird()
    ascii_bird.play()


if __name__=='__main__':
    main()
