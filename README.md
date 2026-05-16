# Path Jump — ROS 路径跳转

基于 ROS（Robot Operating System）的路径跳转项目，实现机器人路径规划与跳转控制。

## 项目概要

本项目旨在研究和实现机器人在复杂环境中的**路径跳转（Path Jump）**能力——即机器人能够根据环境信息动态调整路径，实现智能避障和路径重规划。项目使用 ROS 作为通信框架，目前处于基础功能开发阶段。

## 项目结构

```
path_jump/
├── ws_A/                   # Catkin 工作空间 A — 路径跳转核心开发空间
│   └── src/
│       └── CMakeLists.txt  # 顶层 CMake 配置
│
├── ws_B/                   # Catkin 工作空间 B — ROS 基础教程与仿真
│   └── src/
│       └── ros_tutorials/  # ROS 教程包（用于学习和验证基础功能）
│           ├── turtlesim/         # 小海龟仿真器（C++/Qt5）— 路径跳转可视化验证
│           │   ├── src/           # 核心源码
│           │   ├── include/       # 头文件
│           │   ├── tutorials/     # 示例程序（键盘控制、路径绘制等）
│           │   ├── msg/           # 自定义消息（Pose、Color）
│           │   ├── srv/           # 自定义服务（Spawn、Kill、Teleport 等）
│           │   ├── launch/        # 启动文件
│           │   └── images/        # 图片资源
│           │
│           ├── rospy_tutorials/   # Python ROS 教程
│           │   ├── 001_talker_listener/     # 话题发布/订阅
│           │   ├── 002_headers/             # 消息头
│           │   ├── 003_listener_with_user_data/  # 回调用户数据
│           │   ├── 004_listener_subscribe_notify/ # 订阅通知
│           │   ├── 005_add_two_ints/        # 服务通信
│           │   ├── 006_parameters/          # 参数服务器
│           │   ├── 007_connection_header/   # 连接头
│           │   ├── 008_on_shutdown/         # 关闭回调
│           │   ├── 009_advanced_publish/    # 高级发布
│           │   └── 010_publish_pointcloud2/ # 点云发布
│           │
│           ├── roscpp_tutorials/  # C++ ROS 教程
│           │   ├── talker/                   # 发布者
│           │   ├── listener/                 # 订阅者
│           │   ├── add_two_ints_server/      # 服务端
│           │   ├── add_two_ints_client/      # 客户端
│           │   ├── timers/                   # 定时器
│           │   ├── parameters/               # 参数
│           │   ├── listener_class/           # 类封装订阅者
│           │   ├── time_api/                 # 时间 API
│           │   └── ...                       # 更多教程
│           │
│           └── ros_tutorials/      # 元包
│
└── .gitignore               # Git 忽略规则
```

## 环境要求

- **操作系统**：Ubuntu 20.04+
- **ROS 版本**：ROS Noetic（或兼容的 ROS 1 发行版）
- **编译工具**：Catkin
- **依赖库**：
  - Qt5（turtlesim 图形界面）
  - Boost（线程支持）
  - Python 3

## 快速开始

### 1. 编译工作空间

```bash
# 编译工作空间 A
cd ws_A
catkin_make

# 编译工作空间 B
cd ws_B
catkin_make
```

### 2. 加载环境

```bash
source ws_B/devel/setup.bash
```

### 3. 运行 turtlesim 仿真（用于路径规划可视化验证）

```bash
# 启动小海龟仿真器
rosrun turtlesim turtlesim_node

# 键盘控制小海龟
rosrun turtlesim turtle_teleop_key
```

### 4. 测试话题通信

```bash
# Python 版本
roslaunch rospy_tutorials talker_listener.launch

# C++ 版本
roslaunch roscpp_tutorials talker_listener.launch
```

### 5. 验证 roscd 路径跳转

```bash
# roscd 跳转到 ros_tutorials 包路径
roscd ros_tutorials
pwd
# 输出应为当前工作空间下的 ros_tutorials 源码路径
```

## 开发路线

- [ ] 路径跳转核心算法设计与实现
- [ ] 基于 turtlesim 的路径规划可视化
- [ ] 多海龟协同路径跳转
- [ ] 动态避障与路径重规划
- [ ] ROS 服务端/客户端架构完善

## 许可证

BSD License
