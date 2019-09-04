# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.2.0] - 2019-09-04
### Fixed
- run_program:  Fixed problem with mutable default arguments issue.
- mysql_stat:  Fixed problem with mutable default arguments issue.
- mysql_stat_run:  Fixed problem with mutable default arguments issue.

### Changed
- main:  Refactored "if" statements.
- mysql_stat_run:  Changed JSON dictionary keys to CamelCase.
- mysql_stat_run:  Changed variable to standard naming convention.
- mysql_stat:  Changed variable to standard naming convention.
- run_program:  Changed variables to standard naming convention.


## [2.1.1] - 2018-12-03
### Fixed
- mysql_stat_run:  Changed function parameter mutable argument default to immutable argument default.


## [2.1.0] - 2018-09-13
### Changed
- run_program:  Changed "cmds_gen.Disconnect" to "cmds_gen.disconnect" call.


## [2.0.0] - 2018-05-22
Breaking Change

### Changed
- Changed "mongo_libs" calls to new naming schema.
- Changed "mysql_libs" calls to new naming schema.
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
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

