import unittest
import numpy as np
import game


class TestNash(unittest.TestCase):
    def test_1(self):
        first, second, res = game.nash_equilibrium(np.array([[ 5,  6,  3,  0],
                                                             [10,  5, 12, 10],
                                                             [10,  0,  5, 20]]))
        self.assertEqual(first, ['5/11', '6/11', '0'])
        self.assertEqual(second, ['0', '10/11', '0', '1/11'])
        self.assertEqual(res, '60/11')

    def test_2(self):
        first, second, res = game.nash_equilibrium(np.array([[5, 6, 5],
                                                             [4, 5, 7]]))
        self.assertEqual(first, ['1', '0'])
        self.assertEqual(second, ['1', '0', '0'])
        self.assertEqual(res, '5')
        
    def test_3(self):
        first, second, res = game.nash_equilibrium(np.array([[0, 0, 0],
                                                             [0, 0, 0]]))
        self.assertEqual(first,['1', '0'])
        self.assertEqual(second,['1', '0', '0'])
        self.assertEqual(res, '0')


if __name__ == '__main__':
    unittest.main()
