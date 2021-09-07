#!/usr/bin/python
# Classification (U)

"""Program:  _process_json.py

    Description:  Unit testing of _process_json in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/_process_json.py

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
import version

__version__ = version.__version__


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__
        add_2_msg
        send_mail

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mail_json
        test_json_file_no_stdout
        test_json_file_stdout
        test_json_std_out
        test_json_no_std
        test_json_file

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.mail2 = None
        self.ofile = "/path/file"
        self.ofile2 = None
        self.jdata = {"Server": "Server_Name",
                      "PerfStats": {"key1": "value1"}}
        self.mode = "a"
        self.mode2 = "w"
        self.no_std = True
        self.no_std2 = False

    def test_mail_json(self):

        """Function:  test_mail_json

        Description:  Test with email in JSON format.

        Arguments:

        """

        self.assertFalse(mysql_perf._process_json(
            self.jdata, self.ofile2, self.mail, self.mode, self.no_std))

    @mock.patch("mysql_perf.gen_libs.write_file")
    def test_json_file_no_stdout(self, mock_file):

        """Function:  test_json_file_stdout

        Description:  Test with JSON on and output to a file but no std out.

        Arguments:

        """

        mock_file.return_value = True

        self.assertFalse(mysql_perf._process_json(
            self.jdata, self.ofile, self.mail2, self.mode, self.no_std))

    @mock.patch("mysql_perf.gen_libs.print_data")
    @mock.patch("mysql_perf.gen_libs.write_file")
    def test_json_file_stdout(self, mock_file, mock_print):

        """Function:  test_json_file_stdout

        Description:  Test with JSON on and output to a file and std out.

        Arguments:

        """

        mock_file.return_value = True
        mock_print.return_value = True

        self.assertFalse(mysql_perf._process_json(
            self.jdata, self.ofile, self.mail2, self.mode, self.no_std2))

    @mock.patch("mysql_perf.gen_libs.print_data")
    def test_json_std_out(self, mock_print):

        """Function:  test_json_nostd

        Description:  Test with JSON on and standard out.

        Arguments:

        """

        mock_print.return_value = True

        self.assertFalse(mysql_perf._process_json(
            self.jdata, self.ofile2, self.mail2, self.mode, self.no_std2))

    def test_json_no_std(self):

        """Function:  test_json_no_std

        Description:  Test with JSON on and no standard out.

        Arguments:

        """

        self.assertFalse(mysql_perf._process_json(
            self.jdata, self.ofile2, self.mail2, self.mode, self.no_std))

    @mock.patch("mysql_perf.gen_libs.write_file")
    def test_json_file(self, mock_file):

        """Function:  test_json_file

        Description:  Test with JSON on and output to a file.

        Arguments:

        """

        mock_file.return_value = True

        self.assertFalse(mysql_perf._process_json(
            self.jdata, self.ofile, self.mail2, self.mode, self.no_std))


if __name__ == "__main__":
    unittest.main()
