from pico2d import *
from Global_v import*
import game_framework

# Hero Run Speed
HERO_RUN_BASIC_SPEED_MPS = 6 # m/s
HERO_FLY_BASIC_SPEED_MPSS = 50 # m/s^2
HERO_RUN_SPEED_MPS = 6 
HERO_RUN_SPEED_PPS = (HERO_RUN_SPEED_MPS * PIXEL_PER_METER)
HERO_FLY_SPEED_MPSS = 0 
HERO_FLY_SPEED_PPSS = (HERO_FLY_SPEED_MPSS * PIXEL_PER_METER)

# Hero Action Speed
HERO_TIME_PER_ACTION = 0.5
HERO_ACTION_PER_TIME = 1.0 / HERO_TIME_PER_ACTION
HERO_FRAMES_PER_ACTION = 2

def update_speed():
    global HERO_RUN_SPEED_MPS, HERO_RUN_SPEED_PPS
    HERO_RUN_SPEED_PPS = (HERO_RUN_SPEED_MPS * PIXEL_PER_METER)

    global HERO_FLY_SPEED_MPSS, HERO_FLY_SPEED_PPSS
    HERO_FLY_SPEED_PPSS = (HERO_FLY_SPEED_MPSS * PIXEL_PER_METER)

#1 : 이벤트 정의
RD, LD, UD, RU, LU, UU = range(6)
event_name = ['RD', 'LD', 'UD', 'RU', 'LU', 'UU'] #이벤트 숫자로 부터 이름찾기
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU
}

#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 0

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + HERO_FRAMES_PER_ACTION * HERO_ACTION_PER_TIME * game_framework.frame_time) % 2
        self.y += (GRAVITY_PPSS + HERO_FLY_SPEED_PPSS) * game_framework.frame_time * game_framework.frame_time_sum / 2.0

    @staticmethod
    def draw(self):
        #40/65
        #52/59
        #42/55
        #42/55
        self.image.clip_draw(int(self.frame)*42, 0, 42, 54, self.x, self.y)
        


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + HERO_FRAMES_PER_ACTION * HERO_ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x += self.dir * HERO_RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 800)
        self.y += (GRAVITY_PPSS + HERO_FLY_SPEED_PPSS) * game_framework.frame_time * game_framework.frame_time_sum / 2.0

    def draw(self):
        #40/65
        #52/59
        #42/55
        #42/55
        if self.dir == -1:
            self.image.clip_draw(int(self.frame)*42, 55, 42, 55, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(84 + int(self.frame)*42, 55, 42, 55, self.x, self.y)

class FLY:
    @staticmethod
    def enter(self,event):
        print('ENTER FLY')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        global HERO_FLY_SPEED_MPSS
        HERO_FLY_SPEED_MPSS = HERO_FLY_BASIC_SPEED_MPSS
        update_speed()

    @staticmethod
    def exit(self, event):
        global HERO_FLY_SPEED_MPSS
        HERO_FLY_SPEED_MPSS = 0
        update_speed()
        if event_name[event] == 'UU':
            game_framework.init_frame_time_sum()

    @staticmethod
    def do(self):
        self.frame = 0
        self.x += self.dir * HERO_RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 800)
        self.y += 1 + (GRAVITY_PPSS + HERO_FLY_SPEED_PPSS) * game_framework.frame_time * game_framework.frame_time_sum / 2.0

    @staticmethod
    def draw(self):
        #40/65
        #52/59
        #42/55
        #42/55
        self.fire.clip_composite_draw(0, 0, 78, 41,
                            -3.141592 / 2, '', self.x - 7, self.y - 27, 24, 12)
        self.fire.clip_composite_draw(0, 0, 78, 41,
                            -3.141592 / 2, '', self.x + 7, self.y - 27, 24, 12)
        self.image.clip_draw(int(self.frame)*42, 0, 42, 54, self.x, self.y)
        

#3. 상태 변환 구현

next_state = {
    IDLE:  {RD: RUN,  LD: RUN,  UD:FLY,  RU: RUN,  LU: RUN,  UU:FLY },
    RUN:   {RD: IDLE, LD: IDLE, UD:FLY,  RU: IDLE, LU: IDLE, UU:FLY },
    FLY:   {RD: FLY,  LD: FLY,  UD:IDLE, RU: FLY,  LU: FLY,  UU:IDLE}
}

class Hero:
    def __init__(self):
        self.x, self.y = 800 // 2, 600
        self.frame = 0
        self.dir = 0
        self.image = load_image('img/Koog_sprite.png')
        self.fire = load_image('img/808.png')
        
        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                print(f'{self.cur_state},{event_name[event]},{self.dir}')
                if (self.cur_state, event_name[event]) == (FLY,'UU') and self.dir != 0:
                    global next_state
                    next_state[FLY] = {RD: RUN,  LD: RUN,  UD:RUN, RU: RUN,  LU: RUN,  UU:RUN}
                    self.cur_state = next_state[self.cur_state][event]
                    next_state[FLY] = {RD: FLY,  LD: FLY,  UD:IDLE, RU: FLY,  LU: FLY,  UU:IDLE}
                else:
                    self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                #에러가 발생했으면, 그 때 상태와 이벤트를 출력한다.
                print(self.cur_state, event_name[event])
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Dir: {self.dir}')
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def get_bb(self):
        return self.x - 21, self.y - 27, self.x + 21, self.y + 27

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
    
    def handle_collision(self, other, group):
        #print(other, " - ", group)
        left_self, bottom_self, right_self, top_self = self.get_bb()
        left_other, bottom_other, right_other, top_other = other.get_bb()
        if group == 'hero:tilemap':
            if top_other > bottom_self:
                global HERO_FLY_SPEED_MPSS
                HERO_FLY_SPEED_MPSS = -GRAVITY_MPSS
                update_speed()
                game_framework.init_frame_time_sum()