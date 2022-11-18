from pico2d import *
import game_framework
import game_world 

def enter(): pass

def exit(): pass

def update(): pass

def draw(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

def pause(): pass

def resume(): pass

