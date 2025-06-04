#苏雨的菜花数据采集机械手控制程序
from interbotix_common_modules.common_robot.robot import robot_shutdown, robot_startup
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from interbotix_common_modules.common_robot.robot import robot_shutdown, robot_startup
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np



"""
This script commands some arbitrary positions to the arm joints:

To get started, open a terminal and type:

    ros2 launch interbotix_xsarm_control xsarm_control.launch robot_model:=wx250s

Then change to this directory and type:

    python3 joint_position_control.py
"""
def on_press(key):
    if key == keyboard.Key.esc:
        print(">>> ESC detected, exiting...")
        return False  # 停止监听

def main():

    bot = InterbotixManipulatorXS(
        robot_model='vx300s',
        group_name='arm',
        gripper_name='gripper',
    )

    robot_startup()
    bot.arm.set_joint_positions([1.55, 0.2, -1.0, 0, 1.8, 0])
    #从下往上，1号关节航向，1号关节俯仰，2号关节俯仰，3号关节滚转，3号关节俯仰，爪子滚转（苏雨） 
    # 等待用户输入
    print("\033[36m>>> 机械臂已就位，按\033[1m回车键\033[0m\033[36m退出并归位...\033[0m")
    print("\033[32m>>> The robotic arm is in position, press \033[1mENTER\033[0m\033[32m to exit and return to the initial position...\033[0m")
    input("")  # 等待用户输入回车

    # 返回 home 位姿
    bot.arm.go_to_sleep_pose()
    robot_shutdown()


if __name__ == '__main__':
    main()
