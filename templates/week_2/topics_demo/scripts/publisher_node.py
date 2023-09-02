#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import sys

# Import message type
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__("node_publisher")
        self.get_logger().info(f'ROS 2 Node is running with name node_zero')

        # Initialize Publisher
        # self.publisher_ = self.create_publisher(MessageType, 'Topic_Name', 10)
        # self.timer_ = self.create_timer(Frequency, CallBackFunction)
        # self.msg_ = String()

    # Callback Function
    # def publish_message(self):
    #     self.msg_.data = 'Hello, ROS 2!'
    #     self.publisher_.publish(self.msg_)
    #     self.get_logger().info(f'Publishing: {self.msg_.data}')

def main(args=None):
    rclpy.init(args=args)

    node = MyNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
