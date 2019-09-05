# Python project for monitoring performance on a MySQL database.
# Classification (U)

# Description:
  This program is used to monitor performance on a MySQL database, to include capturing database statistical data and formatting the output of the performance report.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
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
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - mysql_lib/mysql_libs
    - mysql_lib/mysql_class
    - mongo_lib/mongo_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

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

Create MySQL configuration file.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd config
cp mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - sid = SERVER_ID

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create Mongo configuration file. (Optional:  Only required if sending results to the database.)

```
cp mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Change these entries in the Mongo setup:
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"

  * If connecting to a MySQL replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/mysql-perf/mysql_perf.py -h
```


# Testing:

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mysql_perf.py program.

### Installation:
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

Install the project using git.
```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-perf.git
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

# Unit test runs for mysql_perf.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-perf
test/unit/mysql_perf/help_message.py
test/unit/mysql_perf/main.py
test/unit/mysql_perf/mysql_stat.py
test/unit/mysql_perf/mysql_stat_run.py
test/unit/mysql_perf/run_program.py
```

### All unit testing
```
test/unit/mysql_perf/unit_test_run.sh
```

### Code coverage program
```
test/unit/mysql_perf/code_coverage.sh
```

