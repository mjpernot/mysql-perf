#!/usr/bin/python
# Classification (U)

"""Program:      mysql_perf.py

    Description:  Performance administration program for MySQL database
        servers.  Has a number of functions to include capturing database
        performance statistical data and sending the data out in a number of
        formats or to the database.

    Usage:
        mysql_perf.py -c file -d path
            {-S [-j [-f]] [-n count] [-b seconds]
                [-t email_addr [email_addr2 ...] [-s subject_line] [-u]]
                [-i [db_name:table_name] -m file]
                [-o [dir_path]/file [-a]] [-w] [-z]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c file => MySQL server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.

        -S => MySQL Database Performance Statistics option.
            -j => Return output in JSON format.
                -f => Flatten the JSON data structure to file and standard out.
            -n count => Number of loops to run the program.  Default:  1
            -b seconds => Polling interval in seconds.  Default:  1
            -i [database:collection] => Name of database and collection to
                insert the database statistics data into.
                Default:  sysmon:mysql_perf
            -m file => Mongo config file.  Is loaded as a python, do not
                include the .py extension with the name.
            -o [path]/file => Directory path and file name for output.
            -a => Append output to output file.
            -t email_addr email_addr2 => Enables emailing capability for an
                option if the option allows it.  Sends output to one or more
                email addresses.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -u => Override the default mail command and use mailx.
            -w => Suppress printing initial connection errors.
            -z => Suppress standard out.

        -y value => A flavor id for the program lock.  To create unique lock.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and/or -h overrides all other options.
        NOTE 2:  If email is used, only a compilation of all performance
            reports from a multiple loop run will be emailed out.

    Notes:
        MySQL configuration file format (config/mysql_cfg.py.TEMPLATE):
            # Configuration file:
            user = "USER"
            japd = "PSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            sid = SERVER_ID
            extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
            serv_os = "Linux"
            port = 3306
            cfg_file = "MYSQL_DIRECTORY/mysqld.cnf"

        NOTE 1:  Include the cfg_file even if running remotely as the
            file will be used in future releases.
        NOTE 2:  In MySQL 5.6 - it now gives warning if password is passed on
            the command line.  To suppress this warning, will require the use
            of the --defaults-extra-file option (i.e. extra_def_file) in the
            database configuration file.  See below for the
            defaults-extra-file format.

        Defaults Extra File format (config/mysql.cfg.TEMPLATE):
            [client]
            password="PASSWORD"
            socket="MYSQL_DIRECTORY/mysqld.sock"

        NOTE 1:  The socket information can be obtained from the mysqld.cnf
            file under ~/mysql directory.
        NOTE 2:  The --defaults-extra-file option will be overridden if there
            is a ~/.my.cnf or ~/.mylogin.cnf file located in the home directory
            of the user running this program.  The extras file will in effect
            be ignored.

        Mongo configuration file format (config/mongo.py.TEMPLATE).  The
            configuration file format for the Mongo connection used for
            inserting data into a database.
            There are two ways to connect:  single or replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "USER"
            japd = "PSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = 27017
            conf_file = None
            auth = True
            auth_db = "admin"
            use_arg = True
            use_uri = False

            2.)  Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mysql_perf.py -c mysql_cfg -d config -S -j -n 9 -b 5 -i -m mongo

"""

# Libraries and Global Variables

# Standard
import sys
import time

# Third-party
import json

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import mysql_lib.mysql_class as mysql_class
import mysql_lib.mysql_libs as mysql_libs
import mongo_lib.mongo_libs as mongo_libs
import version

__version__ = version.__version__

