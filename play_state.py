from pico2d import *
from TileMap1 import *
from BgMap1 import *
import game_framework

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