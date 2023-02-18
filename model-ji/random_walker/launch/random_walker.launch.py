# Copyright 2021 Intelligent Robotics Lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    rand_walker_cmd = Node(
                            package='random_walker',
                            executable='wanderer',
                            output='screen',
                            parameters=[{
                              'use_sim_time': True
                            }],
                            arguments=['--ros-args', '--log-level', 'info'],
                            remappings=[
                              ('input_scan', '/scan'),
                              ('output_vel', '/cmd_vel'),
                              ('output_led_1', '/commands/led1'),
                              ('output_led_2', '/commands/led2'),
                              ('output_sound', '/commands/sound')
                            ])

    ld = LaunchDescription()
    ld.add_action(rand_walker_cmd)

    return ld
