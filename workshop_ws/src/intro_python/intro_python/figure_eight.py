from math import atan2

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion

class FigureEight(Node):
    
    def __init__(self) -> None:
        super().__init__('figure_eight_complex')
        
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_sub_callback, 10)
        
        self.cmd_vel = Twist()
        self.cmd_vel.linear.x = 1.0
        self.cmd_vel.angular.z = 0.5
        self.tolerance = 0.075
        self.first_call = True
        self.out_of_tolerance = False
        self.reference_angle = 0.0
    
    def get_yaw(self, orientation_msg : Quaternion):
        x, y = orientation_msg.x, orientation_msg.y
        z, w = orientation_msg.z, orientation_msg.w
        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y ** 2 + z ** 2)
        return atan2(siny_cosp, cosy_cosp)
        
    
    def odom_sub_callback(self, odom_msg : Odometry) -> None:
        measured_yaw = self.get_yaw(odom_msg.pose.pose.orientation)
        if self.first_call:
            self.reference_angle = measured_yaw
        else:
            if abs(measured_yaw - self.reference_angle) < self.tolerance:
                self.cmd_vel.angular.z *= -1
        self.cmd_vel_pub.publish(self.cmd_vel)

def main(args=None):
    rclpy.init(args=args)
    
    figure_eight_node = FigureEight()
    
    rclpy.spin(figure_eight_node)
    
    figure_eight_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()