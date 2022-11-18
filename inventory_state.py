from pico2d import *
import play_state
import game_framework
import game_world 

SLOT_MAX = 36
img_iv_board = None
iv_slot = None
img_iv_slot_off = None

class iv_slot_on():
    image = None

    def __init__(self, i, x, y):
        if i < SLOT_MAX:
            if self.image == None:
                self.image = load_image('img/922.png') # 34,34
            self.x = (x - 99) + (i% 6) * 34
            self.y = (y + 31) - (i//6) * 34
            self.size = 34
        else:
            return -1

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 17, self.y - 17, self.x + 17, self.y + 17

def enter(): pass

def exit(): pass

def update(): pass

def draw(): 
    clear_canvas()
    play_state.draw_world()
    img_iv_board.draw(154,214)
    for o in game_world.get_layer_object(3):
        o.draw()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):
            game_framework.push_state(play_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            game_framework.push_state(play_state)
        else:
            play_state.hero.handle_event(event)

def pause():
    global img_iv_board, img_iv_slot_off, iv_slot
    if img_iv_board == None:
        img_iv_board = load_image('img/iv_board.png')#308,428
    if img_iv_slot_off == None:
        img_iv_slot_off = load_image('img/964.png')# 34,34
    if iv_slot == None:
        iv_slots = [iv_slot_on(i, 154, 214) for i in range(18)]
        game_world.add_objects(iv_slots, 3)

    
    #if iv_del_item == None:
    #    iv_del_item = load_image('img/932.png')# 83,26 /self.x - 72 ,self.y - 181

def resume(): 
    pass

