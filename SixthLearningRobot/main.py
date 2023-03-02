#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import robot, lib

CLEAR = 0
CLOSE_OBEJCT_LEFT = 1
MID_OBJECT_LEFT = 2
FAR_OBJECT_LEFT = 3
CLOSE_OBEJCT_MIDDLE = 4
MID_OBJECT_MIDDLE = 5
FAR_OBJECT_MIDDLE = 6
CLOSE_OBEJCT_RIGHT = 7
MID_OBJECT_RIGHT = 8
FAR_OBJECT_RIGHT = 9

def find_state(bot):
    distance_left = bot.sonar_left.distance()
    distance_middle = bot.sonar_middle.distance()
    distance_right = bot.sonar_right.distance()
    if 0 <= distance_left <= 200:
        return CLOSE_OBEJCT_LEFT
    elif 200 <= distance_left <= 400:
        return MID_OBJECT_LEFT
    elif 400 <= distance_left <= 600:
        return FAR_OBJECT_LEFT
    elif 0 <= distance_middle <= 200:
        return CLOSE_OBEJCT_MIDDLE
    elif 200 <= distance_middle <= 400:
        return MID_OBJECT_MIDDLE
    elif 400 <= distance_middle <= 600:
        return FAR_OBJECT_MIDDLE
    elif 0 <= distance_right <= 200:
        return CLOSE_OBEJCT_RIGHT
    elif 200 <= distance_right <= 400:
        return MID_OBJECT_RIGHT
    elif 400 <= distance_right <= 600:
        return FAR_OBJECT_RIGHT 
    else:
        return CLEAR


def reward(bot, state, action):
    if state == CLOSE_OBEJCT_RIGHT:
        return -10
    elif state == MID_OBJECT_RIGHT:
        return -5
    elif (state == FAR_OBJECT_RIGHT) or (state == FAR_OBJECT_MIDDLE):
        return -1
    elif state == MID_OBJECT_MIDDLE:
        return 0
    elif (state == CLOSE_OBEJCT_MIDDLE) or (state == FAR_OBJECT_LEFT):
        return 1
    elif state == MID_OBJECT_LEFT:
        return 5
    elif state == CLOSE_OBEJCT_LEFT:
        return 10
    elif action == 0:
        return 1
    else:
        return 0

params = lib.QParameters()
params.pause_ms = 500
params.actions = [robot.go_forward, robot.go_left, robot.go_right, robot.go_back]
params.num_states = 10
params.state_func = find_state
params.reward_func = reward
params.target_visits = 5
params.discount = 0.5
params.rate_constant = 10
params.max_steps = 200

ev3 = EV3Brick()

lib.run_q(robot.SensorMotor(ev3), params)