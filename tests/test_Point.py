"""Test for LLPoint.py"""

import os
import sys
import unittest

thisFolder = os.path.dirname(os.path.abspath(__file__))
parentFolder = os.path.dirname(os.path.dirname(thisFolder))
sys.path.append(parentFolder)
from LibLathe.LLPoint import Point


class test_point(unittest.TestCase):

    def test_distance_to(self):
        pt = Point(0, 0, 0)
        pt2 = Point(100, 100, 100)
        distance = Point.distance_to(pt, pt2)
        self.assertAlmostEqual(distance, 173.20508075688772)

    def test_angle_to(self):
        pt = Point(0, 0, 0)
        pt2 = Point(100, 100, 100)
        angle = Point.angle_to(pt, pt2)
        self.assertAlmostEqual(angle, 45)

    def test_nearest(self):
        pt = Point(0, 0, 0)
        pt2 = Point(100, 100, 100)
        pt3 = Point(150, 130, 200)
        pts = [pt2, pt3]
        nearest = Point.nearest(pt, pts)
        self.assertAlmostEqual(nearest, pt2)


if __name__ == '__main__':
    unittest.main()
