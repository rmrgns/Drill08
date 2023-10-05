from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.select = random.randint(0, 1)
        if self.select == 1:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.speed = random.randint(10,50)
    def update(self):
        if self.y > 50:
            self.y -= self.speed
        else:
            self.y = 50
    def draw(self):
        if self.select == 1:
            self.image.clip_draw(0,0,23,23,self.x,self.y)
        else:
            self.image.clip_draw(0, 0, 43, 43, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global ball21
    running = True
    grass = Grass()
    ball21 = [Ball() for i in range(20)]


def update_world():
    grass.update()
    for ball in ball21:
        ball.update()

    pass

def render_world():
    clear_canvas()

    grass.draw()
    for ball in ball21:
        ball.draw()

    update_canvas()

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
