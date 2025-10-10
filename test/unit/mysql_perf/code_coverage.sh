#!/bin/bash
# Unit test code coverage for program module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_perf test/unit/mysql_perf/create_data_config.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/create_header.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/data_out.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/file_out.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/help_message.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/mail_out.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/main.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/mysql_stat.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/mysql_stat_run.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/run_program.py
coverage run -a --source=mysql_perf test/unit/mysql_perf/std_out.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
