# Classification (U)

"""Program:  create_data_config.py

    Description:  Unit testing of create_data_config in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/create_data_config.py

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
import mysql_perf                           # pylint:disable=E0401,C0413
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

        self.args_array = {
            "-c": "mysql_cfg", "-d": "config", "-t": "to_addr",
            "-o": "outfile", "-i": "indentation", "-s": "subject",
            "-i": "1", "-a": "a", "-p": False, "-u": True}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mode_with_no_data
        test_mode_with_data
        test_mailx_with_no_data
        test_mailx_with_data
        test_subj_with_no_data
        test_subj_with_data
        test_to_addr_with_no_data
        test_to_addr_with_data

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args2.args_array = {}
        self.results = None
        self.results2 = "to_addr"
        self.results3 = False
        self.results4 = "a"
        self.results5 = "subject"
        self.results6 = True
        self.results7 = "w"

    @mock.patch("mysql_perf.gen_libs.load_module")
    def test_mode_with_no_data(self, mock_load):

        """Function:  test_mode_with_no_data

        Description:  Test with mode with data.

        Arguments:

        """

        mock_load.return_value = "Mongo_Config"

        self.assertEqual(
            mysql_perf.create_data_config(self.args2)["mode"],
            self.results7)

    @mock.patch("mysql_perf.gen_libs.load_module")
    def test_mode_with_data(self, mock_load):

        """Function:  test_mode_with_data

        Description:  Test with mode with data.

        Arguments:

        """

        mock_load.return_value = "Mongo_Config"

        self.assertEqual(
            mysql_perf.create_data_config(self.args)["mode"],
            self.results4)

    @mock.patch("mysql_perf.gen_libs.load_module")
    def test_mailx_with_no_data(self, mock_load):

        """Function:  test_mailx_with_no_data

        Description:  Test with mailx with no data.

        Arguments:

        """

        mock_load.return_value = "Mongo_Config"

        self.assertEqual(
            mysql_perf.create_data_config(self.args2)["mailx"],
            self.results3)

    @mock.patch("mysql_perf.gen_libs.load_module")
    def test_mailx_with_data(self, mock_load):

        """Function:  test_mailx_with_data

        Description:  Test with mailx with no data.

        Arguments:

        """

        mock_load.return_value = "Mongo_Config"

        self.assertEqual(
            mysql_perf.create_data_config(self.args)["mailx"],
            self.results6)

    @mock.patch("mysql_perf.gen_libs.load_module")
    def test_subj_with_no_data(self, mock_load):

        """Function:  test_subj_with_no_data

        Description:  Test with to_address with data.

        Arguments:

        """

        mock_load.return_value = "Mongo_Config"

        self.assertEqual(
            mysql_perf.create_data_config(self.args2)["subj"],
            self.results)

    @mock.patch("mysql_perf.gen_libs.load_module")
    def test_subj_with_data(self, mock_load):

        """Function:  test_subj_with_data

        Description:  Test with to_address with data.

        Arguments:

        """

        mock_load.return_value = "Mongo_Config"

        self.assertEqual(
            mysql_perf.create_data_config(self.args)["subj"],
            self.results5)

    @mock.patch("mysql_perf.gen_libs.load_module")
    def test_to_addr_with_no_data(self, mock_load):

        """Function:  test_to_addr_with_no_data

        Description:  Test with to_address with no data.

        Arguments:

        """

        mock_load.return_value = "Mongo_Config"

        self.assertEqual(
            mysql_perf.create_data_config(self.args2)["to_addr"],
            self.results)

    @mock.patch("mysql_perf.gen_libs.load_module")
    def test_to_addr_with_data(self, mock_load):

        """Function:  test_to_addr_with_data

        Description:  Test with to_address with data.

        Arguments:

        """

        mock_load.return_value = "Mongo_Config"

        self.assertEqual(
            mysql_perf.create_data_config(self.args)["to_addr"],
            self.results2)


if __name__ == "__main__":
    unittest.main()
