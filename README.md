# niosr_project
- [x] pobranie linux
- [x] konfiguracja ROS
- [x] usb_cam
- [x] detekcja kodu na przykladowym obrazku -- 18.12.2023
- [x] obsluga detekcji obszaru obrazka w jakim znajduje się kod -- 19.12.2023
- [x] obsługa pliku video
- [x] implementacja pod środowisko ROS i testy

# Requirements:

install ros2:

https://docs.ros.org/en/crystal/Installation/Linux-Install-Binary.html

install turtlebot3 package:

sudo apt install ros-humble-turtlebot3*

install usb_cam package:

cd ~/ros2_ws/src
git clone --branch ros2 https://github.com/ros-drivers/usb_cam.git
cd ..
rosdep install --from-paths src -y --ignore-src --rosdistro humble

Po każdym pobraniu paczki w katalogu ~/ros2_ws:

colcon build
source install/setup.bash

# Tutorial odpalenia:
Terminal 1 (uruchomienie węzła kamery):
cd ~/ros2_ws 
source install/setup.bash
ros2 run usb_cam usb_cam_node_exe

Terminal 2 (uruchomienie robota i środowiska symulacyjnego):
cd ~/ros2_ws 
source install/setup.bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:`ros2 pkg \
prefix turtlebot3_gazebo \
`/share/turtlebot3_gazebo/models/
ros2 launch turtlebot3_gazebo empty_world.launch.py

Terminal 3 (uruchomienie węzła do detekcji znaczników i sterowania robotem):
cd ~/ros2_ws 
source install/setup.bash
ros2 run aruco aruco_detect