# Global
SUBJ_LINE = "MySQL_Performance"


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def convert_dict(data, mail, **kwargs):

    """Function:  convert_dict

    Description:  Convert dictionary document to standard format and add to
        mail body.

    Arguments:
        (input) data -> Dictionary document.
        (input) mail -> Mail class instance.
        (input) kwargs:
            indent -> Level of indentation for printing.

    """

    data = dict(data)
    indent = kwargs.get("indent", 0)
    spc = " "

    for key, val in data.iteritems():

        if isinstance(val, dict):
            mail.add_2_msg("{0}{1}:\n".format(spc * indent, key))
            convert_dict(val, mail, indent=indent + 4)

        else:
            mail.add_2_msg("{0}{1}:  {2}\n".format(spc * indent, key, val))


def mysql_stat_run(server, perf_list=None, **kwargs):

    """Function:  mysql_stat_run

    Description:  Updated the class' server and performance statistics.  Send
        to output in a number of different formats (e.g. standard, or JSON) and
        to a number of locations (e.g. standard out, database, and/or file).

    Arguments:
        (input) server -> Database server instance.
        (input) perf_list -> List of performance statistics.
        (input) **kwargs:
            class_cfg -> Mongo server configuration.
            indent -> Indentation level for JSON document.
            mode -> File write mode.
            db_tbl -> database:collection - Name of db and collection.
            ofile -> file name - Name of output file.
            no_std -> Suppress standard out.
            json_fmt -> True|False - convert output to JSON format.
            mail -> Mail class instance.

    """

    json_fmt = kwargs.get("json_fmt", False)
    indent = kwargs.get("indent", 4)
    mongo_cfg = kwargs.get("class_cfg", None)
    db_tbl = kwargs.get("db_tbl", None)
    ofile = kwargs.get("ofile", None)
    mode = kwargs.get("mode", "w")
    no_std = kwargs.get("no_std", False)
    mail = kwargs.get("mail", None)

    if perf_list is None:
        perf_list = []

    else:
        perf_list = list(perf_list)

    server.upd_srv_stat()
    server.upd_srv_perf()
    data = {"Server": server.name,
            "AsOf": gen_libs.get_date() + " " + gen_libs.get_time(),
            "PerfStats": {}}

    for item in perf_list:
        data["PerfStats"].update({item: getattr(server, item)})

    if mongo_cfg and db_tbl:
        dbn, tbl = db_tbl.split(":")
        status = mongo_libs.ins_doc(mongo_cfg, dbn, tbl, data)

        if not status[0]:
            print("Insert error:  %s" % (status[1]))

    if json_fmt:
        jdata = json.dumps(data, indent=indent)
        _process_json(jdata, ofile, mail, mode, no_std)

    else:
        err_flag, err_msg = gen_libs.print_dict(data, ofile=ofile,
                                                no_std=no_std, mode=mode)

        if err_flag:
            print(err_msg)

        if mail:
            convert_dict(data, mail)


def _process_json(jdata, ofile, mail, mode, no_std):

    """Function:  _process_json

    Description:  Process JSON formatted data.  Private function for
        mysql_stat_run.

    Arguments:
        (input) jdata -> JSON formatted dictionary data.
        (input) ofile -> Name of output file.
        (input) mail -> Mail class instance.
        (input) mode -> File write mode.
        (input) no_std -> Suppress standard out.

    """

    if ofile:
        gen_libs.write_file(ofile, mode, jdata)

    if not no_std:
        gen_libs.print_data(jdata)

    if mail:
        mail.add_2_msg(jdata)


def mysql_stat(server, args_array, **kwargs):

    """Function:  mysql_stat

    Description:  Setup for processing the mysql statistics and loop on getting
        the MySQL statistics based on count and interval options.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            class_cfg -> Mongo server configuration.

    """

    global SUBJ_LINE

    args_array = dict(args_array)
    ofile = args_array.get("-o", False)
    db_tbl = args_array.get("-i", False)
    json_fmt = args_array.get("-j", False)
    no_std = args_array.get("-z", False)
    mode = "w"
    indent = 4
    mail = None

    if args_array.get("-a", False):
        mode = "a"

    if args_array.get("-f", False):
        indent = None

    if args_array.get("-t", None):
        mail = gen_class.setup_mail(args_array.get("-t"),
                                    subj=args_array.get("-s", SUBJ_LINE))

    # List of performance statistics to be checked.
    perf_list = ["indb_buf_data", "indb_buf_tot", "indb_buf_data_pct",
                 "indb_buf_drty", "max_use_conn", "uptime_flush",
                 "binlog_disk", "binlog_use", "binlog_tot", "indb_buf_wait",
                 "indb_log_wait", "indb_lock_avg", "indb_lock_max",
                 "indb_buf_read", "indb_buf_reqt", "indb_buf_read_pct",
                 "indb_buf_ahd", "indb_buf_evt", "indb_buf_evt_pct",
                 "indb_buf_free", "crt_tmp_tbls", "cur_conn", "uptime",
                 "indb_buf", "indb_log_buf", "max_conn"]

    # Loop iteration based on the -n option.
    for item in range(0, int(args_array["-n"])):
        mysql_stat_run(server, perf_list, db_tbl=db_tbl, ofile=ofile,
                       json_fmt=json_fmt, no_std=no_std, mode=mode,
                       indent=indent, mail=mail, **kwargs)

        # Append to file after first loop.
        mode = "a"

        # Do not sleep on the last loop.
        if item != int(args_array["-n"]) - 1:
            time.sleep(float(args_array["-b"]))

    if mail:
        mail.send_mail(use_mailx=args_array.get("-u", False))


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.

    """

    mongo = None
    args_array = dict(args_array)
    func_dict = dict(func_dict)
    server = mysql_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mysql_class.Server)
    server.connect(silent=True)

    if server.conn_msg and not args_array.get("-w", False):
        print("run_program:  Error encountered on server(%s):  %s" %
              (server.name, server.conn_msg))

    elif not server.conn_msg:
        if args_array.get("-m", False):
            mongo = gen_libs.load_module(args_array["-m"], args_array["-d"])

        # Call function(s) - intersection of command line and function dict.
        for opt in set(args_array.keys()) & set(func_dict.keys()):
            func_dict[opt](server, args_array, class_cfg=mongo, **kwargs)

        mysql_libs.disconnect(server)


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        file_chk_list -> contains the options which will have files included.
        file_crt_list -> contains options which require files to be created.
        func_dict -> dictionary list for the function calls or other options.
        opt_def_dict -> contains options with their default values.
        opt_con_req_list -> contains the options that require other options.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains options that are required for the program.
        opt_val_list -> contains options which require values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    cmdline = gen_libs.get_inst(sys)
    dir_chk_list = ["-d"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-S": mysql_stat}
    opt_def_dict = {"-i": "sysmon:mysql_perf", "-n": "1", "-b": "1"}
    opt_con_req_list = {"-i": ["-m", "-j"], "-s": ["-t"], "-u": ["-t"]}
    opt_multi_list = ["-s", "-t"]
    opt_req_list = ["-c", "-d", "-b", "-n"]
    opt_val_list = ["-c", "-d", "-b", "-i", "-m", "-n", "-o", "-s", "-t", "-y"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list,
                                       opt_def_dict, multi_val=opt_multi_list)

    # Add required default options and values to argument dictionary.
    args_array = arg_parser.arg_add_def(args_array, opt_def_dict, opt_req_list)

    if not gen_libs.is_pos_int(int(args_array["-b"])):
        args_array["-b"] = "1"

    if not gen_libs.is_pos_int(int(args_array["-n"])):
        args_array["-n"] = "1"

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                       file_crt_list):

        try:
            proglock = gen_class.ProgramLock(cmdline.argv,
                                             args_array.get("-y", ""))
            run_program(args_array, func_dict)
            del proglock

        except gen_class.SingleInstanceException:
            print("WARNING:  lock in place for mysql_perf with id of: %s"
                  % (args_array.get("-y", "")))


if __name__ == "__main__":
    sys.exit(main())
