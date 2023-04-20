#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
/usr/bin/python3 test/unit/mysql_perf/_process_json.py
/usr/bin/python3 test/unit/mysql_perf/convert_dict.py
/usr/bin/python3 test/unit/mysql_perf/help_message.py
/usr/bin/python3 test/unit/mysql_perf/main.py
/usr/bin/python3 test/unit/mysql_perf/mysql_stat.py
/usr/bin/python3 test/unit/mysql_perf/mysql_stat_run.py
/usr/bin/python3 test/unit/mysql_perf/run_program.py
