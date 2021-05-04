#!/usr/bin/env python
import math
import rospy
from turtlesim.msg import Pose


class TurtlePosition:
    def __init__(self):
        rospy.init_node('ros_turtle_game', anonymous = True)
        self.get_pose = rospy.Subscriber('/turtle1/pose', Pose, self.get_current_position)
        self.pose = Pose()
        
    def get_current_position(self, position):
        self.pose = position
        self.pose.x = round(self.pose.x,2)
        self.pose.y = round(self.pose.y,2)

    def get_pose_x(self):
        return self.pose.x
        
    def get_pose_y(self):
        return self.pose.y
    
    def calc_distance(self, current_x, current_y, goal_x, goal_y):
        return math.sqrt(pow((goal_x-current_x),2)+pow((goal_y-current_y),2))
