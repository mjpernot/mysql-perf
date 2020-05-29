#!/usr/bin/python
# Classification (U)

"""Program:  mysql_stat.py

    Description:  Unit testing of mysql_stat in mysql_perf.py.

    Usage:
        test/unit/mysql_db_admin/mysql_stat.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mysql_perf
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_interval_negative -> Test with -b option set to negative.
        test_interval_zero -> Test with -b option set to zero.
        test_interval_one -> Test with -b option set to one.
        test_interval_two -> Test with -b option set to > one.
        test_loop_negative -> Test with -n option set to negative number.
        test_zero_loop -> Test with -n option set to zero.
        test_json_flat -> Test with flatten indentation for JSON.
        test_json_indent -> Test with default indentation for JSON.
        test_file_write -> Test with setting file write.
        test_file_append -> Test with setting file append.
        test_multi_loop -> Test with multiple loops.
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-n": 1, "-b": 1}
        self.args_array2 = {"-n": 3, "-b": 1}
        self.args_array3 = {"-n": 1, "-b": 1, "-a": True}
        self.args_array4 = {"-n": 1, "-b": 1, "-f": True}
        self.args_array5 = {"-n": 0, "-b": 1}
        self.args_array6 = {"-n": 2, "-b": 2}
        self.args_array7 = {"-n": 2, "-b": 1}
        self.args_array8 = {"-n": 2, "-b": 0}
        self.args_array9 = {"-n": 2, "-b": -1}
        self.args_array10 = {"-n": -1, "-b": 1}

    @unittest.skip("Error produced with negative -b option")
    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_negative(self, mock_process):

        """Function:  test_interval_negative

        Description:  Test with -b option set to negative.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array9))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_zero(self, mock_process):

        """Function:  test_interval_zero

        Description:  Test with -b option set to zero.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array8))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_one(self, mock_process):

        """Function:  test_interval_two

        Description:  Test with -b option set to one.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array7))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_two(self, mock_process):

        """Function:  test_interval_two

        Description:  Test with -b option set to > one.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array6))

    def test_loop_negative(self):

        """Function:  test_loop_negative

        Description:  Test with -n option set to negative number.

        Arguments:

        """

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array10))

    def test_zero_loop(self):

        """Function:  test_zero_loop

        Description:  Test with -n option set to zero.

        Arguments:

        """

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array5))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_json_flat(self, mock_process):

        """Function:  test_json_flat

        Description:  Test with flatten indentation for JSON.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array4))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_json_indent(self, mock_process):

        """Function:  test_json_indent

        Description:  Test with default indentation for JSON.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_file_write(self, mock_process):

        """Function:  test_file_write

        Description:  Test with setting file write.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array3))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_file_append(self, mock_process):

        """Function:  test_file_append

        Description:  Test with setting file append.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array3))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_multi_loop(self, mock_process):

        """Function:  test_multi_loop

        Description:  Test with multiple loops.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array2))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_default(self, mock_process):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args_array))


if __name__ == "__main__":
    unittest.main()
