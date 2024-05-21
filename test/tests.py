import os
import sys
import unittest

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from GameMenu import GameMenu
from GamePage import GamePage 
import main

class WheelOfFortuneTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_StartGame(self):
        pass

    def test_PlayerNames(self):
        pass

if __name__ == "__main__":
    unittest.main()