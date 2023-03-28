#!/usr/bin/env python

import rospy
import actionlib
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander
from my_robot_msgs.srv import PickDropObject, PickDropObjectResponse

class TurtlebotArm:
    def __init__(self):
        rospy.init_node('turtlebot_arm')

        # Initialize MoveIt
        self.move_group = MoveGroupCommander('arm')

        # Define Pick and Drop poses
        self.pick_pose = PoseStamped()
        self.pick_pose.header.frame_id = "base_link"
        self.pick_pose.pose.position.x = 0.5
        self.pick_pose.pose.position.y = 0.0
        self.pick_pose.pose.position.z = 0.5
        self.pick_pose.pose.orientation.x = 0.0
        self.pick_pose.pose.orientation.y = 0.0
        self.pick_pose.pose.orientation.z = 0.0
        self.pick_pose.pose.orientation.w = 1.0

        self.drop_pose = PoseStamped()
        self.drop_pose.header.frame_id = "base_link"
        self.drop_pose.pose.position.x = -0.5
        self.drop_pose.pose.position.y = 0.0
        self.drop_pose.pose.position.z = 0.5
        self.drop_pose.pose.orientation.x = 0.0
        self.drop_pose.pose.orientation.y = 0.0
        self.drop_pose.pose.orientation.z = 0.0
        self.drop_pose.pose.orientation.w = 1.0

        # Define the Action client
        self.pick_drop_client = actionlib.SimpleActionClient('pick_drop', my_robot_msgs.msg.PickDropAction)

        # Define the Service client
        self.pick_drop_service = rospy.Service('pick_drop', PickDropObject, self.handle_pick_drop_object)

    def pick_object(self):
        # Move to Pick pose
        self.move_group.set_pose_target(self.pick_pose)
        plan = self.move_group.plan()
        self.move_group.execute(plan)

    def drop_object(self):
        # Move to Drop pose
        self.move_group.set_pose_target(self.drop_pose)
        plan = self.move_group.plan()
        self.move_group.execute(plan)

    def handle_pick_drop_object(self, req):
        # Define the action goal
        goal = my_robot_msgs.msg.PickDropGoal()
        goal.object_name = req.object_name
        goal.pick = req.pick

        # Send the action goal to the server and wait for the result
        self.pick_drop_client.wait_for_server()
        self.pick_drop_client.send_goal(goal)
        self.pick_drop_client.wait_for_result()

        # Get the result from the action server
        result = self.pick_drop_client.get_result()

        # Return the result of the action as a service response
        return PickDropObjectResponse(result.success)

if __name__ == '__main__':
    arm = TurtlebotArm()
    arm.pick_object()
    arm.drop_object()
