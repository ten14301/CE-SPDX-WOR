import unittest

import our_functions

class test_is_valid_date(unittest.TestCase):
    def test_correct_date_format(self):
        date_str = "2023-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)

    def test_incorrect_date_format(self):
        date_str = "03-12-2023"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_not_ture(self):
        date_str = "999-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_leap_year(self):
        date_str = "2020-02-29"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)

    def test_month_13(self):
        date_str = "2020-13-29"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_day_32(self):
        date_str = "2020-02-32"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_leap_year_day(self):
        date_str = "----------"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_day_feb(self):
        date_str = "2001-02-28"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)
        

class test_is_valid_username(unittest.TestCase):
    def test_username_more_than_min(self):
        username_str = "myname"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)

    def test_username_equal_min(self):
        username_str = "myname"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)

    def test_username_less_than_min(self):
        username_str = 1
        min_username_chars = 7
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

    def test_username_not_str(self):
        username_str = ""
        min_username_chars = 0
        with self.assertRaises(TypeError):
            our_functions.is_valid_username(username_str, min_username_chars)

    def test_len_username(self):
        username_str = "my"
        min_username_chars = 3
        with self.assertRaises(ValueError):
            our_functions.is_valid_username(username_str, min_username_chars)
    def test_symbol_username(self):
        username_str = "myname@"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

    def test_number_username(self):
        username_str = "1myname"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

if __name__ == "__main__":
    unittest.main()