from pico2d import *
import game_framework
import game_world 

from TileMap1 import *
from BgMap1 import *
from Hero import*

hero = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            hero.handle_event(event)



def enter():
    global hero
    hero = Hero()
    tilemap = [TileMap1(i) for i in range(120)]
    bgmap = BgMap1()
    game_world.add_object(hero,2)
    game_world.add_objects(tilemap, 1)
    game_world.add_object(bgmap, 0)

def exit():
    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
    
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass