from unittest import TestCase
import basicmath


class Test(TestCase):
    def test_addition(self):
        tests = [
            [2, 3, 5],
            [2, 10, 12],
            [200, 3, 203]
        ]
        for value1, value2, expected in tests:
            with self.subTest(f"{value1}, {value2} -> {expected}"):
                actual = basicmath.addition(value1, value2)
                self.assertEqual(actual, expected)

    def test_subtraction(self):
        tests = [
            [2, 3, -1],
            [10, 2, 8],
            [200, 3, 197]
        ]
        for value1, value2, expected in tests:
            with self.subTest(f"{value1}, {value2} -> {expected}"):
                actual = basicmath.subtraction(value1, value2)
                self.assertEqual(actual, expected)

    def test_multiply(self):
        tests = [
            [2, 3, 6],
            [10, 2, 20],
            [200, 3, 600]
        ]
        for value1, value2, expected in tests:
            with self.subTest(f"{value1}, {value2} -> {expected}"):
                actual = basicmath.multiply(value1, value2)
                self.assertEqual(actual, expected)

    def test_divide(self):
        self.fail()

    def test_remainder(self):
        self.fail()
