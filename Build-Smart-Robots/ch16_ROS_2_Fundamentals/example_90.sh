# 1. Enable the Ubuntu "universe" repository
sudo apt install software-properties-common
sudo add-apt-repository universe
# 2. Add the ROS 2 apt source (follow the official
#    guide: it uses the ros2-apt-source package)
# 3. Install ROS 2 desktop and developer tools
sudo apt update
sudo apt install ros-lyrical-desktop ros-dev-tools
# 4. Load ROS 2 in every new terminal
echo "source /opt/ros/lyrical/setup.bash" >> ~/.bashrc
source ~/.bashrc
