from pico2d import *
from Global_v import*
from random import*
import game_framework

# MOB Run Speed
MOB_RUN_BASIC_SPEED_MPS = 6 # m/s
MOB_RUN_SPEED_MPS = 6
MOB_RUN_SPEED_PPS = (MOB_RUN_SPEED_MPS * PIXEL_PER_METER)
MOB_FLY_SPEED_MPSS = 0
MOB_FLY_SPEED_PPSS = (MOB_FLY_SPEED_MPSS * PIXEL_PER_METER)

# MOB Action Speed
MOB_TIME_PER_ACTION = 1.0
MOB_ACTION_PER_TIME = 1.0 / MOB_TIME_PER_ACTION
MOB_FRAMES_PER_ACTION = 4

# MOB Action Time Interval
MOB_ACTION_TIME_INTERVAL = 0.0

def init_time_interval():
    global MOB_ACTION_TIME_INTERVAL
    MOB_ACTION_TIME_INTERVAL = 0.0

def update_speed():
    global MOB_FLY_SPEED_MPSS, MOB_FLY_SPEED_PPSS
    MOB_FLY_SPEED_PPSS = (MOB_FLY_SPEED_MPSS * PIXEL_PER_METER)

#이벤트 정의
HP_0 = range(1)
event_name = ['HP_0']

class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + MOB_FRAMES_PER_ACTION * MOB_ACTION_PER_TIME * game_framework.frame_time) % MOB_FRAMES_PER_ACTION
        self.x += self.dir * MOB_RUN_SPEED_PPS * game_framework.frame_time
        self.y += (GRAVITY_PPSS + MOB_FLY_SPEED_PPSS) * game_framework.frame_time * MOB_ACTION_TIME_INTERVAL / 2.0
        
    @staticmethod
    def draw(self):
        #46,44
        if self.dir == 1:
            self.image.clip_draw(int(self.frame)*46, 44 * self.color, 46, 44, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*46, 44 * self.color, 46, 44, 0, 'h', self.x, self.y, 46, 44)


class DEAD:
    @staticmethod
    def enter(self,event):
        print('ENTER DEAD')

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + MOB_FRAMES_PER_ACTION * MOB_ACTION_PER_TIME * game_framework.frame_time) % MOB_FRAMES_PER_ACTION
        
    @staticmethod
    def draw(self):
        #46,44
        self.image.clip_draw(int(self.frame)*42, 0, 42, 56, self.x, self.y)

next_state = {
    IDLE:  {HP_0:DEAD},
    DEAD:  {}
}

class Mob:
    def __init__(self, color = 0, x = 400, y = 111):
        self.x, self.y = x, y
        self.frame = 0
        self.color = color
        self.dir = -1 if randint(0,1) else 1
        self.image = load_image('img/Mob.png')
        
        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        global MOB_ACTION_TIME_INTERVAL
        MOB_ACTION_TIME_INTERVAL += game_framework.frame_time
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Dir: {self.dir}')
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def get_bb(self):
        return self.x - 23, self.y - 22, self.x + 23, self.y + 22

    def handle_event(self, event):
        pass
    
    def handle_collision(self, other, group):
        #print(other, " - ", group)
        left_self, bottom_self, right_self, top_self = self.get_bb()
        left_other, bottom_other, right_other, top_other = other.get_bb()
        if group == 'mob:tilemap':
            if top_other > bottom_self:
                global MOB_FLY_SPEED_MPSS
                MOB_FLY_SPEED_MPSS = -GRAVITY_MPSS
                update_speed()
                init_time_interval()
        if group == 'hero:mob':
            pass