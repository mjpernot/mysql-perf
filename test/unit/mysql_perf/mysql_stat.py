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
