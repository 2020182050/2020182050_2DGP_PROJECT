from pico2d import *

import game_framework
import play_state

main_image = None
press_any_key_image = None

def enter():
    global main_image
    global press_any_key_image
    main_image = load_image('img/1646.jpg')
    press_any_key_image = load_image('img/1648.png')

def exit():
    global main_image, press_any_key_image
    del main_image, press_any_key_image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.change_state(play_state)

def draw():
    clear_canvas()
    main_image.draw(400,300,800,600)
    press_any_key_image.draw(400,100)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






