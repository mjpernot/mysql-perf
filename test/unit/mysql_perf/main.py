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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mysql_perf
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_add_def
        arg_cond_req
        arg_dir_chk
        arg_file_chk
        arg_require
        arg_valid_val
        get_val
        update_arg

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()
        self.opt_val = None
        self.multi_val = None
        self.do_parse = None
        self.defaults = None
        self.add_def_opt_req = None
        self.file_perm_chk = None
        self.file_crt = None
        self.arg_file_chk2 = True
        self.opt_valid_val = None
        self.arg_valid_val2 = True
        self.opt_req = None
        self.opt_req2 = True
        self.opt_con_req = None
        self.opt_con_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True

    def arg_add_def(self, defaults, opt_req):

        """Method:  arg_add_def

        Description:  Method stub holder for gen_class.ArgParser.arg_add_def.

        Arguments:

        """

        self.defaults = defaults
        self.add_def_opt_req = opt_req

    def arg_cond_req(self, opt_con_req):

        """Method:  arg_cond_req

        Description:  Method stub holder for gen_class.ArgParser.arg_cond_req.

        Arguments:

        """

        self.opt_con_req = opt_con_req

        return self.opt_con_req2

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_file_chk(self, file_perm_chk, file_crt):

        """Method:  arg_file_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_file_chk.

        Arguments:

        """

        self.file_perm_chk = file_perm_chk
        self.file_crt = file_crt

        return self.arg_file_chk2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def arg_valid_val(self, opt_valid_val):

        """Method:  arg_valid_val

        Description:  Method stub holder for gen_class.ArgParser.arg_valid_val.

        Arguments:

        """

        self.opt_valid_val = opt_valid_val

        return self.arg_valid_val2

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def update_arg(self, arg_key, arg_val):

        """Method:  update_arg

        Description:  Method stub holder for gen_class.ArgParser.update_arg.

        Arguments:

        """

        self.args_array[arg_key] = arg_val


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

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
        setUp
        test_help_true
        test_help_false
        test_arg_req_false
        test_arg_req_true
        test_arg_cond_false
        test_arg_cond_true
        test_arg_dir_false
        test_arg_dir_true
        test_arg_file_false
        test_arg_file_true
        test_run_program
        test_programlock_true
        test_programlock_false
        test_programlock_id
        test_interval_positive
        test_interval_zero
        test_interval_negative
        test_loop_positive
        test_loop_zero
        test_loop_negative

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args5 = ArgParser()
        self.args6 = ArgParser()
        self.args7 = ArgParser()
        self.args8 = ArgParser()
        self.args.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-b": "1", "-n": "1"}
        self.args2.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-y": "Flavor", "-b": "1",
            "-n": "1"}
        self.args3.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-b": "1", "-n": "1"}
        self.args4.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-b": "0", "-n": "1"}
        self.args5.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-b": "-1", "-n": "1"}
        self.args6.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-n": "1", "-b": "1"}
        self.args7.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-n": "0", "-b": "1"}
        self.args8.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-n": "-1", "-b": "1"}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_arg_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_arg_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_arg_cond_false(self, mock_arg, mock_help):

        """Function:  test_arg_cond_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_arg_cond_true(self, mock_arg, mock_help):

        """Function:  test_arg_cond_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_arg_dir_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_arg_dir_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_arg_file_false(self, mock_arg, mock_help):

        """Function:  test_arg_file_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_arg_file_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_file_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_run_program(self, mock_arg, mock_help, mock_lock):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_programlock_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_programlock_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.side_effect = \
            mysql_perf.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_programlock_id(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_id

        Description:  Test ProgramLock with flavor ID.

        Arguments:

        """

        mock_arg.return_value = self.args2
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_interval_positive(self, mock_arg, mock_help, mock_lock):

        """Function:  test_interval_positive

        Description:  Test with positive interval value.

        Arguments:

        """

        mock_arg.return_value = self.args3
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_interval_zero(self, mock_arg, mock_help, mock_lock):

        """Function:  test_interval_zero

        Description:  Test with zero interval value.

        Arguments:

        """

        mock_arg.return_value = self.args4
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_interval_negative(self, mock_arg, mock_help, mock_lock):

        """Function:  test_interval_negative

        Description:  Test with negative interval value.

        Arguments:

        """

        mock_arg.return_value = self.args5
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_loop_positive(self, mock_arg, mock_help, mock_lock):

        """Function:  test_loop_positive

        Description:  Test with positive loop value.

        Arguments:

        """

        mock_arg.return_value = self.args6
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_loop_zero(self, mock_arg, mock_help, mock_lock):

        """Function:  test_loop_zero

        Description:  Test with zero loop value.

        Arguments:

        """

        mock_arg.return_value = self.args7
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())

    @mock.patch("mysql_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_perf.gen_class.ProgramLock")
    @mock.patch("mysql_perf.gen_libs.help_func")
    @mock.patch("mysql_perf.gen_class.ArgParser")
    def test_loop_negative(self, mock_arg, mock_help, mock_lock):

        """Function:  test_loop_negative

        Description:  Test with negative loop value.

        Arguments:

        """

        mock_arg.return_value = self.args8
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_perf.main())


if __name__ == "__main__":
    unittest.main()
