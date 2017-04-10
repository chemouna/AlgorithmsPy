import unittest

from mounacheikhna.algorithms.detecttriangle.DetectTriangleGraph import get_num_triangles_dfs


class Test(unittest.TestCase):
    def test1(self):
        A = [(0, 1), (2, 1), (0, 2), (4, 1)]
        res = get_num_triangles_dfs(A)
        self.assertEqual(1, res)

    def test2(self):
        A = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
        res = get_num_triangles_dfs(A)
        self.assertEqual(2, res)

    def test3(self):
        A = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
        res = get_num_triangles_dfs(A)
        self.assertEqual(2, res)

    def test4(self):
        A = [(0, 1), (2, 1), (0, 2), (4, 1)]
        res = get_num_triangles_dfs(A)
        self.assertEqual(1, res)

    def test5(self):
        A = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)]
        res = get_num_triangles_dfs(A)
        self.assertEqual(4, res)


if __name__ == '__main__':
    unittest.main(verbosity=2)
