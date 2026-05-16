# query_service_pkg

基于 ROS（Robot Operating System）的站点查询服务包，实现服务器-客户端（Server-Client）架构，通过 ROS Service 通信机制提供站点信息查询功能。

## 功能概述

- **服务端（Server）**：维护站点数据库，接收查询请求并返回站点名称和位置信息
- **客户端（Client）**：向服务端发送站点编号，获取并展示查询结果
- **通信方式**：基于 ROS Service（`QueryStation.srv`）进行请求-响应式通信

## 文件结构

```
query_service_pkg/
├── CMakeLists.txt          # catkin 构建配置文件
├── package.xml             # ROS 包元信息
├── srv/
│   └── QueryStation.srv    # 服务定义文件
├── scripts/
│   ├── server.py           # 服务端脚本
│   └── client.py           # 客户端脚本
└── README.md
```

## 服务定义（QueryStation.srv）

```
# 请求
string station_id
---
# 响应
string station_name
string station_location
```

## 站点数据库

| 编号   | 名称          | 位置     |
|--------|---------------|----------|
| 510000 | 城市:广州     | 广州省   |
| 610000 | 城市:成都     | 四川省   |
| 04547  | 城市:首尔     | 韩国     |
| 2000   | 城市:悉尼     | 澳大利亚 |
| 10001  | 城市:纽约     | 美国     |
| 310000 | 城市:杭州     | 浙江省   |
| 5003   | 城市:卑尔根   | 瑞典     |
| 665000 | 城市:普洱     | 云南省   |
| 710000 | 城市:西安     | 陕西省   |
| 333000 | 城市:景德镇   | 江西省   |

## 环境要求

- **ROS**（推荐 Melodic 或更高版本）
- **Python 3**
- **catkin** 构建工具

## 编译

1. 将本包复制到你的 catkin 工作空间的 `src` 目录下：

```bash
cd ~/catkin_ws/src
cp -r /path/to/query_service_pkg .
```

2. 编译：

```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

## 使用方法

### 1. 启动 ROS Master

```bash
roscore
```

### 2. 启动服务端

在新终端中运行：

```bash
source ~/catkin_ws/devel/setup.bash
rosrun query_service_pkg server.py
```

服务端启动后将显示：

```
服务端已启动，等待请求...
```

### 3. 运行客户端查询

在新终端中运行：

```bash
source ~/catkin_ws/devel/setup.bash
rosrun query_service_pkg client.py <station_id>
```

示例：

```bash
rosrun query_service_pkg client.py 510000
```

输出：

```
==============================
      站点查询结果
==============================
编号: 510000
名称: 城市:广州
位置: 广州省
==============================
```

如果查询的编号不存在，将返回：

```
名称: 未知站点
位置: 未知位置
```

## 工作原理

1. 服务端 `/station_query_server` 节点启动后注册名为 `query_station_service` 的 ROS Service
2. 客户端 `/station_query_client` 节点通过 `query_station_service` 向服务端发起请求
3. 服务端在数据库中查找对应编号，返回站点名称和位置
4. 客户端接收响应并格式化输出结果

## 许可证

TODO
