# Classification (U)

"""Program:  std_out.py

    Description:  Unit testing of std_out in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/std_out.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_perf                           # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_std_out_expand_true
        test_std_out_expand_false
        test_std_out

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = [{"key": "value", "key2": ["list1", "list2"]}]
        self.expand = True
        self.expand2 = False
        self.cfg = {"indent": 4}

    def test_std_out_expand_true(self):

        """Function:  test_std_out_expand_true

        Description:  Test with standard out and expand option is true.

        Arguments:

        """

        data_config = {}
        data_config["expand"] = self.expand

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_perf.std_out(self.data, self.cfg, **data_config))

    def test_std_out_expand_false(self):

        """Function:  test_std_out_expand_false

        Description:  Test with standard out and expand option is true.

        Arguments:

        """

        data_config = {}
        data_config["expand"] = self.expand2

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_perf.std_out(self.data, self.cfg, **data_config))

    def test_std_out(self):

        """Function:  test_std_out

        Description:  Test with standard out.

        Arguments:

        """

        data_config = {}

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_perf.std_out(self.data, self.cfg, **data_config))


if __name__ == "__main__":
    unittest.main()
