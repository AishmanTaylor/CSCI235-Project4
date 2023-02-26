#!/usr/bin/env pybricks-micropython
import robot, lib

CLEAR = 0
BUMPED = 1
CLOSE_OBEJCT = 2
MID_OBJECT = 3
FAR_OBJECT = 4

def find_state(bot):
    distance = bot.sonar.distance()
    if bot.bump_left.pressed() or bot.bump_right.pressed():
        return BUMPED
    elif 0 <= distance <= 200:
        return CLOSE_OBEJCT
    elif 200 <= distance <= 400:
        return MID_OBJECT
    elif 400 <= distance <= 600:
        return FAR_OBJECT
    else:
        return CLEAR


def reward(bot, state, action):
    if state == BUMPED:
        return -10
    elif state == CLOSE_OBEJCT:
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
params.actions = [robot.go_forward, robot.go_left]
params.num_states = 5
params.state_func = find_state
params.reward_func = reward
params.target_visits = 5
params.discount = 0.5
params.rate_constant = 10
params.max_steps = 200
