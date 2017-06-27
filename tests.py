#!/usr/bin/env python3

import unittest
from guillotine import Guillotine
from functools import cmp_to_key

class ChTest(unittest.TestCase):

    def setUp(self):
        rects = [(2, 12), (12, 2), (4, 17), (17, 4), (5, 14), (14, 5), (7, 25), (25, 7), (22, 14), (14, 22), (12, 29), (29, 12), (18, 24), (24, 18), (22, 20), (20, 22), (26, 18), (18, 26), (18, 27), (27, 18)]
        self.g = Guillotine((60, 60), rects)
        self.cut = (0, 0, 17, 4, 1, (17, 0, 17, 4, 1, (34, 0, 17, 4, 1, None, None), None), (0, 4, 12, 29, 1, (12, 4, 12, 2, 1, None, (12, 6, 18, 24, 1, (30, 6, 12, 2, 1, (42, 6, 12, 2, 1, None, None), (30, 8, 12, 2, 1, None, (30, 10, 25, 7, 1, None, (30, 17, 14, 5, 1, (44, 17, 12, 2, 1, None, None), None)))), None)), (0, 33, 22, 20, 1, (22, 33, 12, 2, 1, (34, 33, 12, 2, 1, None, None), (22, 35, 5, 14, 1, (27, 35, 5, 14, 1, (32, 35, 2, 12, 1, (34, 35, 2, 12, 1, (36, 35, 2, 12, 1, (38, 35, 2, 12, 1, (40, 35, 2, 12, 1, (42, 35, 2, 12, 1, (44, 35, 2, 12, 1, (46, 35, 2, 12, 1, (48, 35, 12, 2, 1, None, None), None), None), None), None), None), None), None), None), None), (22, 49, 17, 4, 1, None, None))), None)))
        self.pieces = [(17, 4), (17, 4), (17, 4), (12, 29), (12, 2), (18, 24), (12, 2), (12, 2), (12, 2), (25, 7), (14, 5), (12, 2), (22, 20), (12, 2), (12, 2), (5, 14), (5, 14), (2, 12), (2, 12), (2, 12), (2, 12), (2, 12), (2, 12), (2, 12), (2, 12), (12, 2), (17, 4)]
        self.sorted_pieces = sorted(self.pieces, key=cmp_to_key(self.__cmp))

    def test_lower_y(self):
        pieces = sorted(self.g.pieces(self.cut), key=cmp_to_key(self.__cmp))
        self.assertEqual(len(self.sorted_pieces), len(pieces))
        self.assertEqual(self.sorted_pieces, pieces)

    def test_cut(self):
        pieces = self.g.pieces(self.cut)
        self.assertEqual(self.cut, self.g.cut(pieces))

    def __cmp(self, a, b):
        if a[0] == b[0]:
            return a[1] - b[1]
        else:
            return a[0] - b[0]

if __name__ == '__main__':
    unittest.main()
