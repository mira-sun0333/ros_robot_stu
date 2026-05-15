# Oryxbot 机器人描述包

## 介绍

该包包含了 Oryxbot 机器人相关的 URDF 文件、xacro 文件、meshes 文件、launch 文件等。

这次主要更新了oryxbot机器人仿真环境。

本包仿真支持ubuntu 18.04(ROS melodic)版本和unbuntu 20.04(ROS noetic)版本，需要配置好ROS环境。

## 配置

scripts文件夹下有配置脚本，需运行后方能正常使用仿真环境。
```bash
./install.sh
```

## 仿真环境

仿真环境基于Gazebo，使用的是Gazebo的默认环境。

启动仿真环境：
```bash
roslaunch oryxbot_description gazebo.launch
```