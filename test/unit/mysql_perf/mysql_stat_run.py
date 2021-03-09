#!/usr/bin/python
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


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__ -> Class initialization.
        add_2_msg -> Stub method holder for Mail.add_2_msg.
        send_mail -> Stub method holder for Mail.send_mail.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        self.data = data

        return True

    def send_mail(self):

        """Method:  send_mail

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        return True


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__ -> Class initialization.
        upd_srv_stat -> Stub method holder for mysql_class.Server.upd_srv_stat.
        upd_srv_perf -> Stub method holder for mysql_class.Server.upd_srv_perf.

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

        pass

    def upd_srv_perf(self):

        """Method:  upd_srv_perf

        Description:  Stub method holder for mysql_class.Server.upd_srv_perf.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_insert_fail -> Test with failed insert into Mongo.
        test_insert_success -> Test with successful insert into Mongo.
        test_mail_std -> Test with email in standard format.
        test_mail_json -> Test with email in JSON format.
        test_json_file_no_stdout -> Test JSON & output to file but no std out.
        test_json_file_stdout -> Test JSON on and output to a file and std out.
        test_json_std_out -> Test with JSON on and no standard out.
        test_json_nostd -> Test with JSON on and no standard out.
        test_json_file -> Test with JSON on and output to a file.
        test_error_handling -> Test error handling.
        test_no_mongo_cfg -> Test with no config for mongo passed.
        test_no_mongo_db_tbl -> Test with no db_tbl for mongo passed.
        test_mongo -> Test with mongo connection.
        test_default -> Test with default settings.
        test_perf_list -> Test with perf_list populated.
        test_perf_empty_list -> Test with perf_list empty.
        test_no_perf_list -> Test with no perf_list passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.mail = Mail()
        self.args_array = {"-j": True}
        self.args_array2 = {}
        self.perf_list = ["uptime_flush", "binlog_disk", "cur_conn", "uptime",
                          "max_conn"]
        self.perf_list2 = []
        self.ofile = "/path/file"

    @mock.patch("mysql_perf.mongo_libs.ins_doc")
    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_insert_fail(self, mock_print, mock_mongo):

        """Function:  test_insert_fail

        Description:  Test with failed insert into Mongo.

        Arguments:

        """

        mock_print.return_value = (False, None)
        mock_mongo.return_value = (False, "Connection Error")

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_perf.mysql_stat_run(
                    self.server, db_tbl="db:tbl", perf_list=self.perf_list,
                    class_cfg="Cfg"))

    @mock.patch("mysql_perf.mongo_libs.ins_doc")
    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_insert_success(self, mock_print, mock_mongo):

        """Function:  test_insert_success

        Description:  Test with successful insert into Mongo.

        Arguments:

        """

        mock_print.return_value = (False, None)
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_perf.mysql_stat_run(
                self.server, db_tbl="db:tbl", perf_list=self.perf_list,
                class_cfg="Cfg"))

    def test_mail_std(self):

        """Function:  test_mail_std

        Description:  Test with email in standard format.

        Arguments:

        """

        self.assertFalse(mysql_perf.mysql_stat_run(
            self.server, self.perf_list, json_fmt=True, mail=self.mail,
            no_std=True))

    def test_mail_json(self):

        """Function:  test_mail_json

        Description:  Test with email in JSON format.

        Arguments:

        """

        self.assertFalse(mysql_perf.mysql_stat_run(
            self.server, self.perf_list, json_fmt=False, mail=self.mail,
            no_std=True))

    @mock.patch("mysql_perf.gen_libs.write_file")
    def test_json_file_no_stdout(self, mock_file):

        """Function:  test_json_file_stdout

        Description:  Test with JSON on and output to a file but no std out.

        Arguments:

        """

        mock_file.return_value = True

        self.assertFalse(mysql_perf.mysql_stat_run(
            self.server, self.perf_list, json_fmt=True, ofile=self.ofile,
            no_std=True))

    @mock.patch("mysql_perf.gen_libs.print_data")
    @mock.patch("mysql_perf.gen_libs.write_file")
    def test_json_file_stdout(self, mock_file, mock_print):

        """Function:  test_json_file_stdout

        Description:  Test with JSON on and output to a file and std out.

        Arguments:

        """

        mock_file.return_value = True
        mock_print.return_value = True

        self.assertFalse(mysql_perf.mysql_stat_run(
            self.server, self.perf_list, json_fmt=True, ofile=self.ofile,
            no_std=False))

    @mock.patch("mysql_perf.gen_libs.print_data")
    def test_json_std_out(self, mock_print):

        """Function:  test_json_nostd

        Description:  Test with JSON on and no standard out.

        Arguments:

        """

        mock_print.return_value = True

        self.assertFalse(mysql_perf.mysql_stat_run(
            self.server, self.perf_list, json_fmt=True, no_std=False))

    def test_json_nostd(self):

        """Function:  test_json_nostd

        Description:  Test with JSON on and no standard out.

        Arguments:

        """

        self.assertFalse(mysql_perf.mysql_stat_run(
            self.server, self.perf_list, json_fmt=True, no_std=True))

    @mock.patch("mysql_perf.gen_libs.write_file")
    def test_json_file(self, mock_file):

        """Function:  test_json_file

        Description:  Test with JSON on and output to a file.

        Arguments:

        """

        mock_file.return_value = True

        self.assertFalse(mysql_perf.mysql_stat_run(
            self.server, self.perf_list, json_fmt=True, ofile=self.ofile,
            no_std=True))

    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_error_handling(self, mock_print):

        """Function:  test_error_handling

        Description:  Test error handling.

        Arguments:

        """

        mock_print.return_value = (True, "Error Message")

        with gen_libs.no_std_out():
            self.assertFalse(mysql_perf.mysql_stat_run(
                self.server, perf_list=self.perf_list))

    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_no_mongo_cfg(self, mock_print):

        """Function:  test_no_mongo_cfg

        Description:  Test with no config for mongo passed.

        Arguments:

        """

        mock_print.return_value = (False, None)

        self.assertFalse(mysql_perf.mysql_stat_run(
            self.server, perf_list=self.perf_list, db_tbl="db:tbl"))

    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_no_mongo_db_tbl(self, mock_print):

        """Function:  test_no_mongo_db_tbl

        Description:  Test with no db_tbl for mongo passed.

        Arguments:

        """

        mock_print.return_value = (False, None)

        self.assertFalse(mysql_perf.mysql_stat_run(
            self.server, perf_list=self.perf_list, class_cfg="Cfg"))

    @mock.patch("mysql_perf.mongo_libs.ins_doc")
    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_mongo(self, mock_print, mock_mongo):

        """Function:  test_mongo

        Description:  Test with mongo connection.

        Arguments:

        """

        mock_print.return_value = (False, None)
        mock_mongo.return_value = (True, None)

        self.assertFalse(
            mysql_perf.mysql_stat_run(
                self.server, db_tbl="db:tbl", perf_list=self.perf_list,
                class_cfg="Cfg"))

    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_default(self, mock_print):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_print.return_value = (False, None)

        self.assertFalse(mysql_perf.mysql_stat_run(self.server))

    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_perf_list(self, mock_print):

        """Function:  test_perf_list

        Description:  Test with perf_list populated.

        Arguments:

        """

        mock_print.return_value = (False, None)

        self.assertFalse(mysql_perf.mysql_stat_run(self.server,
                                                   perf_list=self.perf_list))

    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_perf_empty_list(self, mock_print):

        """Function:  test_perf_empty_list

        Description:  Test with perf_list empty.

        Arguments:

        """

        mock_print.return_value = (False, None)

        self.assertFalse(mysql_perf.mysql_stat_run(self.server,
                                                   perf_list=self.perf_list2))

    @mock.patch("mysql_perf.gen_libs.print_dict")
    def test_no_perf_list(self, mock_print):

        """Function:  test_no_perf_list

        Description:  Test with no perf_list passed.

        Arguments:

        """

        mock_print.return_value = (False, None)

        self.assertFalse(mysql_perf.mysql_stat_run(self.server))


if __name__ == "__main__":
    unittest.main()
