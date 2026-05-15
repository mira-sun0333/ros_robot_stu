#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
绘制"马"字轨迹导航节点
控制机器人按马字笔画运动，在RViz中用Path显示轨迹
用法: roslaunch oryxbot_description draw_ma.launch
"""
import rospy
import math
import tf
from nav_msgs.msg import Path
from geometry_msgs.msg import Twist, PoseStamped


class DrawMa:
    def __init__(self):
        rospy.init_node('draw_ma')

        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.path_pub = rospy.Publisher('/ma_trajectory', Path, queue_size=1, latch=True)

        self.tf_listener = tf.TransformListener()

        # 轨迹 Path (仅记录笔画, 跳过过渡移动)
        self.path = Path()
        self.path.header.frame_id = 'odom'

        self.linear_speed = 0.35
        self.angular_speed = 0.8
        self.rate = rospy.Rate(20)
        self.drawing = True

    def get_pose(self):
        """获取机器人位姿 (odom 坐标系)"""
        try:
            self.tf_listener.waitForTransform(
                'odom', 'base_footprint', rospy.Time(0), rospy.Duration(1.0))
            (trans, rot) = self.tf_listener.lookupTransform(
                'odom', 'base_footprint', rospy.Time(0))
            yaw = tf.transformations.euler_from_quaternion(rot)[2]
            return trans[0], trans[1], yaw
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            return None

    def record(self):
        """记录当前位置到轨迹 (仅笔画时记录)"""
        if not self.drawing:
            return
        pose = self.get_pose()
        if pose is None:
            return
        ps = PoseStamped()
        ps.header.frame_id = 'odom'
        ps.header.stamp = rospy.Time.now()
        ps.pose.position.x = pose[0]
        ps.pose.position.y = pose[1]
        ps.pose.orientation.z = math.sin(pose[2] / 2)
        ps.pose.orientation.w = math.cos(pose[2] / 2)
        self.path.poses.append(ps)
        self.path.header.stamp = rospy.Time.now()
        self.path_pub.publish(self.path)

    def move_forward(self, distance):
        """前进/后退指定距离"""
        twist = Twist()
        twist.linear.x = self.linear_speed if distance > 0 else -self.linear_speed
        start = self.get_pose()
        if start is None:
            return
        traveled = 0
        while abs(traveled) < abs(distance) and not rospy.is_shutdown():
            self.cmd_pub.publish(twist)
            self.rate.sleep()
            current = self.get_pose()
            if current:
                dx = current[0] - start[0]
                dy = current[1] - start[1]
                traveled = dx * math.cos(start[2]) + dy * math.sin(start[2])
            self.record()
        self.stop()

    def turn(self, angle):
        """原地旋转指定角度 (弧度, 正=逆时针)"""
        twist = Twist()
        twist.angular.z = self.angular_speed if angle > 0 else -self.angular_speed
        start = self.get_pose()
        if start is None:
            return
        turned = 0
        while abs(turned) < abs(angle) and not rospy.is_shutdown():
            self.cmd_pub.publish(twist)
            self.rate.sleep()
            current = self.get_pose()
            if current:
                turned = current[2] - start[2]
                while turned > math.pi:
                    turned -= 2 * math.pi
                while turned < -math.pi:
                    turned += 2 * math.pi
            self.record()
        self.stop()

    def stop(self):
        twist = Twist()
        self.cmd_pub.publish(twist)

    def goto(self, x, y, draw=True):
        """移动到绝对坐标 (odom坐标系), draw=True 记录笔画"""
        self.drawing = draw
        pose = self.get_pose()
        if pose is None:
            return
        dx = x - pose[0]
        dy = y - pose[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance < 0.02:
            return
        target_angle = math.atan2(dy, dx)
        angle_diff = target_angle - pose[2]
        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        while angle_diff < -math.pi:
            angle_diff += 2 * math.pi

        self.turn(angle_diff)
        rospy.sleep(0.2)
        self.move_forward(distance)
        rospy.sleep(0.2)

    def run(self):
        rospy.sleep(3)

        # ========== 马 字参数 ==========
        # 缩放: s 越大字越大, 偏移: ox/oy 平移字的中心
        s = 1.0
        ox = 0.0
        oy = 0.0

        rospy.loginfo("===== 开始绘制 马 字 =====")

        # 笔画1: 横折 (顶部横线 + 右侧竖线)
        rospy.loginfo("笔画1: 横折")
        self.goto(0.0 * s + ox, 0.0 * s + oy, draw=True)   
        self.goto(2.0 * s + ox, 0.0 * s + oy, draw=True)    
        self.goto(2.0 * s + ox, -2.0 * s + oy, draw=True)    
        self.goto(0.5 * s + ox, -2.0 * s + oy, draw=True)
        self.goto(0.5 * s + ox, -0.5 * s + oy, draw=True)
        self.goto(0.5 * s + ox, -2.0 * s + oy, draw=True)
        self.goto(2.5 * s + ox, -2.0 * s + oy, draw=True)
        self.goto(2.5 * s + ox, -4.0 * s + oy, draw=True)
        self.goto(2.0 * s + ox, -3.5 * s + oy, draw=True)
        self.goto(2.5 * s + ox, -4.0 * s + oy, draw=True)
        self.goto(2.5 * s + ox, -3.0 * s + oy, draw=True)
        self.goto(0.0 * s + ox, -3.0 * s + oy, draw=True)
        



if __name__ == '__main__':
    try:
        drawer = DrawMa()
        drawer.run()
    except rospy.ROSInterruptException:
        pass
