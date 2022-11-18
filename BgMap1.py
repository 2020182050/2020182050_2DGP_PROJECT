from pico2d import*
from Global_v import*

class BgMap1:
    def __init__(self):
        self.bg_image = load_image('img/1484.jpg')

    def update(self):
        pass

    def draw(self):
        self.bg_image.draw(size_of_window_x/2, size_of_window_y/2, size_of_window_x, size_of_window_y)