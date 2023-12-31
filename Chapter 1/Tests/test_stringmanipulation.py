from unittest import TestCase
import stringmanipulation as sm


class Test(TestCase):
    def test_make_lowercase(self):
        tests = [
            ["HELLO THERE!", "hello there!"],
            ["Try this one On For Size.", "try this one on for size."],
            ["We're Number 1!", "we're number 1!"]
        ]
        for the_string, expected in tests:
            with self.subTest(f"{the_string} -> {expected}"):
                actual = sm.make_lowercase(the_string)
                self.assertEqual(actual, expected)

    def test_make_uppercase(self):
        tests = [
            ["hello there!", "HELLO THERE!"],
            ["Try this one On For Size", "TRY THIS ONE ON FOR SIZE"],
            ["we're number 1!", "WE'RE NUMBER 1!"]
        ]
        for the_string, expected in tests:
            with self.subTest(f"{the_string} -> {expected}"):
                actual = sm.make_uppercase(the_string)
                self.assertEqual(actual, expected)


    def test_reverse(self):
        tests = [
            ["racecar", "racecar"],
            ["Reverse Me Please","esaelP eM esreveR"],
            ["we're number 1!", "!1 rebmun er'ew"]
        ]
        for the_string, expected in tests:
            with self.subTest(f"{the_string} -> {expected}"):
                actual = sm.reverse(the_string)
                self.assertEqual(actual, expected)


    def test_string_length(self):
        tests = [
            ["I am the very model of a modern major general", 45],
            ["This string is 33 characters long", 33]
        ]
        for the_string, expected in tests:
            with self.subTest(f"{the_string} -> {expected}"):
                actual = sm.length(the_string)
                self.assertEqual(actual, expected)

    def test_cut_string_in_half(self):
        tests = [
            ["Egads, you have divided me!", "ve divided me!"],
            ["How Dare", "Dare!"]
        ]
        for the_string, expected in tests:
            with self.subTest(f"{the_string} -> {expected}"):
                actual = sm.reverse(the_string)
                self.assertEqual(actual, expected)

    def test_remove_character(self):
        tests = [
            ["Hello there my friend!", "e", "Hllo thr my frind!"],
            ["A large collection of words", "l", "A arge coection of words"]
        ]
        for the_string,the_character, expected in tests:
            with self.subTest(f"{the_string},{the_character} -> {expected}"):
                actual = sm.remove_character(the_string, the_character)
                self.assertEqual(actual, expected)

    def test_remove_word(self):
        self.fail()

    def test_remove_vowels(self):
        self.fail()

    def test_remove_list_of_characters(self):
        self.fail()
