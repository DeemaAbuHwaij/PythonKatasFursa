import unittest
from katas.matrix_rotate import rotate_matrix


class MyTestCase(unittest.TestCase):
    def test1(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)
    def test2(self):
        matrix = [
            [1, 9, 3],
            [8, 7, 6],
            [12, 8, 10]
        ]
        expected = [
            [12, 8, 1],
            [8, 7, 9],
            [10, 6, 3]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)
    def test3(self):
        matrix = [
            [4, 12, 4],
            [7, 8, 7],
            [4, 12, 4]
        ]
        expected = [
            [4, 7, 4],
            [12, 8, 12],
            [4, 7, 4]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

if __name__ == '__main__':
    unittest.main()


