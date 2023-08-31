# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/run_program.py

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


def mysql_stat(server, args_array, **kwargs):

    """Method:  mysql_stat

    Description:  Function stub holder for mysql_perf.mysql_stat.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Stub holder for dictionary of args.
        (input) **kwargs
            class_cfg -> Stub holder for Mongo configuration.

    """

    status = True
    mongo_cfg = kwargs.get("class_cfg", None)

    if server and args_array and mongo_cfg:
        status = True

    return status


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_args_keys
        get_val
        arg_exist

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "Server_Name"
        self.conn_msg = None

    def connect(self, silent=False):

        """Method:  connect

        Description:  Stub method holder for mysql_class.Server.connect.

        Arguments:

        """

        status = True

        if silent:
            status = True

        return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_conn_fail_suppress
        test_connect_failure
        test_connect_success
        test_mongo
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args.args_array = {"-m": True, "-d": True, "-c": True, "-S": True}
        self.args2.args_array = {
            "-m": True, "-d": True, "-c": True, "-S": True, "-e": "ToEmail",
            "-s": "SubjectLine"}
        self.args3.args_array = {"-d": True, "-c": True, "-S": True}
        self.args4.args_array = {
            "-d": True, "-c": True, "-S": True, "-w": True}
        self.func_names = {"-S": mysql_stat}

    @mock.patch("mysql_perf.mysql_libs.create_instance")
    def test_conn_fail_suppress(self, mock_inst):

        """Function:  test_conn_fail_suppress

        Description:  Test with failed conn with suppression.

        Arguments:

        """

        self.server.conn_msg = "Error connection message"

        mock_inst.return_value = self.server

        self.assertFalse(
            mysql_perf.run_program(self.args4, self.func_names))

    @mock.patch("mysql_perf.mysql_libs.create_instance")
    def test_connect_failure(self, mock_inst):

        """Function:  test_connect_failure

        Description:  Test with failed connection.

        Arguments:

        """

        self.server.conn_msg = "Error connection message"

        mock_inst.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_perf.run_program(self.args3, self.func_names))

    @mock.patch("mysql_perf.mysql_libs.disconnect")
    @mock.patch("mysql_perf.mysql_libs.create_instance")
    def test_connect_success(self, mock_inst, mock_disconn):

        """Function:  test_connect_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(
            mysql_perf.run_program(self.args3, self.func_names))

    @mock.patch("mysql_perf.mysql_libs.disconnect")
    @mock.patch("mysql_perf.gen_libs.load_module")
    @mock.patch("mysql_perf.mysql_libs.create_instance")
    def test_mongo(self, mock_inst, mock_mongo, mock_disconn):

        """Function:  test_mongo

        Description:  Test with mongo option.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_mongo.return_value = True
        mock_disconn.return_value = True

        self.assertFalse(
            mysql_perf.run_program(self.args, self.func_names))

    @mock.patch("mysql_perf.mysql_libs.disconnect")
    @mock.patch("mysql_perf.mysql_libs.create_instance")
    def test_run_program(self, mock_inst, mock_disconn):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(
            mysql_perf.run_program(self.args3, self.func_names))


if __name__ == "__main__":
    unittest.main()
