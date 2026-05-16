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
roscd ros_tutorials
pwd
```

## Path Jump 命令速查

> 以下命令帮助你在 ROS 文件系统中快速"跳转"和"定位"。

### 文件系统跳转（rospack / roscd / rosls / rosed）

| 命令 | 说明 |
|------|------|
| `rospack find <pkg>` | 查找包的绝对路径 |
| `rospack list` | 列出所有 ROS 包及其路径 |
| `rospack depends <pkg>` | 查看包的依赖 |
| `roscd <pkg>` | **跳转**到包目录 |
| `roscd <pkg>/<subdir>` | 跳转到包的子目录 |
| `roscd log` | 跳转到 ROS 日志目录 |
| `rosls <pkg>` | 列出包内文件 |
| `rosed <pkg> <file>` | 直接编辑包内文件（支持 Tab 补全） |

### 节点跳转（rosnode）

| 命令 | 说明 |
|------|------|
| `rosnode list` | 列出所有运行中的节点 |
| `rosnode info <node>` | 查看节点详细信息 |
| `rosnode ping <node>` | 测试节点连通性 |
| `rosnode kill <node>` | 停止指定节点 |
| `rosnode machine <host>` | 列出某主机上的节点 |

### 话题跳转（rostopic）

| 命令 | 说明 |
|------|------|
| `rostopic list` | 列出所有活跃话题 |
| `rostopic info <topic>` | 查看话题类型和发布/订阅者 |
| `rostopic echo <topic>` | 实时查看话题数据 |
| `rostopic hz <topic>` | 查看话题发布频率 |
| `rostopic type <topic>` | 查看话题消息类型 |
| `rostopic pub <topic> <type> <data>` | 手动发布消息 |

### 消息/服务跳转（rosmsg / rossrv）

| 命令 | 说明 |
|------|------|
| `rosmsg show <type>` | 查看消息结构 |
| `rosmsg list` | 列出所有消息类型 |
| `rosmsg package <pkg>` | 列出某包的所有消息 |
| `rossrv show <type>` | 查看服务结构 |
| `rossrv list` | 列出所有服务类型 |
| `rossrv package <pkg>` | 列出某包的所有服务 |

### 服务调用（rosservice）

| 命令 | 说明 |
|------|------|
| `rosservice list` | 列出所有活跃服务 |
| `rosservice info <srv>` | 查看服务详情 |
| `rosservice call <srv> <args>` | 调用服务 |
| `rosservice type <srv>` | 查看服务类型 |

### 参数跳转（rosparam）

| 命令 | 说明 |
|------|------|
| `rosparam list` | 列出所有参数 |
| `rosparam get <param>` | 获取参数值 |
| `rosparam set <param> <value>` | 设置参数 |
| `rosparam dump <file>` | 导出参数到 YAML 文件 |
| `rosparam load <file>` | 从 YAML 文件加载参数 |

### 运行与 Launch

| 命令 | 说明 |
|------|------|
| `rosrun <pkg> <node>` | 运行包中的节点 |
| `roslaunch <pkg> <file>` | 启动 launch 文件 |
| `roslaunch --nodes <file>` | 预览 launch 文件会启动的节点 |

### 可视化调试

| 命令 | 说明 |
|------|------|
| `rqt_graph` | 查看节点-话题关系图 |
| `rqt_plot <topic> <field>` | 实时绘制话题数据曲线 |
| `rqt_console` | 查看日志信息 |
| `rviz` | 3D 可视化工具 |

## 开发路线

- [ ] 路径跳转核心算法设计与实现
- [ ] 基于 turtlesim 的路径规划可视化
- [ ] 多海龟协同路径跳转
- [ ] 动态避障与路径重规划
- [ ] ROS 服务端/客户端架构完善

## 许可证

BSD License
