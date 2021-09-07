# Python project for monitoring performance on a MySQL database.
# Classification (U)

# Description:
  Used to monitor performance on a MySQL database, to include capturing database statistical data and formatting the output of the performance report.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
    - FIPS Environment
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit


# Features:
  * Capture database performance statistical data.
  * Convert performance output into a number of formats or send to a database.


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip
    - python-devel

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - lib/gen_class
    - mysql_lib/mysql_libs
    - mysql_lib/mysql_class
    - mongo_lib/mongo_libs

  * FIPS Environment
    If operating in a FIPS 104-2 environment, this package will require at least a minimum of pymongo==3.8.0 or better.  It will also require a manual change to the auth.py module in the pymongo package.  See below for changes to auth.py.
    - Locate the auth.py file python installed packages on the system in the pymongo package directory.
    - Edit the file and locate the \_password_digest function.
    - In the \_password_digest function there is an line that should match: "md5hash = hashlib.md5()".  Change it to "md5hash = hashlib.md5(usedforsecurity=False)".
    - Lastly, it will require the configuration file entry auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.


# Installation:

Install the project using git.
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-perf.git
```

Install/upgrade system modules.

```
cd mysql-perf
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create MySQL configuration file.  Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOST_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "MYSQL_DIRECTORY/mysqld.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

```
cd config
cp mysql_cfg.py.TEMPLATE mysql_cfg.py
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.  Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
  * Note:  socket use is only required to be set in certain conditions when connecting using localhost.
    - password="PASSWORD"
    - socket="MYSQL_DIRECTORY/mysql.sock"

```
cp mysql.cfg.TEMPLATE mysql.cfg
vim mysql.cfg
chmod 600 mysql.cfg
```

Create Mongo configuration file.  Make the appropriate change to the environment.
  * Only required if sending results to the database.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOST_IP"
    - name = "HOST_NAME"

  * Change these entries only if required:
    - port = 27017
    - conf_file = None
    - auth = True
    - auth_db = "admin"
    - auth_mech = "SCRAM-SHA-1"
    - use_arg = True
    - use_uri = False

  * If connecting to a Mongo replica set:
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
cp mongo.py.TEMPLATE mongo.py
vim mongo.py
chmod 600 mongo.py
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
{Python_Project}/mysql-perf/mysql_perf.py -h
```


# Testing:

# Unit Testing:

Install the project using the procedures in the Installation section.

### Testing:

```
cd {Python_Project}/mysql-perf
test/unit/mysql_perf/unit_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/mysql-perf
test/unit/mysql_perf/code_coverage.sh
```

