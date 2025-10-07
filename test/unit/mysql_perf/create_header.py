# Classification (U)

"""Program:  create_header.py

    Description:  Unit testing of create_header in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/create_header.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_perf                                # pylint:disable=E0401,C0413
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                                  # pylint:disable=R0903

    """Class:  RepSet

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__

    """

    def __init__(self, name):                   # pylint:disable=R0913,R0917

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_header2
        test_header

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.server = Server("ServerName")
        self.results = "ServerName"
        self.results2 = "MySQL_Perf"

    def test_header2(self):

        """Function:  test_header2

        Description:  Test with application name.

        Arguments:

        """

        self.assertEqual(
            mysql_perf.create_header(self.dtg, self.server)["Application"],
            self.results2)

    def test_header(self):

        """Function:  test_header

        Description:  Test with server name.

        Arguments:

        """

        self.assertEqual(
            mysql_perf.create_header(self.dtg, self.server)["Server"],
            self.results)


if __name__ == "__main__":
    unittest.main()
