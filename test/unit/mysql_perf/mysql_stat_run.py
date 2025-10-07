# Classification (U)

"""Program:  mysql_stat_run.py

    Description:  Unit testing of mysql_stat_run in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/mysql_stat_run.py

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
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__
        upd_srv_stat
        upd_srv_perf

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "ServerName"
        self.binlog_disk = "binlog_disk"
        self.uptime_flush = "uptime_flush"
        self.max_conn = "max_conn"
        self.uptime = "uptime"
        self.cur_conn = "cur_conn"

    def upd_srv_stat(self):

        """Method:  upd_srv_stat

        Description:  Stub method holder for mysql_class.Server.upd_srv_stat.

        Arguments:

        """

    def upd_srv_perf(self):

        """Method:  upd_srv_perf

        Description:  Stub method holder for mysql_class.Server.upd_srv_perf.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default
        test_perf_list
        test_perf_empty_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.timeform = "zulu"
        self.current = True
        self.server = Server()
        self.perf_list = ["uptime_flush", "binlog_disk", "cur_conn", "uptime",
                          "max_conn"]
        self.perf_list2 = []
        self.perf_list3 = ["uptime_flush"]
        self.header = {
            "Application": "MySQL_Perf", "Server": "ServerName",
            "AsOf": "YYYYMMDDTHHMMSS"}
        self.results = "uptime_flush"
        self.results2 = "uptime"

    @mock.patch("mysql_perf.create_header")
    def test_perf_list2(self, mock_hdr):

        """Function:  test_perf_list2

        Description:  Test with multiple items in perf_list.

        Arguments:

        """

        mock_hdr.return_value = self.header

        self.assertEqual(
            mysql_perf.mysql_stat_run(
                self.server, self.perf_list, self.dtg, self.timeform,
                self.current)["PerfStats"]["uptime"],
            self.results2)

    @mock.patch("mysql_perf.create_header")
    def test_perf_list(self, mock_hdr):

        """Function:  test_perf_list

        Description:  Test with one item in perf_list.

        Arguments:

        """

        mock_hdr.return_value = self.header

        self.assertEqual(
            mysql_perf.mysql_stat_run(
                self.server, self.perf_list3, self.dtg, self.timeform,
                self.current)["PerfStats"]["uptime_flush"],
            self.results)

    @mock.patch("mysql_perf.create_header")
    def test_perf_empty_list(self, mock_hdr):

        """Function:  test_perf_empty_list

        Description:  Test with perf_list empty.

        Arguments:

        """

        mock_hdr.return_value = self.header

        self.assertEqual(
            mysql_perf.mysql_stat_run(
                self.server, self.perf_list2, self.dtg, self.timeform,
                self.current)["PerfStats"], {})


if __name__ == "__main__":
    unittest.main()
