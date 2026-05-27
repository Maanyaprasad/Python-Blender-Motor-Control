from ursina import *
from ursina.prefabs.slider import Slider
from ursina.prefabs.button import Button

app = Ursina()

rotation_speed = 0
is_running = False

motor = Entity(
    model='models/motor.glb',
    scale=1,
    position=(-1,0,0)
)

pulley = Entity(
    model='models/pulley.glb',
    scale=1,
    position=(2,0,0)
)

def start_rotation():
    global is_running
    is_running = True

def stop_rotation():
    global is_running
    is_running = False

def update():
    global rotation_speed

    rotation_speed = speed_slider.value

    if is_running:
        pulley.rotation_z += rotation_speed

start_button = Button(
    text='Start',
    color=color.green,
    position=(-0.35, -0.4),
    scale=0.4
)

start_button.on_click = start_rotation

stop_button = Button(
    text='Stop',
    color=color.red,
    position=(0.35, -0.4),
    scale=0.4
)

stop_button.on_click = stop_rotation

speed_slider = Slider(
    min=0,
    max=10,
    default=1,
    position=(0, -0.6),
    scale=0.5
)

app.run()