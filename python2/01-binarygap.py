
# my solution to https://codility.com/programmers/task/binary_gap/

from nose_parameterized import parameterized
import sys
import unittest




def solution(N):

    if N is None:
        raise TypeError

    max_count = 0

    while N / 2 is not 0:
        current_count = 0
        
        while N % 4 is not 1:
            N = N / 2

        N = N / 2
        
        while N is not 0 and N % 2 is 0:
            current_count += 1
            N = N / 2

            if current_count > max_count:
                max_count = current_count
        
    return max_count



class TestBinaryGap(unittest.TestCase):

    def test_invoke_without_argument(self):
        with self.assertRaises(TypeError):
            solution()

    def test_with_none(self):
        with self.assertRaises(TypeError):
            solution(None)

    def _build_parameters(base2_string, expected):
        the_integer = int(base2_string, base=2)
        return (base2_string, the_integer, expected)

    @parameterized.expand([
        _build_parameters('0', 0),
        _build_parameters('1', 0),
        _build_parameters('101', 1),
        _build_parameters('101001', 2),
        _build_parameters('100101', 2),
        _build_parameters('1011', 1),
        _build_parameters('1101', 1),
        _build_parameters('1100000100010000000111110000', 7),
        ('sys.maxint', sys.maxint, 0),
    ])
    def test_solution(self, _, N, expected):
        self.assertEqual(solution(N), expected)
