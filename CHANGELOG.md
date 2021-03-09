# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.3.0] - 2020-07-31
- Updated to use the mysql_libs v5.0.2 library.
- Updated to use pymongo v3.8.0.

### Fixed
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
- mysql_stat_run:  Changed JSON dictionary keys to CamelCase.
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

