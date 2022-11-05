from pico2d import *
import game_framework

class Grass:
    def __init__(self):
        self.image = load_image('img/grass.png')

    def draw(self):
        self.image.draw(400, 30)

class BgMap1:
    def __init__(self):
        self.bg_image = load_image('img/1484.jpg')

    def draw(self):
        self.bg_image.draw(400, 300,800,600)

class TileMap1:
    def __init__(self):
        self.tile_image = load_image('img/42_tilemap.png')
        self.size = 42
        self.x = 21
        self.y = 21

    def draw(self):
        self.tile_image.clip_draw(self.size*12,self.size*2,self.size,self.size,self.x,self.y)

class Koog:
    def __init__(self):
        self.image = load_image('img/Koog_sprite.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

bgmap1 = None
tilemap1 = []

def enter():
    global tilemap1,bgmap1
    tilemap1 = [TileMap1() for i in range(60)]
    bgmap1 = BgMap1()

def exit():
    global tilemap1,bgmap1
    del tilemap1,bgmap1

def update():
    pass

def draw():
    clear_canvas()
    bgmap1.draw()
    for i,tile in enumerate(tilemap1):
        tile.x = i*42 + 21
        tile.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass