# Classification (U)

"""Program:  data_out.py

    Description:  Unit testing of data_out in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/data_out.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import json
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mysql_perf                               # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class MailTest():

    """Class:  MailTest

    Description:  Class which is a representation of an email.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self, toline, subj=None, frm=None, msg_type=None):

        """Method:  __init__

        Description:  Initialization of an instance of the Mail class.

        Arguments:

        """

        if isinstance(subj, list):
            subj = list(subj)

        if isinstance(toline, list):
            self.toline = list(toline)

        else:
            self.toline = toline

        self.subj = subj
        self.frm = frm
        self.msg_type = msg_type
        self.msg = ""

    def add_2_msg(self, txt_ln=None):

        """Method:  add_2_msg

        Description:  Add text to text string if data is present.

        Arguments:

        """

        if txt_ln:

            if isinstance(txt_ln, str):
                self.msg = self.msg + txt_ln

            else:
                self.msg = self.msg + json.dumps(txt_ln)

    def send_mail(self, use_mailx=False):

        """Method:  send_mail

        Description:  Send email.

        Arguments:

        """

        status = True

        if use_mailx:
            status = True

        return status


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
        test_email_subj
        test_email_no_subj
        test_email_mailx2
        test_email_mailx
        test_email_indent
        test_separate_true
        test_separate_false
        test_email
        test_indent_true
        test_indent_false
        test_suppress_true
        test_suppress_false_expand2
        test_suppress_false_expand
        test_suppress_false

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = MailTest("toaddr")
        self.data = [{"key": "value", "key2": ["list1", "list2"]}]
        self.to_addr = "To_Address"
        self.subj = "EmailSubject"
        self.mailx = True
        self.mailx2 = False
        self.outfile = "/path/to/file"
        self.mode = "a"
        self.mode2 = "w"
        self.expand = True
        self.expand2 = False
        self.indent = 4
        self.suppress = True
        self.suppress2 = False
        self.separate = False
        self.separate2 = True

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
        data_config["suppress"] = self.suppress

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

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
        data_config["suppress"] = self.suppress

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

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
        data_config["suppress"] = self.suppress

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

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
        data_config["suppress"] = self.suppress

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

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
        data_config["suppress"] = self.suppress

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    @mock.patch("mysql_perf.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile(self):

        """Function:  test_outfile

        Description:  Test with outfile option.

        Arguments:

        """

        data_config = {}
        data_config["outfile"] = self.outfile
        data_config["suppress"] = self.suppress

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_email_subj(self, mock_mail):

        """Function:  test_email_subj

        Description:  Test with email option with subject option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["subj"] = self.subj
        data_config["suppress"] = self.suppress
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_email_no_subj(self, mock_mail):

        """Function:  test_email_no_subj

        Description:  Test with email option with no subject option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["suppress"] = self.suppress
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_email_mailx2(self, mock_mail):

        """Function:  test_email_mailx2

        Description:  Test with email option with mailx option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["mailx"] = self.mailx2
        data_config["suppress"] = self.suppress
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_email_mailx(self, mock_mail):

        """Function:  test_email_mailx

        Description:  Test with email option with mailx option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["mailx"] = self.mailx
        data_config["suppress"] = self.suppress
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_email_indent(self, mock_mail):

        """Function:  test_email_indent

        Description:  Test with email option with indent.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["indent"] = self.indent
        data_config["suppress"] = self.suppress
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_separate_true(self, mock_mail):

        """Function:  test_separate_true

        Description:  Test with separate option set to true.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["suppress"] = self.suppress
        data_config["separate"] = self.separate2

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_separate_false(self, mock_mail):

        """Function:  test_separate_false

        Description:  Test with separate option set to false.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["suppress"] = self.suppress
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_email(self, mock_mail):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["suppress"] = self.suppress
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    def test_indent_true(self):

        """Function:  test_indent_true

        Description:  Test pass in indent arg.

        Arguments:

        """

        data_config = {}
        data_config["indent"] = self.indent
        data_config["suppress"] = self.suppress

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    def test_indent_false(self):

        """Function:  test_indent_false

        Description:  Test with no indent arg passed in.

        Arguments:

        """

        data_config = {}
        data_config["suppress"] = self.suppress

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    def test_suppress_true(self):

        """Function:  test_suppress_true

        Description:  Test with suppression is true.

        Arguments:

        """

        data_config = {}
        data_config["suppress"] = self.suppress

        self.assertFalse(
            mysql_perf.data_out(self.data, data_config, **data_config))

    def test_suppress_false_expand2(self):

        """Function:  test_suppress_false_expand2

        Description:  Test with suppression is false and expand option.

        Arguments:

        """

        data_config = {}
        data_config["expand"] = self.expand2
        data_config["indent"] = self.indent
        data_config["suppress"] = self.suppress2

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_perf.data_out(self.data, data_config, **data_config))

    def test_suppress_false_expand(self):

        """Function:  test_suppress_false_expand

        Description:  Test with suppression is false and expand option.

        Arguments:

        """

        data_config = {}
        data_config["expand"] = self.expand
        data_config["indent"] = self.indent
        data_config["suppress"] = self.suppress2

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_perf.data_out(self.data, data_config, **data_config))

    def test_suppress_false(self):

        """Function:  test_suppress_false

        Description:  Test with suppression is false.

        Arguments:

        """

        data_config = {}
        data_config["suppress"] = self.suppress2

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_perf.data_out(self.data, data_config, **data_config))


if __name__ == "__main__":
    unittest.main()
