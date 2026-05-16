# ROS Robot Study - path_jump

ROS（Robot Operating System）机器人学习项目，包含多个 Catkin 工作空间和 ROS 入门教程。

## 项目结构

```
path_jump/
├── ws_A/                   # Catkin 工作空间 A — 基础工作空间
│   └── src/
│       └── CMakeLists.txt  # 顶层 CMake 配置
│
├── ws_B/                   # Catkin 工作空间 B — ROS 教程集合
│   └── src/
│       └── ros_tutorials/  # ROS 官方教程包
│           ├── turtlesim/         # 小海龟仿真器（C++/Qt5）
│           │   ├── src/           # 核心源码
│           │   ├── include/       # 头文件
│           │   ├── tutorials/     # 示例程序
│           │   ├── msg/           # 自定义消息
│           │   ├── srv/           # 自定义服务
│           │   ├── launch/        # 启动文件
│           │   └── images/        # 图片资源
│           │
│           ├── rospy_tutorials/   # Python ROS 教程
│           │   ├── 001_talker_listener/     # 发布者/订阅者
│           │   ├── 002_headers/             # 消息头
│           │   ├── 003_listener_with_user_data/  # 用户数据回调
│           │   ├── 004_listener_subscribe_notify/ # 订阅通知
│           │   ├── 005_add_two_ints/        # 服务通信
│           │   ├── 006_parameters/          # 参数服务器
│           │   ├── 007_connection_header/   # 连接头
│           │   ├── 008_on_shutdown/         # 关闭回调
│           │   ├── 009_advanced_publish/    # 高级发布
│           │   ├── 010_publish_pointcloud2/ # 点云发布
│           │   ├── msg/                     # 自定义消息
│           │   ├── srv/                     # 自定义服务
│           │   └── test/                    # 测试文件
│           │
│           ├── roscpp_tutorials/  # C++ ROS 教程
│           │   ├── talker/                   # 发布者
│           │   ├── listener/                 # 订阅者
│           │   ├── add_two_ints_server/      # 服务端
│           │   ├── add_two_ints_client/      # 客户端
│           │   ├── timers/                   # 定时器
│           │   ├── parameters/               # 参数
│           │   ├── listener_class/           # 类封装订阅者
│           │   ├── babbler/                  # 多话题发布
│           │   ├── time_api/                 # 时间 API
│           │   └── ...                       # 更多教程
│           │
│           └── ros_tutorials/      # 元包
│
└── .gitignore               # Git 忽略规则
```

## 环境要求

- **操作系统**：Ubuntu 20.04+（或其他支持 ROS 的 Linux 发行版）
- **ROS 版本**：ROS Noetic（或其他 ROS 1 发行版）
- **编译工具**：Catkin
- **依赖库**：
  - Qt5（turtlesim 图形界面）
  - Boost（线程支持）
  - Python 3

## 编译与运行

### 1. 初始化工作空间

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
# 加载工作空间 B 的环境
source ws_B/devel/setup.bash
```

### 3. 运行 turtlesim 示例

```bash
# 启动小海龟仿真器
rosrun turtlesim turtlesim_node

# 在另一个终端中，使用键盘控制小海龟
rosrun turtlesim turtle_teleop_key
```

### 4. 运行 talker/listener 示例

```bash
# Python 版本
roslaunch rospy_tutorials talker_listener.launch

# C++ 版本
roslaunch roscpp_tutorials talker_listener.launch
```

## 主要功能

### turtlesim
经典的 ROS 入门仿真器，提供二维平面上的小海龟，支持：
- 键盘/程序控制海龟移动
- 多海龟生成与管理
- 画笔功能（颜色、线宽）
- 绝对/相对坐标移动

### rospy_tutorials
Python 语言 ROS 编程教程，涵盖：
- 话题（Topic）发布与订阅
- 服务（Service）客户端与服务器
- 参数（Parameter）服务器
- 消息头（Header）使用
- 点云（PointCloud2）发布
- 节点关闭回调

### roscpp_tutorials
C++ 语言 ROS 编程教程，涵盖：
- 发布者/订阅者基本模式
- 服务通信
- 定时器与时间 API
- 参数使用
- 多线程回调
- 自定义回调处理

## 学习资源

- [ROS 官方 Wiki](http://wiki.ros.org/)
- [ROS 教程](http://wiki.ros.org/ROS/Tutorials)
- [turtlesim 教程](http://wiki.ros.org/turtlesim)

## 许可证

本项目遵循 BSD 许可证，与 ROS 官方教程保持一致。
