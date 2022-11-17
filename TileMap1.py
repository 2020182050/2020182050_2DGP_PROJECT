from pico2d import*
from Global_v import*

class TileMap1:
    tile_image = None
    def __init__(self,i):
        if TileMap1.tile_image == None:
            TileMap1.tile_image = load_image('img/42_tilemap.png')
        self.size = 42
        self.x = 21 + (i %  60) * 42
        self.y = 63 - (i // 60) * 42

    def draw(self):
        if self.y == 63:
            self.tile_image.clip_draw(self.size*12,self.size*2,self.size,self.size,self.x,self.y)
            draw_rectangle(*self.get_bb())
        else:
            self.tile_image.clip_draw(self.size*11,self.size*2,self.size,self.size,self.x,self.y)
            draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 21, self.y - 21, self.x + 21, self.y + 21

    def handle_collision(self, other, group):
        pass
