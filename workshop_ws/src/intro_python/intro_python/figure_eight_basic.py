from math import pi

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class FigureEight(Node):
    
    def __init__(self):
        # super().__init__('figure_eight')
        super().__init__()
        
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.linear_vel = 1.0 # m/s
        self.angular_vel = 0.5 # rad/s
        cmd_vel_timer_frequency = 30.0 # Hz
        self.cmd_vel_timer = self.create_timer(1/cmd_vel_timer_frequency, self.cmd_vel_callback)
        angular_switch_period = 2*pi / self.angular_vel # s = (rad/(rad/s))
        self.switch_timer = self.create_timer(angular_switch_period, self.switch_angular_vel)
        self.cmd_vel_out = Twist()
        self.cmd_vel_out.linear.x = 0.0
        self.cmd_vel_out.angular.z = 0.0
    
    def cmd_vel_callback(self):
        self.cmd_vel_out.linear.x = self.linear_vel
        self.cmd_vel_out.angular.z = self.angular_vel
        self.cmd_vel_pub.publish(self.cmd_vel_out)
    
    def switch_anglar_vel(self):
        self.angular_vel *= -1
    

def main(args=None):
    rclpy.init(args)
    
    figure_eight_node = FigureEight()
    
    rclpy.spin(figure_eight_node)
    
    figure_eight_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()