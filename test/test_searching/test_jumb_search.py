import unittest
from random import randint, choice

from source.algorithm.searching.jump_searching import jump_searching

print(" This unit test is disabled")

'''class TestJumbSearch(unittest.TestCase):

    def test_case_1(self):
        input_list = [randint(0,50) for i in range(20)]
        input_list.sort()

        element, step = choice(input_list), randint(1,5)

        self.assertEqual(jump_searching(input_list, element, step), input_list.index(element) )

    def test_case_2(self):
        input_list = [0, 1, 2, 3, 4, 5, 6, 7]
        element, step = choice(input_list), randint(1,5)

        self.assertEqual(jump_searching(input_list, element, step), element )



if __name__ == '__main__':
    unittest.main()
'''
