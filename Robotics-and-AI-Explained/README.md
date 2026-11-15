# Code examples — Robotics & AI Explained

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
| appendix_A_Answers_to_Review_Questions_and_Exercises | example_126.py | Searching for a valid gear ratio | desktop (runs without hardware) |
| appendix_A_Answers_to_Review_Questions_and_Exercises | example_127.py | A charge method with a maximum | desktop (runs without hardware) |
| appendix_A_Answers_to_Review_Questions_and_Exercises | example_128.py | Flagging outliers with two standard deviations | desktop (runs without hardware) |
| appendix_A_Answers_to_Review_Questions_and_Exercises | example_129.py | PID with simple anti-windup | desktop (runs without hardware) |
| appendix_A_Answers_to_Review_Questions_and_Exercises | example_130.py | Payback for different time savings | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_131.py | Variables and basic types | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_132.py | Arithmetic operators | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_133.py | Formatting text with f-strings | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_134.py | Decisions with if, elif and else | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_135.py | for and while loops | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_136.py | Working with lists | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_137.py | List comprehensions | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_138.py | Working with dictionaries | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_139.py | Defining and calling functions | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_140.py | A small robot class | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_141.py | Handling errors with try and except | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_142.py | Using standard library modules | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_143.sh | Creating a virtual environment | command / config |
| appendix_B_Python_Crash_Course | example_144.py | Writing and reading a CSV log | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_145.py | NumPy arrays and vectorized math | desktop (runs without hardware) |
| appendix_B_Python_Crash_Course | example_146.py | A simple line chart with Matplotlib | desktop (runs without hardware) |
| appendix_C_Cheat_Sheets | example_147.py | Clamp, map and moving average helpers | desktop (runs without hardware) |
| appendix_C_Cheat_Sheets | example_148.py | A steady-rate control loop | desktop (runs without hardware) |
| appendix_C_Cheat_Sheets | example_149.py | A minimal finite state machine | desktop (runs without hardware) |
| appendix_C_Cheat_Sheets | example_150.py | The scikit-learn pattern | desktop (runs without hardware) |
| appendix_D_Setup_Open_Source_Tools_and_Licenses | example_151.sh | Creating the environment (Linux and macOS) | command / config |
| appendix_D_Setup_Open_Source_Tools_and_Licenses | example_152.sh | Installing the packages used in this book | command / config |
| appendix_D_Setup_Open_Source_Tools_and_Licenses | example_153.sh | Running an example | command / config |
| appendix_F_Capstone_Projects | example_154.py | Capstone 1: a line-following robot | desktop (runs without hardware) |
| appendix_F_Capstone_Projects | example_155.py | Capstone 2: a warehouse delivery robot | desktop (runs without hardware) |
| appendix_F_Capstone_Projects | example_156.py | Capstone 3: training a quality inspector | desktop (runs without hardware) |
| appendix_F_Capstone_Projects | example_157.py | Capstone 4: odometry plus landmarks with a Kalman filter | desktop (runs without hardware) |
| appendix_F_Capstone_Projects | example_158.py | Capstone 5: a safe command interface | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_159.py | Degrees versus radians | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_160.py | Wrapping angles to the range -180..180 degrees | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_161.py | A unit mistake in a speed calculation | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_162.py | Comparing floating-point numbers | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_163.py | The missing time step | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_164.py | Removing invalid readings safely | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_165.py | The mutable default argument trap | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_166.py | Overflow in a small integer type | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_167.py | Scaling after the split | desktop (runs without hardware) |
| appendix_G_Debugging_Guide_Common_Mistakes_in_Robot_Code | example_168.py | Measuring how long each part of a loop takes | desktop (runs without hardware) |
| ch01_Key_Concepts | example_01.sh | Install the libraries used in this book | command / config |
| ch01_Key_Concepts | example_02.py | Hello, robot | desktop (runs without hardware) |
| ch01_Key_Concepts | example_03.py | A robot approaches a wall | desktop (runs without hardware) |
| ch01_Key_Concepts | example_04.py | A noisy distance sensor | desktop (runs without hardware) |
| ch01_Key_Concepts | example_05.py | Averaging reduces noise | desktop (runs without hardware) |
| ch01_Key_Concepts | example_06.py | A thermostat feedback loop | desktop (runs without hardware) |
| ch01_Key_Concepts | example_07.py | A simple agent looks for warmth | desktop (runs without hardware) |
| ch02_Anatomy_of_a_Robot | example_08.py | Counting degrees of freedom | desktop (runs without hardware) |
| ch02_Anatomy_of_a_Robot | example_09.py | Forward kinematics of a two-link arm | desktop (runs without hardware) |
| ch02_Anatomy_of_a_Robot | example_10.py | Plotting the reachable workspace | desktop (runs without hardware) |
| ch02_Anatomy_of_a_Robot | example_11.py | Gear ratio: speed versus torque | desktop (runs without hardware) |
| ch02_Anatomy_of_a_Robot | example_12.py | Distance from wheel encoder ticks | desktop (runs without hardware) |
| ch02_Anatomy_of_a_Robot | example_13.py | A power budget and battery runtime | desktop (runs without hardware) |
| ch02_Anatomy_of_a_Robot | example_14.py | A robot described as a Python class | desktop (runs without hardware) |
| ch03_Types_of_Robots | example_15.py | A small robot catalog | desktop (runs without hardware) |
| ch03_Types_of_Robots | example_16.py | Differential drive: from wheel speeds to motion | desktop (runs without hardware) |
| ch03_Types_of_Robots | example_17.py | Plotting a robot's path | desktop (runs without hardware) |
| ch03_Types_of_Robots | example_18.py | Comparing the cost of transport | desktop (runs without hardware) |
| ch03_Types_of_Robots | example_19.py | How much thrust does a drone need? | desktop (runs without hardware) |
| ch03_Types_of_Robots | example_20.py | Water pressure at depth | desktop (runs without hardware) |
| ch03_Types_of_Robots | example_21.py | A swarm gathers without a leader | desktop (runs without hardware) |
| ch03_Types_of_Robots | example_22.py | Choosing a robot type for a task | desktop (runs without hardware) |
| ch04_Algorithms_and_Data | example_23.py | Finding the closest obstacle | desktop (runs without hardware) |
| ch04_Algorithms_and_Data | example_24.py | Linear search versus binary search | desktop (runs without hardware) |
| ch04_Algorithms_and_Data | example_25.py | Measuring how algorithms grow | desktop (runs without hardware) |
| ch04_Algorithms_and_Data | example_26.py | A simple sorting algorithm | desktop (runs without hardware) |
| ch04_Algorithms_and_Data | example_27.py | Describing sensor data with NumPy | desktop (runs without hardware) |
| ch04_Algorithms_and_Data | example_28.py | Cleaning a messy sensor log | desktop (runs without hardware) |
| ch04_Algorithms_and_Data | example_29.py | Scaling features | desktop (runs without hardware) |
| ch04_Algorithms_and_Data | example_30.py | Splitting data into training and test sets | desktop (runs without hardware) |
| ch04_Algorithms_and_Data | example_31.py | A histogram of sensor noise | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_32.py | k-nearest neighbors from scratch | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_33.py | k-NN with scikit-learn and accuracy | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_34.py | A decision tree that explains itself | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_35.py | Linear regression: battery use per trip | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_36.py | Confusion matrix, precision and recall | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_37.py | Overfitting: complexity versus test error | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_38.py | k-means: where to place three charging stations | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_39.py | Detecting unusual motor vibration | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_40.py | Explore or exploit: three charging stations | desktop (runs without hardware) |
| ch05_Supervised_Unsupervised_and_Reinforcement_Learning | example_41.py | Q-learning: a robot learns to reach its charger | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_42.py | A perceptron decides when to stop | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_43.py | A perceptron learns AND by itself | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_44.py | A single perceptron fails on XOR | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_45.py | Common activation functions | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_46.py | Gradient descent in one dimension | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_47.py | A two-layer network learns XOR from scratch | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_48.py | Looking at the digits dataset | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_49.py | A neural network reads handwritten digits | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_50.py | Plotting the learning curve | desktop (runs without hardware) |
| ch06_Neural_Networks_Step_by_Step | example_51.py | A convolution filter detects edges | desktop (runs without hardware) |
| ch07_Generative_AI | example_52.py | A tiny text generator from word pairs | desktop (runs without hardware) |
| ch07_Generative_AI | example_53.py | Next-word probabilities | desktop (runs without hardware) |
| ch07_Generative_AI | example_54.py | How temperature changes the choices | desktop (runs without hardware) |
| ch07_Generative_AI | example_55.py | Comparing sentences with word vectors | desktop (runs without hardware) |
| ch07_Generative_AI | example_56.py | Finding the right manual entry | desktop (runs without hardware) |
| ch07_Generative_AI | example_57.py | Generating synthetic robot stop positions | desktop (runs without hardware) |
| ch07_Generative_AI | example_58.py | From words to a checked robot plan | desktop (runs without hardware) |
| ch08_Sensors_in_Depth | example_59.py | Bias and noise in two sensors | desktop (runs without hardware) |
| ch08_Sensors_in_Depth | example_60.py | From echo time to distance | desktop (runs without hardware) |
| ch08_Sensors_in_Depth | example_61.py | Turning a lidar scan into points | desktop (runs without hardware) |
| ch08_Sensors_in_Depth | example_62.py | Estimating tilt from gravity | desktop (runs without hardware) |
| ch08_Sensors_in_Depth | example_63.py | A gyroscope drifts over time | desktop (runs without hardware) |
| ch08_Sensors_in_Depth | example_64.py | Fusing gyroscope and accelerometer | desktop (runs without hardware) |
| ch08_Sensors_in_Depth | example_65.py | Moving average versus median filter | desktop (runs without hardware) |
| ch08_Sensors_in_Depth | example_66.py | A one-dimensional Kalman filter | desktop (runs without hardware) |
| ch08_Sensors_in_Depth | example_67.py | Aliasing: sampling too slowly | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_68.py | Building a tiny color image | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_69.py | Converting to grayscale | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_70.py | Finding a red object and its center | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_71.py | Counting separate objects in a mask | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_72.py | Sobel edge detection | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_73.py | Distance from apparent size | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_74.py | Depth from stereo disparity | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_75.py | Intersection over union for bounding boxes | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_76.py | Removing duplicate detections | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_77.py | Creating and measuring a sound wave | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_78.py | Which frequency is this alarm? | desktop (runs without hardware) |
| ch09_Vision_and_Sound | example_79.py | Locating a sound with two microphones | desktop (runs without hardware) |
| ch10_Actuators_and_Control | example_80.py | Duty cycle and average voltage | desktop (runs without hardware) |
| ch10_Actuators_and_Control | example_81.py | A motor speeds up step by step | desktop (runs without hardware) |
| ch10_Actuators_and_Control | example_82.py | Open loop versus closed loop under load | desktop (runs without hardware) |
| ch10_Actuators_and_Control | example_83.py | A PID controller for motor speed | desktop (runs without hardware) |
| ch10_Actuators_and_Control | example_84.py | Comparing P, PI and PID responses | desktop (runs without hardware) |
| ch10_Actuators_and_Control | example_85.py | A position controller moves a joint | desktop (runs without hardware) |
| ch10_Actuators_and_Control | example_86.py | Inverse kinematics of a two-link arm | desktop (runs without hardware) |
| ch10_Actuators_and_Control | example_87.py | Linear versus smooth trajectories | desktop (runs without hardware) |
| ch11_Navigation | example_88.py | An occupancy grid map | desktop (runs without hardware) |
| ch11_Navigation | example_89.py | Odometry errors grow over time | desktop (runs without hardware) |
| ch11_Navigation | example_90.py | A particle filter finds the robot in a corridor | desktop (runs without hardware) |
| ch11_Navigation | example_91.py | Breadth-first search on a grid | desktop (runs without hardware) |
| ch11_Navigation | example_92.py | A* path planning with a map plot | desktop (runs without hardware) |
| ch11_Navigation | example_93.py | Avoiding an obstacle with a potential field | desktop (runs without hardware) |
| ch11_Navigation | example_94.py | Building a map from simulated range readings | desktop (runs without hardware) |
| ch12_Robot_Software_and_Operating_Systems | example_95.py | A loop that keeps a steady rate | desktop (runs without hardware) |
| ch12_Robot_Software_and_Operating_Systems | example_96.py | A tiny publish-subscribe system | desktop (runs without hardware) |
| ch12_Robot_Software_and_Operating_Systems | example_97.py | Defining message types with data classes | desktop (runs without hardware) |
| ch12_Robot_Software_and_Operating_Systems | example_98.py | A finite state machine for a delivery robot | desktop (runs without hardware) |
| ch12_Robot_Software_and_Operating_Systems | example_99.py | A small behavior tree | desktop (runs without hardware) |
| ch12_Robot_Software_and_Operating_Systems | example_100.py | A minimal ROS 2 publisher node (requires ROS 2) | hardware / ROS 2 |
| ch12_Robot_Software_and_Operating_Systems | example_101.py | Logging what the robot does | desktop (runs without hardware) |
| ch13_Human_Robot_Interaction | example_102.py | Speed limits based on personal space | desktop (runs without hardware) |
| ch13_Human_Robot_Interaction | example_103.py | Choosing status lights from the robot's state | desktop (runs without hardware) |
| ch13_Human_Robot_Interaction | example_104.py | Matching spoken commands to intents | desktop (runs without hardware) |
| ch13_Human_Robot_Interaction | example_105.py | Classifying simple arm gestures | desktop (runs without hardware) |
| ch13_Human_Robot_Interaction | example_106.py | Calculating a System Usability Scale score | desktop (runs without hardware) |
| ch13_Human_Robot_Interaction | example_107.py | A simple model of trust over time | desktop (runs without hardware) |
| ch14_Safety_and_Standards | example_108.py | Scoring risks with a risk matrix | desktop (runs without hardware) |
| ch14_Safety_and_Standards | example_109.py | Stopping distance of a mobile robot | desktop (runs without hardware) |
| ch14_Safety_and_Standards | example_110.py | Minimum separation distance | desktop (runs without hardware) |
| ch14_Safety_and_Standards | example_111.py | A software watchdog | desktop (runs without hardware) |
| ch14_Safety_and_Standards | example_112.py | Two-out-of-three voting | desktop (runs without hardware) |
| ch14_Safety_and_Standards | example_113.py | Checking a virtual safety zone | desktop (runs without hardware) |
| ch15_Industry_Tour | example_114.py | Analyzing robot installation figures | desktop (runs without hardware) |
| ch15_Industry_Tour | example_115.py | Robot density by country | desktop (runs without hardware) |
| ch15_Industry_Tour | example_116.py | Measuring overall equipment effectiveness | desktop (runs without hardware) |
| ch15_Industry_Tour | example_117.py | How many robots does a warehouse need? | desktop (runs without hardware) |
| ch15_Industry_Tour | example_118.py | Herbicide savings with targeted spraying | desktop (runs without hardware) |
| ch15_Industry_Tour | example_119.py | A simple payback calculation | desktop (runs without hardware) |
| ch16_Careers_in_Robotics_and_AI | example_120.py | Finding your skill gaps | desktop (runs without hardware) |
| ch16_Careers_in_Robotics_and_AI | example_121.py | Which role fits my profile best? | desktop (runs without hardware) |
| ch16_Careers_in_Robotics_and_AI | example_122.py | Counting skills in job advertisements | desktop (runs without hardware) |
| ch17_Your_Learning_Roadmap | example_123.py | Choosing your next project | desktop (runs without hardware) |
| ch17_Your_Learning_Roadmap | example_124.py | Scheduling spaced reviews | desktop (runs without hardware) |
| ch17_Your_Learning_Roadmap | example_125.py | A weekly study planner | desktop (runs without hardware) |
