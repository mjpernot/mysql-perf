# Classification (U)

"""Program:  file_out.py

    Description:  Unit testing of file_out in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/file_out.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_outfile_mode_expand2
        test_outfile_mode_expand
        test_outfile_expand
        test_outfile_mode2
        test_outfile_mode
        test_outfile

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = [{"key": "value", "key2": ["list1", "list2"]}]
        self.outfile = "/path/to/file"
        self.mode = "a"
        self.mode2 = "w"
        self.expand = True
        self.expand2 = False
        self.indent = 4
        self.cfg = {"indent": 4}

    @mock.patch("mysql_perf.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_mode_expand2(self, mock_file):

        """Function:  test_outfile_mode_expand2

        Description:  Test with outfile and mode and expand options.

        Arguments:

        """

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        data_config = {}
        data_config["outfile"] = self.outfile
        data_config["mode"] = self.mode2
        data_config["expand"] = self.expand

        self.assertFalse(
            mysql_perf.file_out(self.data, self.cfg, **data_config))

    @mock.patch("mysql_perf.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_mode_expand(self, mock_file):

        """Function:  test_outfile_mode_expand

        Description:  Test with outfile and mode and expand options.

        Arguments:

        """

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        data_config = {}
        data_config["outfile"] = self.outfile
        data_config["mode"] = self.mode
        data_config["expand"] = self.expand

        self.assertFalse(
            mysql_perf.file_out(self.data, self.cfg, **data_config))

    @mock.patch("mysql_perf.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_expand(self, mock_file):

        """Function:  test_outfile_expand

        Description:  Test with outfile option with expand.

        Arguments:

        """

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        data_config = {}
        data_config["outfile"] = self.outfile
        data_config["expand"] = self.expand

        self.assertFalse(
            mysql_perf.file_out(self.data, self.cfg, **data_config))

    @mock.patch("mysql_perf.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile_mode2(self):

        """Function:  test_outfile_mode2

        Description:  Test with outfile and mode option.

        Arguments:

        """

        data_config = {}
        data_config["outfile"] = self.outfile
        data_config["mode"] = self.mode2

        self.assertFalse(
            mysql_perf.file_out(self.data, self.cfg, **data_config))

    @mock.patch("mysql_perf.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile_mode(self):

        """Function:  test_outfile_mode

        Description:  Test with outfile and mode option.

        Arguments:

        """

        data_config = {}
        data_config["outfile"] = self.outfile
        data_config["mode"] = self.mode

        self.assertFalse(
            mysql_perf.file_out(self.data, self.cfg, **data_config))

    @mock.patch("mysql_perf.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile(self):

        """Function:  test_outfile

        Description:  Test with outfile option.

        Arguments:

        """

        data_config = {}
        data_config["outfile"] = self.outfile

        self.assertFalse(
            mysql_perf.file_out(self.data, self.cfg, **data_config))


if __name__ == "__main__":
    unittest.main()
