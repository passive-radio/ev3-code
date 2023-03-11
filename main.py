#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

"""
いりなか杯攻略用のプログラム
"""


"""
ロボットを定義する
"""
left = Motor(Port.B)                        # 左モーター
right = Motor(Port.C)                       # 右モーター
color_sensor = ColorSensor(Port.S3)         # カラーセンサー
robot = DriveBase(left, right, 55, 125)     # 走行体を定義した


ev3.speaker.beep()                          # デバッグ用のビープ音

"""
まずカラーセンサー開始地点に移動する
"""
robot.straight(200)                         # 200mm (20cm)　直進する
robot.turn(90)                              # その場で時計回りに90度回る

while not color_sensor.color() == Color.RED:
    if color_sensor.reflection() > 40:
        robot.drive(100, 30)
    else:
        robot.drive(100, -30)
robot.stop()

ev3.speaker.beep()

"""
のりば２に入ってタイルの色を判定する
赤：レストラン→遊園地エリア
青：ホテル→フルーツパークエリア
"""
robot.straight(200)                         # カラータイルまで直進する
wait(1000)                                  # 1秒待機
area = color_sensor.color()                 # 1秒後にカラーセンサーで色を測定する。areaという変数に赤か青を代入する

if area == Color.RED:
    
    robot.turn(90)
    robot.straight(300)
    """
    青色を見つけるまで直進する
    """
    while not color_sensor.color() == Color.BLUE:
        robot.drive(100, 0)
    robot.stop()
    
    ev3.speaker.beep()
    
    """
    中継地点のホテルに入る
    """
    robot.straight(100)
    robot.turn(90)
    
    robot.straight(1000)                # 1000mm (1m)　直進する →フルーツパークエリアに向かう

    ev3.speaker.beep()
else:
    robot.turn(-90)
    robot.staright(300)
    """
    赤色を見つけるまで直進する
    """
    while not color_sensor.color() == Color.RED:
        robot.drive(100, 0)
    robot.stop()
    
    ev3.speaker.beep()
    
    """
    中継地点のレストランに入る
    """
    robot.straight(100)
    robot.turn(-90)
    
    robot.straight(1000)                # 1000mm (1m)　直進する→遊園地エリアに向かう
    
    ev3.speaker.beep()