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
LEFT_BUMP = 1
RIGHT_BUMP = 2
CLOSE_OBEJCT = 3
MID_OBJECT = 4
FAR_OBJECT = 5

def find_state(bot):
    distance = bot.sonar.distance()
    if bot.bump_left.pressed():
        return LEFT_BUMP
    elif bot.bump_right.pressed():
        return RIGHT_BUMP
    elif 0 <= distance <= 200:
        return CLOSE_OBEJCT
    elif 200 <= distance <= 400:
        return MID_OBJECT
    elif 400 <= distance <= 600:
        return FAR_OBJECT
    else:
        return CLEAR


def reward(bot, state, action):
    if (state == LEFT_BUMP) or (state == RIGHT_BUMP) or (state == CLOSE_OBEJCT):
        return -10
    elif state == MID_OBJECT:
        return -5
    elif state == FAR_OBJECT:
        return 0
    elif action == 0:
        return 1
    else:
        return 0

params = lib.QParameters()
params.pause_ms = 500
params.actions = [robot.go_forward, robot.go_left, robot.go_right, robot.go_back]
params.num_states = 6
params.state_func = find_state
params.reward_func = reward
params.target_visits = 5
params.discount = 0.5
params.rate_constant = 10
params.max_steps = 200

lib.run_q(robot.SensorMotor(ev3), params)