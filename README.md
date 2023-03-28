# Inclass-week5
# Our project is based on turtlebot arm cortex to use it for picking and droping objects in  our house hold.
- The project is based on developing a robotic arm using Turtlebot arm cortex that can pick and drop objects using the Robot Operating System (ROS) framework. The code provided is a Python implementation of this project.
- The robotic arm can perform two actions: picking and dropping. These actions are triggered through ROS services. Once the service is called, the robotic arm plans a motion using MoveIt, which is a ROS package for motion planning, and executes the motion to pick or drop the object.
- The project involves the use of several ROS packages, including MoveIt and the Actionlib package, which provides a simple way to define and use action servers and clients.
- The code includes a simple implementation of a pick and drop motion using pre-defined poses. These poses are defined with respect to the base link of the robot, which is the reference frame of the robot. The code uses inverse kinematics to compute the joint angles for the desired pose, which is then used to plan and execute the motion.

# In the given python code:
- In this code, the TurtlebotArm class initializes the MoveIt package for the arm and defines the pick and drop poses. The pick_object() and drop_object() methods move the arm to the respective poses using MoveIt.

- The handle_pick_drop_object method defines the service callback function, which sends an action goal to the action server and waits for the result. The action goal includes the name of the object and the pick/drop action. The service response is based on the result of the action server.
