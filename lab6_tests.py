import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        input1 = [
            data.Book(["Bob","Jeff","Rick"], "Helping Christians"),
            data.Book(["Sam","Dylan","Rick"],"Helping Children"),
            data.Book(["Pluto","Scooby"],"Helping Christmas Elves")]
        result = lab6.selection_sort_books(input1)
        expected = [
                data.Book(["Sam", "Dylan", "Rick"], "Helping Children"),
                data.Book(["Bob","Jeff","Rick"],"Helping Christians") ,
                data.Book(["Pluto","Scooby"], "Helping Christmas Elves")]
        self.assertEqual(expected, result)

    def test_selection_sort_books_2(self):
        input1 = [
            data.Book(["Bob", "Jeff", "Rick"], "Winds of time"),
            data.Book(["Sam", "Dylan", "Rick"], "Changing Worlds"),
            data.Book(["Pluto", "Scooby"], "Mystery Land")]
        result = lab6.selection_sort_books(input1)
        expected = [
            data.Book(["Sam", "Dylan", "Rick"], "Changing Worlds"),
            data.Book(["Pluto", "Scooby"], "Mystery Land"),
            data.Book(["Bob", "Jeff", "Rick"], "Winds of time")]
        self.assertEqual(expected, result)
    # Part 2
    def test_swap_case_1(self):
        input = "HelLo ! WoRld"
        result = lab6.swap_case(input)
        expected = "hELlO ! wOrLD"
        self.assertEqual(expected,result)

    def test_swap_case_2(self):
        input = "こにちわ、mY nAME iS nick! はじめまして。"
        result = lab6.swap_case(input)
        expected = "こにちわ、My Name Is NICK! はじめまして。"
        self.assertEqual(expected, result)
    # Part 3
    def test_str_translate_1(self):
        input = "Hello World, the world is gone forever."
        input2 = "o"
        input3 = "x"
        result = lab6.str_translate(input,input2,input3)
        expected = "Hellx Wxrld, the wxrld is gxne fxrever."
        self.assertEqual(expected,result)

    def test_str_translate_1(self):
        input = "xWaxtxcxhx xOxuxtx"
        input2 = "x"
        input3 = ""
        result = lab6.str_translate(input, input2, input3)
        expected = "Watch Out"
        self.assertEqual(expected, result)
    # Part 4
    def test_histogram_1(self):
        input = "so math is so so math"
        result = lab6.histogram(input)
        expected = {
            "math": 2,
            "is": 1,
            "so": 3
        }
        self.assertEqual(expected,result)

    def test_histogram_2(self):
        input = "woah woah woah man what like what woah"
        result = lab6.histogram(input)
        expected = {
            "woah": 4,
            "man": 1,
            "what": 2,
            "like": 1
        }
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
