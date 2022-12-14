from pico2d import *
import shop_state
import inventory_state
import game_framework
import game_world 

from TileMap1 import *
from BgMap1 import *
from Hero import*
from Mob import*
from Shop import*

hero = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):
            game_framework.push_state(inventory_state)
        else:
            hero.handle_event(event)

def enter():
    global hero
    hero = Hero()
    tilemaps = [TileMap1(i) for i in range(120)]
    shop = Shop()
    #mobs = [Mob(0, 300 + 100 * i, 111) for i in range(2)]
    bgmap = BgMap1()
    game_world.add_object(hero, 2)
    #game_world.add_objects(mobs, 2)
    game_world.add_object(shop, 1)
    game_world.add_objects(tilemaps, 1)
    game_world.add_object(bgmap, 0)
    #game_world.add_collision_pairs(hero, mobs, 'hero:mob')
    game_world.add_collision_pairs(hero, tilemaps, 'hero:tilemap')
    game_world.add_collision_pairs(hero, shop, 'hero:shop')
    #game_world.add_collision_pairs(mobs, tilemaps, 'mob:tilemap')

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    
    for a, b, group in game_world.all_collision_pairs():
        if group == 'hero:shop':
            pass
            #game_framework.push_state(shop_state)
        if collide(a,b):
            #print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)
    
    #for game_object in game_world.all_objects():
    #    game_object.update()

def draw_world():
    for i in range(3):
        for game_object in game_world.get_layer_object(i):
            game_object.draw()
    
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()