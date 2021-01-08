#  mpvQC
#
#  Copyright (C) 2021 mpvQC developers
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


import unittest

from mpvqc.core.utility import flat_map


class Test(unittest.TestCase):

    def test_flat_map_simple(self):
        numbers = [[0], [1], [2], [3]]

        expected = (0, 1, 2, 3)
        actual = flat_map(lambda x: x, numbers)

        self.assertEqual(expected, actual)

    def test_flat_map_flat_it(self):
        numbers = [[0, 1], [1, 2, 3], [2], [3], []]

        expected = (0, 1, 1, 2, 3, 2, 3)
        actual = flat_map(lambda x: x, numbers)

        self.assertEqual(expected, actual)
