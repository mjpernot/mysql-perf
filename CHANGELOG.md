# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.

## [2.5.6] - 2024-11-08
- Updated chardet==4.0.0 for Python 3
- Updated distro==1.9.0 for Python 3
- Updated protobuf==3.19.6 for Python 3
- Updated mysql-connector-python==8.0.28 for Python 3
- Updated psutil==5.9.4 for Python 3
- Updated mongo-lib to v4.3.3
- Updated mysql-lib to v5.3.8
- Updated python-lib to v3.0.7

### Deprecated
- Support for Python 2.7


## [2.5.5] - 2024-09-27
- Updated pymongo==4.1.1 for Python 3.6
- Updated simplejson==3.13.2 for Python 3
- Updated mongo-lib to v4.3.2
- Updated python-lib to v3.0.5
- Updated mysql-lib to v5.3.7


## [2.5.4] - 2024-09-10

### Changed
- config/mysql_cfg.py.TEMPLATE:  Changed cfg_file default value.


## [2.5.3] - 2024-04-23
- Updated mongo-lib to v4.3.0
- Added TLS capability for Mongo
- Set pymongo to 3.12.3 for Python 2 and Python 3.

### Changed
- Set pymongo to 3.12.3 for Python 2 and Python 3.
- config/mongo.py.TEMPLATE: Added TLS entries.
- Documentation updates.


## [2.5.2] - 2024-02-29
- Updated to work in Red Hat 8
- Updated python-lib to v3.0.3
- Updated mongo-lib to v4.2.9
- Updated mysql-lib to v5.3.4

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [2.5.1] - 2023-10-11
### Fixed
- mysql_stat: Fixed incorrect syntax for args.get_val call.


## [2.5.0] - 2023-08-23
- Upgraded python-lib to v2.10.1
- Replaced the arg_parser code with gen_class.ArgParser code.

### Changed
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- main: Removed gen_libs.get_inst call.


## [2.4.2] - 2022-11-28
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4 
- Upgraded mysql-lib to v5.3.2
- Upgraded mongo-lib to v4.2.2

### Changed     
- convert_dict: Changed from iteritems() to items() and converted the output to a list.
- Converted imports to use Python 2.7 or Python 3.


## [2.4.1] - 2022-06-27
- Upgrade mysql-connector to v8.0.22
- Upgrade mysql-libs to v5.3.1
- Upgrade mongo-libs to v4.2.1
- Upgrade python-lib to v2.9.2
- Added TLS capability

### Changed
- config/mysql_cfg.py.TEMPLATE: Added TLS version entry.
- config/mongo.py.TEMPLATE: Removed old entries.
- Documentation updates.


## [2.4.0] - 2021-09-07
- Updated to work in MySQL 8.0 environment.
- Updated to work in a SSL environment.
- Updated to use the mysql_libs v5.2.2 library.
- Updated to use gen_libs v2.8.4 library.


## [2.3.0] - 2020-07-31
- Updated to use the mysql_libs v5.0.4 library.
- Updated to use pymongo v3.8.0.
- Updated to be used in FIPS 140-2 environment.
- Updated to work with (much older) mysql.connector v1.1.6 library module.
- Validated against MySQL 5.7 environment.

### Fixed
- convert_dict:  Fixed formatting problem and printing all dictionary keys in nested dictionaries.
- config/mysql.cfg.TEMPLATE:  Point to correct socket file.
- mysql_stat:  Set file mode to append after first loop.

### Added
- Added -u option to override postfix and use mailx command.
- Added -w option to suppress printing the inital connection error.
- Added email capability to send performance reports to email addresses.
- \_process_json:  Process JSON formatted data, private function for mysql_stat_run.
- convert_dict:  Convert dictionary document to standard format and add to mail body.
- is_pos_int:  Checks to see if number is an integer and positive.

