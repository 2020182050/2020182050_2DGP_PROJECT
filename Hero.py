from pico2d import *
from Global_v import*
import game_world

#1 : 이벤트 정의
RD, LD, RU, LU = range(4)
event_name = ['RD', 'LD', 'RU', 'LU'] #이벤트 숫자로 부터 이름찾기
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
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
        self.frame = (self.frame + 1) % 2

    @staticmethod
    def draw(self):
        #40/65
        #52/59
        #42/55
        #42/55
        self.image.clip_draw(self.frame*42, 0, 42, 55, self.x, self.y)
        


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
        self.frame = (self.frame + 1) % 2
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        #40/65
        #52/59
        #42/55
        #42/55
        if self.dir == -1:
            self.image.clip_draw(self.frame*42, 55, 42, 55, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(84 + self.frame*42, 55, 42, 55, self.x, self.y)

#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}

class Hero:

    def __init__(self):
        self.x, self.y = 800 // 2, 111
        self.frame = 0
        self.dir = 0
        self.image = load_image('img/Koog_sprite.png')
        
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
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                #에러가 발생했으면, 그 때 상태와 이벤트를 출력한다.
                print(self.cur_state, event_name[event])
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Dir: {self.dir}')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)