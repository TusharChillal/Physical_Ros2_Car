from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen'
        ),
        Node(
            package='motor_driver',
            executable='joy_motor_driver',
            name='joy_motor_driver',
            output='screen'
        )
    ])