### Changed
- mysql_stat:  Set the use_mailx argument in the mail.send_mail command.
- main:  Added -u option to allow for mailx use.
- main:  Replaced is_pos_int with gen_libs.is_pos_int call.
- run_program:  Added check for -w option to ignore initial connection error.
- run_program:  Check on connection status and process accordingly.
- mysql_stat_run:  Process status return from mongo_libs.ins_doc call.
- run_program:  Replaced cmds_gen.disconnect with mysql_libs.disconnect call.
- Removed unnesscary \*\*kwargs from function parameters lists.
- config/mongo.py.TEMPLATE:  Changed configuration entry name and added a number of configuration entries.
- mysql_stat_run:  Replaced datetime call with calls to gen_libs.get_date and gen_libs.get_time.
- config/mysql_cfg.py.TEMPLATE:  Changed configuration entry name.
- mysql_stat_run:  Replaced code to process JSON data with call to \_process_json.
- mysql_stat_run:  Add to email body if email is setup.
- mysql_stat:  Setup email instance and pass to performance function.
- main:  Added -s and -t options to parsing for email capability.
- main:  Added checks for positive integers for loop and interval options.
- Documentation updates.

### Removed
- Removed lib.cmds_gen module.
- Removed is_pos_int function.
- Removed datetime module.


## [2.2.1] - 2020-05-28
### Fixed
- main: Fixed handling command line arguments from SonarQube scan finding.

### Added
- Added ProgramLock class to prevent multiple runs at the same time.
- Added -f option to allow for flattening of JSON structure in output.
- Added -a option to allow for append of data to an existing output file.

### Changed
- mysql_stat, run_program, mysql_stat_run:  Changed variable name to standard naming convention.
- main:  Added ProgramLock class to implement program locking.
- mysql_stat:  Added indentation option for JSON structure flattening.  Default is set to 4.
- mysql_stat:  Added file mode option to writing data to a file.  Default is write.
- mysql_stat:  Converted "-s" to "-z" to avoid confusion.
- mysql_stat:  Converted mysql_stat_run arguments from positional to kwargs.
- mysql_stat_run:  Refactored function to streamline the process, include append write mode, flattening of JSON, and moved a number of arguments to kwargs.
- config/mongo.py.TEMPLATE:  Changed format.
- config/mysql.cfg.TEMPLATE:  Changed format.
- config/mysql_cfg.py.TEMPLATE:  Changed format.
- Documentation updates.


## [2.2.0] - 2019-09-05
### Fixed
- mysql_stat, run_program, mysql_stat_run:  Fixed problem with mutable default arguments issue.

### Changed
- mysql_stat_run: Replaced mongo_libs.json_2_out with internal code.
- main:  Refactored "if" statements.
- mysql_stat_run:  Changed JSON dictionary keys to PascalCase.
- mysql_stat, run_program, mysql_stat_run:  Changed variable to standard naming convention.


## [2.1.1] - 2018-12-03
### Fixed
- mysql_stat_run:  Changed function parameter mutable argument default to immutable argument default.


## [2.1.0] - 2018-09-13
### Changed
- run_program:  Changed "cmds_gen.Disconnect" to "cmds_gen.disconnect" call.


## [2.0.0] - 2018-05-22
Breaking Change

### Changed
- Changed "mongo_libs", "mysql_libs", "gen_libs", "arg_parser" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.


## [1.3.0] - 2018-04-27
### Changed
- Changed "cmds_mongo" to "mongo_libs" module reference.
- Changed "commands" to "mysql_libs" module reference.
- Changed "server" to "mysql_class" module reference.

### Added
- Added single-source version control.


## [1.2.0] - 2017-08-15
### Changed
- Change single quotes to double quotes.
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.


## [1.1.0] - 2017-08-15
### Changed
- Convert program to use local libraries from ./lib directory.
- Mysql_Stat_Run:  Add call to insert data into Mongo database.
- Mysql_Stat_Run:  Replace call to Dict_Out with Print_Dict and error checking.


## [1.0.0] - 2016-05-23
- Initial creation.

