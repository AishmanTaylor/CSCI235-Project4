from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
import pybricks.nxtdevices


class SensorMotor:
    def __init__(self, ev3):
        self.ev3 = ev3
        self.left = Motor(Port.A)
        self.right = Motor(Port.D)
        self.sonar_left = pybricks.nxtdevices.UltrasonicSensor(Port.S1)
        self.sonar_right = pybricks.nxtdevices.UltrasonicSensor(Port.S4)
        self.sonar_middle = UltrasonicSensor(Port.S2)
        self.loops = 0

    def stop_all(self):
        self.left.run(0)
        self.right.run(0)

    def values(self):
        return ["SL:" + str(self.sonar_left.distance()),
            "SR:" + str(self.sonar_right.distance()),
            "SM:" + str(self.sonar_middle.distance())]

    def show(self, state, action, reward, total_reward):
        self.ev3.screen.clear()
        self.ev3.screen.draw_text(0, 0, str(state))
        self.ev3.screen.draw_text(0, 16, str(action))
        self.ev3.screen.draw_text(0, 32, str(reward) + "(" + str(total_reward) + ")")
        y = 48
        for value in self.values():
            self.ev3.screen.draw_text(0, y, value)
            y += 16

SPEED = 360

def go_forward(robot):
    robot.left.run(SPEED)
    robot.right.run(SPEED)

def go_right(robot):
    robot.left.run(-SPEED)
    robot.right.run(SPEED)

def go_left(robot):
    robot.left.run(SPEED)
    robot.right.run(-SPEED)

def go_back(robot):
    robot.left.run(-SPEED)
    robot.right.run(-SPEED)

def stop(robot):
    robot.left.run(0)
    robot.right.run(0)