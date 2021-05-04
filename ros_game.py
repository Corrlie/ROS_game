from Player import PlayerPoint
from Turtle import TurtlePosition
from NodeMgmt import *
import time


def calc_to_turtle_plane(raw_x, raw_y):
    rescaled_x = raw_x/46
    rescaled_y = raw_y/46
    return rescaled_x, rescaled_y

player1 = PlayerPoint()
print('Choose position of a goal point')
(raw_goal_x1, raw_goal_y1) = player1.get_coords()

(scaled_goal_x1, scaled_goal_y1) = calc_to_turtle_plane(raw_goal_x1, raw_goal_y1)

turtle1 = TurtlePosition()

process_window = run_node('turtlesim', 'turtlesim_node')
process_teleop = run_node('turtlesim', 'turtle_teleop_key')
start_timer = time.time()
print('Timer started!')
distance_state = 'Distance unknown'
new_distance_state = 'Distance unknown'
while(1):
    distance = turtle1.calc_distance(turtle1.get_pose_x(), turtle1.get_pose_y(), scaled_goal_x1, scaled_goal_y1)
    if (distance>8):
        distance_state = 'REALLY COLD!'
    elif(distance<=8 and distance > 4):
        distance_state = 'cold'
    elif(distance<=4 and distance>2):
        distance_state='warm'
    elif(distance<=2 and distance>0.2):
        distance_state = 'HOT'
    else:
        distance_state = 'POINT FOUND'
        print('CONGRATS! YOU FOUND THE POINT')
        break
    if(new_distance_state != distance_state):
        print(distance_state)
        new_distance_state = distance_state
    
finish_timer = time.time()
goal_time = round(finish_timer - start_timer, 2)
print('==============================')
print('==============================')
print('----------Your time: ---------')
print(f'---------{goal_time} s...')
print('==============================')
print('===========EXITING============')
print('==============================')
print('=============GG===============')
print('==============================')
print('=======THX FOR THE GAME=======')
print('==============================')
print('==============================')
