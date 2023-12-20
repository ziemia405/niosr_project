import argparse
import sys
import cv2
import numpy as np
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge # ROS2 package to convert between ROS and OpenCV Images


class ArucoDetect(Node):
    def __init__(self):
        super().__init__('aruco_detect')
        self.robot_controller = self.create_publisher(Twist, 'cmd_vel', 10)
        self.cam_feed = self.create_subscription(Image, 'image_raw', self.follow, 10)
        self.cam_feed # zeby kokon przeszedl

    def follow(self, image_data):
        frame = CvBridge().imgmsg_to_cv2(image_data, "bgr8")
        speed = Twist()

        # Jeśli poprawnie odczytano klatkę
        # Wyświetlenie klatki
        dx = 640
        dy = 480

        # Inicjalizacja detektora ArUco oraz Detekcja markerów ArUco
        arucoParams = cv2.aruco.DetectorParameters_create()
        arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)
        (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

        # Przygotowanie listy narożników
        if len(corners) > 0:
            rogi = [corner for marker in corners for corner in marker[0]]
            rogi = np.array(rogi)
            ld = rogi[0]
            pd = rogi[1]
            pg = rogi[2]
            lg = rogi[3]

            if pd[1] < 0.5 * dy:
                print('gora')
                speed.linear.x = 1.0
            else:
                print('dol')
                speed.linear.x = -1.0
            # Parametry do rysowania punktów
            color = (0, 255, 0)  # Zielony
            radius = 5
            thickness = -1  # Wypełniony okrąg

            # Rysowanie punktów na obrazie
            cv2.circle(frame, (int(ld[0]), int(ld[1])), radius, color, thickness)
            cv2.circle(frame, (int(pd[0]), int(pd[1])), radius, color, thickness)
            cv2.circle(frame, (int(pg[0]), int(pg[1])), radius, color, thickness)
            cv2.circle(frame, (int(lg[0]), int(lg[1])), radius, color, thickness)
            self.robot_controller.publish(speed)
        else:
            speed.linear.x = 0.0
            self.robot_controller.publish(speed)
        cv2.imshow('Frame', frame)
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            print("[INFO] Exit by key press")
            cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    aruco = ArucoDetect()
    rclpy.spin(aruco)
    aruco.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
