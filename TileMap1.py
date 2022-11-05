from pico2d import*

class TileMap1:
    def __init__(self):
        self.tile_image = load_image('img/42_tilemap.png')
        self.size = 42
        self.x = 21
        self.y = 21

    def draw(self):
        self.tile_image.clip_draw(self.size*12,self.size*2,self.size,self.size,self.x,self.y)
