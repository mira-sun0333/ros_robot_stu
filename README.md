# ros_robot_stu

ROS 小乌龟 (turtlesim) 录制与回放项目。

## 前置条件

- ROS Noetic (Ubuntu 20.04)
- `turtlesim` 包已安装：`sudo apt install ros-noetic-turtlesim`

## 使用方法

### 设置环境

```bash
source /opt/ros/noetic/setup.bash
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)
```

### 录制

录制小乌龟的 `/turtle1/cmd_vel` 和 `/turtle1/pose` 话题：

```bash
roslaunch ros_robot_stu record.launch
```

或者手动：

```bash
rosrun turtlesim turtlesim_node &
rosbag record -O run.bag /turtle1/cmd_vel /turtle1/pose
```

### 回放

回放录制好的 bag 文件（注意需要 `--clock` 仿真时间）：

```bash
roslaunch ros_robot_stu playback.launch
```

或者手动分步：

```bash
rosparam set /use_sim_time true
rosrun turtlesim turtlesim_node &
rosbag play --clock run.bag
```

### 循环回放

```bash
rosbag play --clock --loop run.bag
```

## bag 文件信息

| 项目 | 内容 |
|------|------|
| 文件名 | run.bag |
| 时长 | 36 秒 |
| 话题 | /turtle1/cmd_vel (121条), /turtle1/pose (2251条) |
| 大小 | 195 KB |

## 项目结构

```
ros_robot_stu/
├── launch/
│   ├── record.launch      # 录制启动文件
│   └── playback.launch    # 回放启动文件
├── run.bag                # 录制数据
├── .gitignore
└── README.md
```
