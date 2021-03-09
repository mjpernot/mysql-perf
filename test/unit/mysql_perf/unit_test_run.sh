#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
test/unit/mysql_perf/_process_json.py
test/unit/mysql_perf/convert_dict.py
test/unit/mysql_perf/help_message.py
test/unit/mysql_perf/main.py
test/unit/mysql_perf/mysql_stat.py
test/unit/mysql_perf/mysql_stat_run.py
test/unit/mysql_perf/run_program.py
