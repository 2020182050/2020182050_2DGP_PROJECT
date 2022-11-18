from pico2d import *
from Global_v import*

import game_framework

# Shop Action Speed
SHOP_TIME_PER_ACTION_TOP = 0.5
SHOP_ACTION_TOP_PER_TIME = 1.0 / SHOP_TIME_PER_ACTION_TOP
SHOP_FRAMES_PER_ACTION_TOP = 6

SHOP_TIME_PER_ACTION_SIGN = 0.8
SHOP_ACTION_SIGN_PER_TIME = 1.0 / SHOP_TIME_PER_ACTION_SIGN
SHOP_FRAMES_PER_ACTION_SIGN = 2

SHOP_TIME_PER_ACTION_POTAL = 1.0
SHOP_ACTION_POTAL_PER_TIME = 1.0 / SHOP_TIME_PER_ACTION_POTAL
SHOP_FRAMES_PER_ACTION_POTAL = 8

class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        self.frame_top = (self.frame_top + SHOP_FRAMES_PER_ACTION_TOP * SHOP_ACTION_TOP_PER_TIME * game_framework.frame_time) % SHOP_FRAMES_PER_ACTION_TOP
        self.frame_sign = (self.frame_sign + SHOP_FRAMES_PER_ACTION_SIGN * SHOP_ACTION_SIGN_PER_TIME * game_framework.frame_time) % SHOP_FRAMES_PER_ACTION_SIGN
        self.frame_potal = (self.frame_potal + SHOP_FRAMES_PER_ACTION_POTAL * SHOP_ACTION_POTAL_PER_TIME * game_framework.frame_time) % SHOP_FRAMES_PER_ACTION_POTAL
        
    @staticmethod
    def draw(self):
        self.shop_basic.clip_draw(0, 0, 256, 190, self.x, self.y)
        self.shop_top.clip_draw(int(self.frame_top)*122, 0, 122, 50, self.x - 5, self.y + 108)
        self.shop_sign.clip_draw(int(self.frame_sign)*82, 0, 82, 88, self.x - 60, self.y - 62)
        self.shop_potal.clip_draw(int(self.frame_potal)*88, 0, 88, 94, self.x - 5, self.y - 60)

class Shop():
    def __init__(self):
        self.x, self.y = size_of_window_x/2, 179
        self.frame_top = 0
        self.frame_sign = 0
        self.frame_potal = 0
        
        self.shop_basic = load_image('img/shop_basic.png')#294,228
        self.shop_top = load_image('img/shop_top.png')    #122,74
        self.shop_sign = load_image('img/shop_sign.png') #82,88
        self.shop_potal = load_image('img/shop_potal.png')#88,94

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def get_bb(self):
        return self.x - 44, self.y - 102, self.x + 34, self.y - 18

    def handle_event(self, event):
        pass
    
    def handle_collision(self, other, group):
        pass
        