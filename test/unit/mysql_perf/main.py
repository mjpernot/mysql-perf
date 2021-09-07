#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/main.py

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


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            (input) cmdline -> Argv command line.
            (input) flavor -> Lock flavor ID.

        """

        self.cmdline = cmdline
        self.flavor = flavor


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_help_true -> Test help if returns true.
        test_help_false -> Test help if returns false.
        test_arg_req_true -> Test arg_require if returns true.
        test_arg_req_false -> Test arg_require if returns false.
        test_arg_cond_false -> Test arg_cond_req if returns false.
        test_arg_cond_true -> Test arg_cond_req if returns true.
        test_arg_dir_true -> Test arg_dir_chk_crt if returns true.
        test_arg_dir_false -> Test arg_dir_chk_crt if returns false.
        test_arg_file_true -> Test arg_file_chk if returns true.
        test_arg_file_false -> Test arg_file_chk if returns false.
        test_run_program -> Test run_program function.
        test_programlock_true -> Test with ProgramLock returns True.
        test_programlock_false -> Test with ProgramLock returns False.
        test_programlock_id -> Test ProgramLock with flavor ID.
        test_interval_positive -> Test with positive interval value.
        test_interval_zero -> Test with zero interval value.
        test_interval_negative -> Test with negative interval value.
        test_loop_positive -> Test with positive loop value.
        test_loop_zero -> Test with zero loop value.
        test_loop_negative -> Test with negative loop value.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-c": "CfgFile", "-d": "CfgDir", "-b": "1",
                           "-n": "1"}
        self.args_array2 = {"-c": "CfgFile", "-d": "CfgDir", "-y": "Flavor",
                            "-b": "1", "-n": "1"}
        self.args_array3 = {"-c": "CfgFile", "-d": "CfgDir", "-b": "1",
                            "-n": "1"}
        self.args_array4 = {"-c": "CfgFile", "-d": "CfgDir", "-b": "0",
                            "-n": "1"}
        self.args_array5 = {"-c": "CfgFile", "-d": "CfgDir", "-b": "-1",
                            "-n": "1"}
        self.args_array6 = {"-c": "CfgFile", "-d": "CfgDir", "-n": "1",
                            "-b": "1"}
        self.args_array7 = {"-c": "CfgFile", "-d": "CfgDir", "-n": "0",
                            "-b": "1"}
        self.args_array8 = {"-c": "CfgFile", "-d": "CfgDir", "-n": "-1",
                            "-b": "1"}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = True

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.arg_parser.arg_require")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_help_false(self, mock_arg, mock_help, mock_req):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.arg_parser.arg_require")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_arg_req_true(self, mock_arg, mock_help, mock_req):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.arg_parser.arg_cond_req")
    @mock.patch("mysql_perf.arg_parser.arg_require")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_arg_req_false(self, mock_arg, mock_help, mock_req, mock_cond):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.arg_parser.arg_cond_req")
    @mock.patch("mysql_perf.arg_parser.arg_require")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_arg_cond_false(self, mock_arg, mock_help, mock_req, mock_cond):

        """Function:  test_arg_cond_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.arg_parser.arg_dir_chk_crt")
    @mock.patch("mysql_perf.arg_parser.arg_cond_req")
    @mock.patch("mysql_perf.arg_parser.arg_require")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_arg_cond_true(self, mock_arg, mock_help, mock_req, mock_cond,
                           mock_dir):

        """Function:  test_arg_cond_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = True
        mock_dir.return_value = True

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.arg_parser.arg_dir_chk_crt")
    @mock.patch("mysql_perf.arg_parser.arg_cond_req")
    @mock.patch("mysql_perf.arg_parser.arg_require")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_arg_dir_true(self, mock_arg, mock_help, mock_req, mock_cond,
                          mock_dir):

        """Function:  test_arg_dir_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = True
        mock_dir.return_value = True

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_arg_dir_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_arg_file_true(self, mock_arg, mock_help):

        """Function:  test_arg_file_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_arg_file_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_file_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_run_program(self, mock_arg, mock_help, mock_lock):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_programlock_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_programlock_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_arg.arg_add_def.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.side_effect = \
            mysql_perf.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_programlock_id(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_id

        Description:  Test ProgramLock with flavor ID.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array2
        mock_arg.arg_add_def.return_value = self.args_array2
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_interval_positive(self, mock_arg, mock_help, mock_lock):

        """Function:  test_interval_positive

        Description:  Test with positive interval value.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array3
        mock_arg.arg_add_def.return_value = self.args_array3
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_interval_zero(self, mock_arg, mock_help, mock_lock):

        """Function:  test_interval_zero

        Description:  Test with zero interval value.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array4
        mock_arg.arg_add_def.return_value = self.args_array4
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_interval_negative(self, mock_arg, mock_help, mock_lock):

        """Function:  test_interval_negative

        Description:  Test with negative interval value.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array5
        mock_arg.arg_add_def.return_value = self.args_array5
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_loop_positive(self, mock_arg, mock_help, mock_lock):

        """Function:  test_loop_positive

        Description:  Test with positive loop value.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array6
        mock_arg.arg_add_def.return_value = self.args_array6
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_loop_zero(self, mock_arg, mock_help, mock_lock):

        """Function:  test_loop_zero

        Description:  Test with zero loop value.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array7
        mock_arg.arg_add_def.return_value = self.args_array7
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.arg_parser")
    def test_loop_negative(self, mock_arg, mock_help, mock_lock):

        """Function:  test_loop_negative

        Description:  Test with negative loop value.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array8
        mock_arg.arg_add_def.return_value = self.args_array8
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())


if __name__ == "__main__":
    unittest.main()
