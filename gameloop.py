from pico2d import*
from Global_v import*
import game_framework

import play_state
import shop_state
import inventory_state

open_canvas(size_of_window_x, size_of_window_y)
game_framework.fill_states(inventory_state)
game_framework.run(play_state)
clear_canvas()