import robot, lib

CLEAR = 0
BUMPED = 1
OBJECT = 2

def find_state(bot):
    distance = bot.sonar.distance()
    if bot.bump_left.pressed() and bot.bump_right.pressed():
        return BUMPED
    elif distance < 400:
        return OBJECT
    else:
        return CLEAR


def reward(bot, state, action):
    if state == BUMPED:
        return -10
    elif action == 0:
        return 1
    else:
        return 0

params = lib.QParameters()
params.pause_ms = 500
params.actions = [robot.go_forward, robot.go_right]
params.num_states = 3
params.state_func = find_state
params.reward_func = reward
params.target_visits = 5
params.discount = 0.5
params.rate_constant = 10
params.max_steps = 200