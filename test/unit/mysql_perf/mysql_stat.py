# Classification (U)

"""Program:  mysql_stat.py

    Description:  Unit testing of mysql_stat in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/mysql_stat.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mysql_perf                               # pylint:disable=E0401,C0413
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Server():                                         # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_interval_zero
        test_interval_one
        test_interval_two
        test_loop_negative
        test_zero_loop
        test_multi_loop
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.data_config = {"option": "value"}
        self.server = Server()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args5 = ArgParser()
        self.args6 = ArgParser()
        self.args7 = ArgParser()
        self.args8 = ArgParser()
        self.args10 = ArgParser()
        self.args.args_array = {"-n": 1, "-b": 1}
        self.args2.args_array = {"-n": 3, "-b": 1}
        self.args5.args_array = {"-n": 0, "-b": 1}
        self.args6.args_array = {"-n": 2, "-b": 2}
        self.args7.args_array = {"-n": 2, "-b": 1}
        self.args8.args_array = {"-n": 2, "-b": 0}
        self.args10.args_array = {"-n": -1, "-b": 1}
        self.mysql_stat_run = {"Stats": "Stats_Here"}

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_zero(self, mock_process):

        """Function:  test_interval_zero

        Description:  Test with -b option set to zero.

        Arguments:

        """

        mock_process.return_value = self.mysql_stat_run

        self.assertFalse(
            mysql_perf.mysql_stat(
                self.server, self.args8, self.dtg, self.data_config))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_one(self, mock_process):

        """Function:  test_interval_two

        Description:  Test with -b option set to one.

        Arguments:

        """

        mock_process.return_value = self.mysql_stat_run

        self.assertFalse(
            mysql_perf.mysql_stat(
                self.server, self.args7, self.dtg, self.data_config))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_two(self, mock_process):

        """Function:  test_interval_two

        Description:  Test with -b option set to greater than one.

        Arguments:

        """

        mock_process.return_value = self.mysql_stat_run

        self.assertFalse(
            mysql_perf.mysql_stat(
                self.server, self.args6, self.dtg, self.data_config))

    def test_loop_negative(self):

        """Function:  test_loop_negative

        Description:  Test with -n option set to negative number.

        Arguments:

        """

        self.assertFalse(
            mysql_perf.mysql_stat(
                self.server, self.args10, self.dtg, self.data_config))

    def test_zero_loop(self):

        """Function:  test_zero_loop

        Description:  Test with -n option set to zero.

        Arguments:

        """

        self.assertFalse(
            mysql_perf.mysql_stat(
                self.server, self.args5, self.dtg, self.data_config))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_multi_loop(self, mock_process):

        """Function:  test_multi_loop

        Description:  Test with multiple loops.

        Arguments:

        """

        mock_process.return_value = self.mysql_stat_run

        self.assertFalse(
            mysql_perf.mysql_stat(
                self.server, self.args2, self.dtg, self.data_config))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_default(self, mock_process):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_process.return_value = self.mysql_stat_run

        self.assertFalse(
            mysql_perf.mysql_stat(
                self.server, self.args, self.dtg, self.data_config))


if __name__ == "__main__":
    unittest.main()
