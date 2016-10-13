import unittest
from reshow_lena import lena

class test_reshow_lena(unittest.TestCase):
    def test_load_lena(self):
        l = lena()
        self.assertEqual(l.shape, (512,512))
