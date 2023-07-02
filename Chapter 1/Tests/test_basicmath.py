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
                self.assertEqual(expected, actual)

    def test_subtraction(self):
        self.fail()

    def test_multiply(self):
        self.fail()

    def test_divide(self):
        self.fail()

    def test_remainder(self):
        self.fail()
