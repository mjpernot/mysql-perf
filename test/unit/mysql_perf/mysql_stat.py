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
        self.args_array = dict()

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Mail():

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

    def send_mail(self, use_mailx=False):

        """Method:  send_mail

        Description:  Stub method holder for Mail.send_mail.

        Arguments:
            (input) use_mailx -> True|False - To use mailx command.

        """

        status = True

        if use_mailx:
            status = True

        return status


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

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_email_no_subj_mailx
        test_email_mailx
        test_email_no_subj
        test_email
        test_interval_zero
        test_interval_one
        test_interval_two
        test_loop_negative
        test_zero_loop
        test_json_flat
        test_json_indent
        test_file_write
        test_file_append
        test_multi_loop
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.mail = Mail()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args5 = ArgParser()
        self.args6 = ArgParser()
        self.args7 = ArgParser()
        self.args8 = ArgParser()
        self.args10 = ArgParser()
        self.args11 = ArgParser()
        self.args11a = ArgParser()
        self.args12 = ArgParser()
        self.args12a = ArgParser()
        self.args.args_array = {"-n": 1, "-b": 1}
        self.args2.args_array = {"-n": 3, "-b": 1}
        self.args3.args_array = {"-n": 1, "-b": 1, "-a": True}
        self.args4.args_array = {"-n": 1, "-b": 1, "-f": True}
        self.args5.args_array = {"-n": 0, "-b": 1}
        self.args6.args_array = {"-n": 2, "-b": 2}
        self.args7.args_array = {"-n": 2, "-b": 1}
        self.args8.args_array = {"-n": 2, "-b": 0}
        self.args10.args_array = {"-n": -1, "-b": 1}
        self.args11.args_array = {
            "-n": 1, "-b": 1, "-t": "email_addr", "-s": "subject_line"}
        self.args11a.args_array = {
            "-n": 1, "-b": 1, "-t": "email_addr", "-s": "subject_line",
            "-u": True}
        self.args12.args_array = {"-n": 1, "-b": 1, "-t": "email_addr"}
        self.args12a.args_array = {
            "-n": 1, "-b": 1, "-t": "email_addr", "-u": True}

    @mock.patch("mysql_perf.gen_class.setup_mail")
    @mock.patch("mysql_perf.mysql_stat_run")
    def test_email_no_subj_mailx(self, mock_process, mock_mail):

        """Function:  test_email_no_subj_mailx

        Description:  Test with email but no subject using mailx.

        Arguments:

        """

        mock_process.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args12a))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    @mock.patch("mysql_perf.mysql_stat_run")
    def test_email_mailx(self, mock_process, mock_mail):

        """Function:  test_email_mailx

        Description:  Test with email option set using mailx.

        Arguments:

        """

        mock_process.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args11a))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    @mock.patch("mysql_perf.mysql_stat_run")
    def test_email_no_subj(self, mock_process, mock_mail):

        """Function:  test_email_no_subj

        Description:  Test with email but no subject in args.

        Arguments:

        """

        mock_process.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args12))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    @mock.patch("mysql_perf.mysql_stat_run")
    def test_email(self, mock_process, mock_mail):

        """Function:  test_email

        Description:  Test with email option set.

        Arguments:

        """

        mock_process.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args11))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_zero(self, mock_process):

        """Function:  test_interval_zero

        Description:  Test with -b option set to zero.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args8))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_one(self, mock_process):

        """Function:  test_interval_two

        Description:  Test with -b option set to one.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args7))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_interval_two(self, mock_process):

        """Function:  test_interval_two

        Description:  Test with -b option set to > one.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args6))

    def test_loop_negative(self):

        """Function:  test_loop_negative

        Description:  Test with -n option set to negative number.

        Arguments:

        """

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args10))

    def test_zero_loop(self):

        """Function:  test_zero_loop

        Description:  Test with -n option set to zero.

        Arguments:

        """

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args5))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_json_flat(self, mock_process):

        """Function:  test_json_flat

        Description:  Test with flatten indentation for JSON.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args4))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_json_indent(self, mock_process):

        """Function:  test_json_indent

        Description:  Test with default indentation for JSON.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_file_write(self, mock_process):

        """Function:  test_file_write

        Description:  Test with setting file write.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args3))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_file_append(self, mock_process):

        """Function:  test_file_append

        Description:  Test with setting file append.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args3))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_multi_loop(self, mock_process):

        """Function:  test_multi_loop

        Description:  Test with multiple loops.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args2))

    @mock.patch("mysql_perf.mysql_stat_run")
    def test_default(self, mock_process):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_process.return_value = True

        self.assertFalse(mysql_perf.mysql_stat(self.server, self.args))


if __name__ == "__main__":
    unittest.main()
