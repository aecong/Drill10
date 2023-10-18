from pico2d import *

import game_world
from Backgrass import BackGrass
from grass import Grass
from boy import Boy


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global grass1
    global grass2
    global team
    global boy

    running = True

    grass1 = Grass()
    grass2 = BackGrass()
    game_world.add_object(grass1, 0)
    game_world.add_object(grass2, 2)

    boy = Boy()
    game_world.add_object(boy, 1)



def update_world():
    game_world.update()



def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
