# Classification (U)

"""Program:  mail_out.py

    Description:  Unit testing of mail_out in mysql_perf.py.

    Usage:
        test/unit/mysql_perf/mail_out.py

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
        test_email_subj
        test_email_no_subj
        test_email_mailx2
        test_email_mailx
        test_email_indent
        test_separate_true
        test_separate_false
        test_email

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = MailTest("toaddr")
        self.mail2 = None
        self.data = [{"key": "value", "key2": ["list1", "list2"]}]
        self.to_addr = "To_Address"
        self.subj = "EmailSubject"
        self.mailx = True
        self.mailx2 = False
        self.indent = 4
        self.separate = False
        self.separate2 = True
        self.cfg = {"indent": 4}

    def test_email_subj(self):

        """Function:  test_email_subj

        Description:  Test with email option with subject option.

        Arguments:

        """

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["subj"] = self.subj
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.mail_out(self.mail, self.data, self.cfg, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_email_no_subj(self, mock_mail):

        """Function:  test_email_no_subj

        Description:  Test with email option with no subject option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.mail_out(self.mail, self.data, self.cfg, **data_config))

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
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.mail_out(self.mail, self.data, self.cfg, **data_config))

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
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.mail_out(self.mail, self.data, self.cfg, **data_config))

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
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.mail_out(self.mail, self.data, self.cfg, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_separate_true(self, mock_mail):

        """Function:  test_separate_true

        Description:  Test with separate option set to true.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["separate"] = self.separate2

        self.assertFalse(
            mysql_perf.mail_out(
                self.mail2, self.data, self.cfg, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_separate_false(self, mock_mail):

        """Function:  test_separate_false

        Description:  Test with separate option set to false.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.mail_out(self.mail, self.data, self.cfg, **data_config))

    @mock.patch("mysql_perf.gen_class.setup_mail")
    def test_email(self, mock_mail):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        data_config = {}
        data_config["to_addr"] = self.to_addr
        data_config["separate"] = self.separate

        self.assertFalse(
            mysql_perf.mail_out(self.mail, self.data, self.cfg, **data_config))


if __name__ == "__main__":
    unittest.main()
