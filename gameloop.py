from pico2d import*
import game_framework

import title_state
import play_state

open_canvas()

game_framework.run(play_state)
clear_canvas()