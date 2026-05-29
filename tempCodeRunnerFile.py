from ursina import *
from ursina.prefabs.slider import Slider
from ursina.prefabs.button import Button

app = Ursina()

rotation_speed = 0
is_running = False

# Nema 17 stepper Motor GT3 Pulley part

motor = Entity(
    model='models/nemapulley.glb',
    scale=0.8,
    position=(-2,2,0),
    rotation=(0,90,0),
    texture='texture_blend.png',
)

# Nema 17 stepper Motor body part 
motor_body = Entity(
    model='models/nemamotorbody.glb',
    scale=0.6,
    position=(-2,0,0),
    rotation=(0,90,0),
    texture='texture_blend.png',
)

# Nema 17 stepper motor shaft part

shaft = Entity(
    model='models/nemashaft.glb',
    scale=0.8,
    position=(-2,0,0),
    rotation=(0,90,0),
    texture='texture_blend.png',
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
        motor.rotation_y += rotation_speed
        shaft.rotation_y += rotation_speed  

#---------------------------------------------------------------
#         START/STOP BUTTONS AND SPEED CONTROL SLIDER BAR BUTTON
#---------------------------------------------------------------


start_button = Button(
    text='Start',
    color=color.green,
    position=(-0.35, -0.4),
    scale=0.2
)

start_button.on_click = start_rotation

stop_button = Button(
    text='Stop',
    color=color.red,
    position=(0.6, -0.4),
    scale=0.2
)

stop_button.on_click = stop_rotation

speed_slider = Slider(
    min=0,
    max=10,
    default=1,
    position=(0, -0.4),
    scale=0.6,
    step=0.1
)

app.run()