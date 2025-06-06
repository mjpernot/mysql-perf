# Classification (U)

"""Program:  convert_dict.py

    Description:  Unit testing of convert_dict in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/convert_dict.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_perf                               # pylint:disable=E0401,C0413
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_multi_key_lvl
        test_multi_lvl
        test_multi_dict
        test_one_item
        test_empty_dict

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {}
        self.data2 = {"key1": "value1"}
        self.data3 = {"key1": "value1", "key2": "value2"}
        self.data4 = {"key1": {"key1a": "value1a"}}
        self.data5 = {"key1": {"key1a": "value1a"}, "key2": "value2"}
        self.data6 = {"key1": "value1",
                      "key2": {"key2A": "value2A", "key2B": "value2B"},
                      "key3": {"key3A": {"key3AA": "value3AA"}}}
        self.mail = gen_class.setup_mail("email_addr", subj="subject_line")
        self.results = ""
        self.results2 = "key1:  value1\n"
        self.results3 = "key2:  value2\nkey1:  value1\n"
        self.results3a = "key1:  value1\nkey2:  value2\n"
        self.results4 = "key1:\n    key1a:  value1a\n"
        self.results5 = "key2:  value2\nkey1:\n    key1a:  value1a\n"
        self.results5a = "key1:\n    key1a:  value1a\nkey2:  value2\n"
        self.sub = "key1:  value1\n"
        self.sub2 = "key3:\n    key3A:\n        key3AA:  value3AA\n"
        self.sub3 = "key2:\n    key2B:  value2B\n    key2A:  value2A\n"
        self.sub3a = "key2:\n    key2A:  value2A\n    key2B:  value2B\n"
        self.results6 = self.sub2 + self.sub3 + self.sub
        self.results6a = self.sub + self.sub3a + self.sub2

    def test_nested_dicts(self):

        """Function:  test_nested_dicts

        Description:  Test with nested dictionaries.

        Arguments:

        """

        mysql_perf.convert_dict(self.data6, self.mail)

        if sys.version_info < (3, 0):
            results = self.results6

        else:
            results = self.results6a

        self.assertEqual(self.mail.msg, results)

    def test_multi_key_lvl(self):

        """Function:  test_multi_key_lvl

        Description:  Test with multi-key and multi-level dictionary.

        Arguments:

        """

        mysql_perf.convert_dict(self.data5, self.mail)

        if sys.version_info < (3, 0):
            results = self.results5

        else:
            results = self.results5a

        self.assertEqual(self.mail.msg, results)

    def test_multi_lvl(self):

        """Function:  test_multi_lvl

        Description:  Test with multiple level dictionary.

        Arguments:

        """

        mysql_perf.convert_dict(self.data4, self.mail)

        self.assertEqual(self.mail.msg, self.results4)

    def test_multi_dict(self):

        """Function:  test_multi_dict

        Description:  Test with multiple items in dictionary.

        Arguments:

        """

        mysql_perf.convert_dict(self.data3, self.mail)

        if sys.version_info < (3, 0):
            results = self.results3

        else:
            results = self.results3a

        self.assertEqual(self.mail.msg, results)

    def test_one_item(self):

        """Function:  test_one_item

        Description:  Test with one item in dictionary.

        Arguments:

        """

        mysql_perf.convert_dict(self.data2, self.mail)

        self.assertEqual(self.mail.msg, self.results2)

    def test_empty_dict(self):

        """Function:  test_empty_dict

        Description:  Test with empty dictionary.

        Arguments:

        """

        mysql_perf.convert_dict(self.data, self.mail)

        self.assertEqual(self.mail.msg, self.results)


if __name__ == "__main__":
    unittest.main()
