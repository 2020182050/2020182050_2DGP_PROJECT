from pico2d import*

size_of_window_x = 800
size_of_window_y = 600

class BgMap1:
    def __init__(self):
        self.bg_image = load_image('img/1484.jpg')

    def draw(self):
        self.bg_image.draw(size_of_window_x/2, size_of_window_y/2, size_of_window_x, size_of_window_y)
