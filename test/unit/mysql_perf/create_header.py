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
import time
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
        test_current_false
        test_current_true
        test_timeform_new
        test_timeform_default
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
        time.sleep(1)
        self.server = Server("ServerName")
        self.results = "ServerName"
        self.results2 = "MySQL_Perf"

    def test_current_false(self):

        """Function:  test_current_false

        Description:  Test with current set to false.

        Arguments:

        """

        self.assertEqual(
            mysql_perf.create_header(
                self.dtg, self.server, current=False)["AsOf"],
            self.dtg.get_time(timeform="zulu"))

    def test_current_true(self):

        """Function:  test_current_true

        Description:  Test with current set to true.

        Arguments:

        """

        self.assertNotEqual(
            mysql_perf.create_header(
                self.dtg, self.server)["AsOf"],
            self.dtg.get_time(timeform="zulu"))

    def test_timeform_new(self):

        """Function:  test_timeform_new

        Description:  Test with new timeform name.

        Arguments:

        """

        self.assertEqual(
            len(mysql_perf.create_header(
                self.dtg, self.server, timeform="dtg")["AsOf"]), 15)

    def test_timeform_default(self):

        """Function:  test_timeform_default

        Description:  Test with default timeform name.

        Arguments:

        """

        self.assertEqual(
            len(mysql_perf.create_header(self.dtg, self.server)["AsOf"]), 20)

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
