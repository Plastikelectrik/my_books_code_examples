# Code examples — Build Smart Robots

Every numbered example from the book, organized by chapter.
Each file is named after its number in the book (Example 01 -> example_01.*).

## How to use

1. Create and activate a Python virtual environment (see Appendix A).
2. Install the libraries: `pip install numpy matplotlib opencv-python scikit-learn pyserial pytest flask pybullet joblib`.
3. Run desktop examples with `python3 example_NN.py` from inside their chapter folder.
4. Arduino examples (`.ino`): open them in the Arduino IDE (each sketch must be inside a folder with the same name; the IDE offers to create it).
5. MicroPython examples: copy them to the ESP32 with Thonny and save them as `main.py` to run at startup.
6. ROS 2 examples: place them in a ROS 2 package as described in the book.

## Files that other examples import

Some later examples import earlier ones by module name. Those files are included a second time under the required name (for example `rover.py`). Keep them in the same folder as the program that imports them.

## Safety and license

Examples are provided as is, without warranty, for learning. Read the safety notes in the book before running anything that moves hardware. The code is released under the MIT License (see the LICENSE file in the root of this repository). Third-party libraries keep their own licenses (see the appendix on third-party software).

## List of examples

| Folder | File | Title | Type |
|---|---|---|---|
| appendix_A_Installation_and_Setup_Guide | example_135.sh | Create and activate a virtual environment | command / config |
| appendix_A_Installation_and_Setup_Guide | example_136.sh | Install all Python libraries used in the book | command / config |
| appendix_A_Installation_and_Setup_Guide | example_137.sh | Log in to the Raspberry Pi over the network | command / config |
| appendix_A_Installation_and_Setup_Guide | example_138.sh | First steps on the Raspberry Pi | command / config |
| appendix_A_Installation_and_Setup_Guide | example_139.py | Check that the main libraries are installed | desktop (runs without hardware) |
| appendix_D_Solutions_to_Selected_Exercises | example_140.py | Solution: speed depends on the distance | desktop (runs without hardware) |
| appendix_D_Solutions_to_Selected_Exercises | example_141.py | Solution: obstacle avoidance with three rays | desktop (runs without hardware) |
| appendix_D_Solutions_to_Selected_Exercises | example_142.py | Solution: a reward that penalizes hard steering | desktop (runs without hardware) |
| appendix_D_Solutions_to_Selected_Exercises | example_143.py | Solution: waypoints plus a final heading | desktop (runs without hardware) |
| appendix_D_Solutions_to_Selected_Exercises | example_144.py | Solution: core of the safety_stop node | desktop (runs without hardware) |
| appendix_D_Solutions_to_Selected_Exercises | example_145.sh | Remap the teleop output topic | command / config |
| ch01_Your_Robotics_Toolkit | example_01.sh | Check the Python version | command / config |
| ch01_Your_Robotics_Toolkit | example_02.sh | Create the project and its virtual environment | command / config |
| ch01_Your_Robotics_Toolkit | example_03.sh | Activate the environment on Windows | command / config |
| ch01_Your_Robotics_Toolkit | example_04.sh | Install the libraries used in the first chapters | command / config |
| ch01_Your_Robotics_Toolkit | example_05.py | The sense-think-act loop in its simplest form | desktop (runs without hardware) |
| ch01_Your_Robotics_Toolkit | example_06.sh | Run your first robot program | command / config |
| ch01_Your_Robotics_Toolkit | example_07.sh | Start tracking your project with Git | command / config |
| ch02_Python_for_Robotics | example_08.py | Units in names make bugs visible | desktop (runs without hardware) |
| ch02_Python_for_Robotics | example_09.py | Cleaning a lidar scan with NumPy | desktop (runs without hardware) |
| ch02_Python_for_Robotics | example_10.py | A simple robot class with a pose | desktop (runs without hardware) |
| ch02_Python_for_Robotics | example_11.py | A loop that runs at a steady rate | desktop (runs without hardware) |
| ch02_Python_for_Robotics | example_12.py | A state machine for obstacle avoidance | desktop (runs without hardware) |
| ch02_Python_for_Robotics | example_13.py | Plot the path of a robot driving in a circle | desktop (runs without hardware) |
| ch02_Python_for_Robotics | example_14.py | A tiny 2D simulator with a distance sensor | desktop (runs without hardware) |
| ch03_Hardware_Basics | example_15.ino | Blink and talk: the Arduino "hello world" | Arduino board |
| ch03_Hardware_Basics | example_16.py | Blink on an ESP32 with MicroPython | hardware / ROS 2 |
| ch03_Hardware_Basics | example_17.ino | Drive two motors forward, backward and turn | Arduino board |
| ch03_Hardware_Basics | example_18.ino | Sweep a servo between 0 and 180 degrees | Arduino board |
| ch03_Hardware_Basics | example_19.ino | Arduino side: receive motor commands | Arduino board |
| ch03_Hardware_Basics | example_20.py | Raspberry Pi side: send motor commands over USB | hardware / ROS 2 |
| ch04_Building_Rover_Step_by_Step | example_21.ino | Rover's complete Arduino firmware | Arduino board |
| ch04_Building_Rover_Step_by_Step | example_22.py (also `rover.py`) | rover.py: a Python driver for Rover's firmware | hardware / ROS 2 |
| ch04_Building_Rover_Step_by_Step | example_23.py | Drive until an obstacle appears | hardware / ROS 2 |
| ch04_Building_Rover_Step_by_Step | example_24.py | Calculate meters per tick from a test drive | desktop (runs without hardware) |
| ch05_Reading_Sensors | example_25.ino | Read an ultrasonic distance sensor | Arduino board |
| ch05_Reading_Sensors | example_26.ino | Count encoder ticks with interrupts | Arduino board |
| ch05_Reading_Sensors | example_27.py | Convert encoder ticks into distance and speed | desktop (runs without hardware) |
| ch05_Reading_Sensors | example_28.py | Read the gyroscope on an ESP32 (MicroPython) | hardware / ROS 2 |
| ch05_Reading_Sensors | example_29.py | Simulate a noisy sensor with outliers | desktop (runs without hardware) |
| ch05_Reading_Sensors | example_30.py | Compare four filters on the same noisy data | desktop (runs without hardware) |
| ch05_Reading_Sensors | example_31.py | A complementary filter beats both sensors alone | desktop (runs without hardware) |
| ch05_Reading_Sensors | example_32.py | Record sensor lines from the Arduino to CSV | hardware / ROS 2 |
| ch06_Computer_Vision_with_OpenCV | example_33.py | An image is just a NumPy array | desktop (runs without hardware) |
| ch06_Computer_Vision_with_OpenCV | example_34.py | Capture frames from a USB camera | hardware / ROS 2 |
| ch06_Computer_Vision_with_OpenCV | example_35.py | Capture frames from a Raspberry Pi camera module | hardware / ROS 2 |
| ch06_Computer_Vision_with_OpenCV | example_36.py | Find an orange ball by color | desktop (runs without hardware) |
| ch06_Computer_Vision_with_OpenCV | example_37.py | Clean a noisy mask with opening and closing | desktop (runs without hardware) |
| ch06_Computer_Vision_with_OpenCV | example_38.py | Turn the ball position into motor commands | desktop (runs without hardware) |
| ch06_Computer_Vision_with_OpenCV | example_39.py | Find a dark line and compute the steering error | desktop (runs without hardware) |
| ch06_Computer_Vision_with_OpenCV | example_40.py | Estimate distance from apparent size | desktop (runs without hardware) |
| ch06_Computer_Vision_with_OpenCV | example_41.py | Complete ball-following loop on the Raspberry Pi | hardware / ROS 2 |
| ch07_Object_Detection | example_42.py | Generate printable ArUco markers | desktop (runs without hardware) |
| ch07_Object_Detection | example_43.py | Detect an ArUco marker in a tilted view | desktop (runs without hardware) |
| ch07_Object_Detection | example_44.py | Estimate distance and angle to a marker | desktop (runs without hardware) |
| ch07_Object_Detection | example_45.py | Train a shape classifier with scikit-learn | desktop (runs without hardware) |
| ch07_Object_Detection | example_46.py | The shape of a detection pipeline (pseudo-model) | desktop (runs without hardware) |
| ch08_Control_Loops_and_PID | example_47.py | A simple motor model with inertia and friction | desktop (runs without hardware) |
| ch08_Control_Loops_and_PID | example_48.py | Proportional control of motor speed | desktop (runs without hardware) |
| ch08_Control_Loops_and_PID | example_49.py (also `pid.py`) | A reusable PID controller with anti-windup | desktop (runs without hardware) |
| ch08_Control_Loops_and_PID | example_50.py | Compare P, PI and PID on a motor with a load step | desktop (runs without hardware) |
| ch08_Control_Loops_and_PID | example_51.ino | Wheel speed PI control with encoders (Arduino) | Arduino board |
| ch08_Control_Loops_and_PID | example_52.py | Wall following with PID in the 2D simulator | desktop (runs without hardware) |
| ch09_Machine_Learning_for_Robots | example_53.py | Generate vibration data for three surfaces | desktop (runs without hardware) |
| ch09_Machine_Learning_for_Robots | example_54.py (also `features.py`) | Extract features from one-second windows | desktop (runs without hardware) |
| ch09_Machine_Learning_for_Robots | example_55.py | Compare two classifiers with cross-validation | desktop (runs without hardware) |
| ch09_Machine_Learning_for_Robots | example_56.py | Confusion matrix with a harder fourth class | desktop (runs without hardware) |
| ch09_Machine_Learning_for_Robots | example_57.py | Detect abnormal motor behavior with Isolation Forest | desktop (runs without hardware) |
| ch09_Machine_Learning_for_Robots | example_58.py | Detect collisions from sudden acceleration changes | desktop (runs without hardware) |
| ch09_Machine_Learning_for_Robots | example_59.py | Train, save and reload a model for the robot | desktop (runs without hardware) |
| ch10_Reinforcement_Learning_Basics | example_60.py | Q-learning in a grid world | desktop (runs without hardware) |
| ch10_Reinforcement_Learning_Basics | example_61.py | Q-learning to follow a curving line | desktop (runs without hardware) |
| ch10_Reinforcement_Learning_Basics | example_62.py | Use a learned Q-table to steer Rover | hardware / ROS 2 |
| ch11_Kinematics_Made_Simple | example_63.py | Differential-drive kinematics in both directions | desktop (runs without hardware) |
| ch11_Kinematics_Made_Simple | example_64.py (also `odometry.py`) | Odometry from encoder ticks | desktop (runs without hardware) |
| ch11_Kinematics_Made_Simple | example_65.py | Live odometry on Rover | hardware / ROS 2 |
| ch11_Kinematics_Made_Simple | example_66.py | Correct the wheelbase from a rotation test | desktop (runs without hardware) |
| ch11_Kinematics_Made_Simple | example_67.py | A go-to-goal controller in simulation | desktop (runs without hardware) |
| ch11_Kinematics_Made_Simple | example_68.py | Forward and inverse kinematics of a 2-link arm | desktop (runs without hardware) |
| ch12_Path_Planning | example_69.py | Build an occupancy grid for a room | desktop (runs without hardware) |
| ch12_Path_Planning | example_70.py (also `astar.py`) | A* path planning on an occupancy grid | desktop (runs without hardware) |
| ch12_Path_Planning | example_71.py | Inflate obstacles by the robot's radius | desktop (runs without hardware) |
| ch12_Path_Planning | example_72.py | Shortcut smoothing with line-of-sight checks | desktop (runs without hardware) |
| ch12_Path_Planning | example_73.py | RRT in a 2D room with circular obstacles | desktop (runs without hardware) |
| ch12_Path_Planning | example_74.py | Pure pursuit following a waypoint path | desktop (runs without hardware) |
| ch13_SLAM_and_Localization | example_75.py | A 1D particle filter: where in the corridor am I? | desktop (runs without hardware) |
| ch13_SLAM_and_Localization | example_76.py | A 2D particle filter with range-bearing landmarks | desktop (runs without hardware) |
| ch13_SLAM_and_Localization | example_77.py | Build an occupancy grid from simulated lidar scans | desktop (runs without hardware) |
| ch14_Building_and_Controlling_a_Robot_Arm | example_78.py | Servo arm firmware for ESP32 (MicroPython) | hardware / ROS 2 |
| ch14_Building_and_Controlling_a_Robot_Arm | example_79.py | 3D inverse kinematics for a 3-joint arm | desktop (runs without hardware) |
| ch14_Building_and_Controlling_a_Robot_Arm | example_80.py | Minimum-jerk interpolation between two poses | desktop (runs without hardware) |
| ch14_Building_and_Controlling_a_Robot_Arm | example_81.py | Execute a smooth move on the real arm | hardware / ROS 2 |
| ch14_Building_and_Controlling_a_Robot_Arm | example_82.py | Convert pixels to table coordinates | desktop (runs without hardware) |
| ch15_Wireless_Control_and_Telemetry | example_83.py | ESP32: connect to Wi-Fi and send UDP telemetry | hardware / ROS 2 |
| ch15_Wireless_Control_and_Telemetry | example_84.py | secrets.py on the ESP32 (never publish this file) | desktop (runs without hardware) |
| ch15_Wireless_Control_and_Telemetry | example_85.py | Send and receive UDP telemetry (self-test) | desktop (runs without hardware) |
| ch15_Wireless_Control_and_Telemetry | example_86.py (also `dashboard.py`) | dashboard.py: a Flask web dashboard for Rover | desktop (runs without hardware) |
| ch15_Wireless_Control_and_Telemetry | example_87.sh | Start the dashboard with your own token | command / config |
| ch15_Wireless_Control_and_Telemetry | example_88.py | Control loop with command timeout (add to dashboard.py) | hardware / ROS 2 |
| ch15_Wireless_Control_and_Telemetry | example_89.py | Test the dashboard API with Flask's test client | desktop (runs without hardware) |
| ch16_ROS_2_Fundamentals | example_90.sh | Install ROS 2 (summary, see the official guide) | command / config |
| ch16_ROS_2_Fundamentals | example_91.sh | Test the installation with two demo nodes | command / config |
| ch16_ROS_2_Fundamentals | example_92.sh | Essential ROS 2 command-line tools | command / config |
| ch16_ROS_2_Fundamentals | example_93.py | A minimal publisher node | hardware / ROS 2 |
| ch16_ROS_2_Fundamentals | example_94.py | A minimal subscriber node | hardware / ROS 2 |
| ch16_ROS_2_Fundamentals | example_95.sh | Create a workspace and a Python package | command / config |
| ch16_ROS_2_Fundamentals | example_96.py | Register nodes in setup.py (excerpt) | desktop (runs without hardware) |
| ch16_ROS_2_Fundamentals | example_97.sh | Build the workspace and run a node | command / config |
| ch16_ROS_2_Fundamentals | example_98.py (also `bridge.py`) | bridge.py: connect Rover to ROS 2 | hardware / ROS 2 |
| ch16_ROS_2_Fundamentals | example_99.sh | Drive Rover with the keyboard through ROS 2 | command / config |
| ch16_ROS_2_Fundamentals | example_100.py | rover.launch.py: start the bridge with parameters | hardware / ROS 2 |
| ch16_ROS_2_Fundamentals | example_101.sh | Record and replay Rover's topics | command / config |
| ch17_Simulation_with_Gazebo_and_PyBullet | example_102.xml | rover.urdf: a simple description of Rover | command / config |
| ch17_Simulation_with_Gazebo_and_PyBullet | example_103.py | Drive Rover to a goal in PyBullet | desktop (runs without hardware) |
| ch17_Simulation_with_Gazebo_and_PyBullet | example_104.py | Inverse kinematics for a 7-joint arm in PyBullet | desktop (runs without hardware) |
| ch17_Simulation_with_Gazebo_and_PyBullet | example_105.py | Test the controller with randomized physics | desktop (runs without hardware) |
| ch17_Simulation_with_Gazebo_and_PyBullet | example_106.sh | Install and test Gazebo with ROS 2 (Lyrical) | command / config |
| ch17_Simulation_with_Gazebo_and_PyBullet | example_107.sh | Bridge Gazebo and ROS 2 topics | command / config |
| ch18_Capstone_An_Autonomous_Delivery_Robot | example_108.py (also `delivery_sim.py`) | The complete delivery robot in simulation | desktop (runs without hardware) |
| ch18_Capstone_An_Autonomous_Delivery_Robot | example_109.py | Real Rover: plan, follow and replan (main loop) | hardware / ROS 2 |
| ch18_Capstone_An_Autonomous_Delivery_Robot | example_110.py | Final docking approach using an ArUco marker | desktop (runs without hardware) |
| ch19_Safety_Testing_and_Next_Steps | example_111.py | test_rover.py: automatic tests with pytest | desktop (runs without hardware) |
| ch19_Safety_Testing_and_Next_Steps | example_112.sh | Run all tests in the current folder | command / config |
| ch19_Safety_Testing_and_Next_Steps | example_113.py | Professional logging with rotating log files | desktop (runs without hardware) |
| ch20_Bonus_Project_Voice_Commands_for_Rover | example_114.sh | Install Vosk and an audio library | command / config |
| ch20_Bonus_Project_Voice_Commands_for_Rover | example_115.py | Recognize Rover commands with Vosk (live microphone) | hardware / ROS 2 |
| ch20_Bonus_Project_Voice_Commands_for_Rover | example_116.py (also `voice_parser.py`) | A command parser with speed levels and safe defaults | desktop (runs without hardware) |
| ch20_Bonus_Project_Voice_Commands_for_Rover | example_117.py (also `voice_executor.py`) | Execute parsed commands with timeouts (simulated) | desktop (runs without hardware) |
| ch20_Bonus_Project_Voice_Commands_for_Rover | example_118.py | Voice-controlled Rover (main program) | hardware / ROS 2 |
| ch21_Bonus_Project_Neural_Networks_on_the_Robot | example_119.py | Load the digits dataset and look at one example | desktop (runs without hardware) |
| ch21_Bonus_Project_Neural_Networks_on_the_Robot | example_120.py | A two-layer neural network written with NumPy only | desktop (runs without hardware) |
| ch21_Bonus_Project_Neural_Networks_on_the_Robot | example_121.py | Train the same kind of network with scikit-learn | desktop (runs without hardware) |
| ch21_Bonus_Project_Neural_Networks_on_the_Robot | example_122.py | Measure inference time of the NumPy network | desktop (runs without hardware) |
| ch21_Bonus_Project_Neural_Networks_on_the_Robot | example_123.py | Convert a camera crop into the 8 x 8 digit format | desktop (runs without hardware) |
| ch22_Bonus_Project_A_Walking_Robot_with_Otto_DIY | example_124.py | Compute an oscillator gait for a four-servo biped | desktop (runs without hardware) |
| ch22_Bonus_Project_A_Walking_Robot_with_Otto_DIY | example_125.py | Variations: backward walking and turning | desktop (runs without hardware) |
| ch22_Bonus_Project_A_Walking_Robot_with_Otto_DIY | example_126.ino | Oscillator walking gait for a four-servo biped | Arduino board |
| ch23_Bonus_Project_A_Competition_Line_Follower_and_Maze | example_127.py | Line following with a sensor array and PD control | desktop (runs without hardware) |
| ch23_Bonus_Project_A_Competition_Line_Follower_and_Maze | example_128.ino | Calibrate and read a five-sensor reflectance array | Arduino board |
| ch23_Bonus_Project_A_Competition_Line_Follower_and_Maze | example_129.py | Left-hand and right-hand rules with path simplification | desktop (runs without hardware) |
| ch24_Bonus_Project_Two_Robots_One_Corridor | example_130.py | Prioritized space-time planning for two robots | desktop (runs without hardware) |
| ch24_Bonus_Project_Two_Robots_One_Corridor | example_131.py | Launch two robots with namespaces (ROS 2) | hardware / ROS 2 |
| ch25_Bonus_Project_Live_Video_and_Telepresence | example_132.py | Encode frames as MJPEG parts and measure bandwidth | desktop (runs without hardware) |
| ch25_Bonus_Project_Live_Video_and_Telepresence | example_133.py | Stream the robot camera to a browser (Flask) | hardware / ROS 2 |
| ch25_Bonus_Project_Live_Video_and_Telepresence | example_134.py | Record frames with telemetry to a video file | desktop (runs without hardware) |
