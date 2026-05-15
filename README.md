# oryxbot 仿真工作区

带机械臂小车的 Gazebo 仿真，支持 gmapping 建图、导航和写马字。

## 1. 依赖与编译

```bash
# 安装依赖
sudo apt install ros-noetic-gmapping \
  ros-noetic-teleop-twist-keyboard \
  ros-noetic-navigation \
  ros-noetic-teb-local-planner -y

# 编译
cd ~/oryxbot_sim_ws
source /opt/ros/noetic/setup.bash
catkin_make
```

## 2. 建图

```bash
source devel/setup.bash
roslaunch oryxbot_description slam.launch
```

另开终端遥控小车建图：

```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

## 3. 保存地图

```bash
roslaunch oryxbot_description map_save.launch map_name:=four_walls
```

地图保存在 `src/oryxbot_description/maps/` 下。

## 4. 写马字

```bash
roslaunch oryxbot_description draw_ma.launch
```


