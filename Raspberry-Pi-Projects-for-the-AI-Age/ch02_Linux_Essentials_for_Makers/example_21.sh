# minute hour day month weekday  command
# every day at 03:00
0 3 * * *   /home/oscar/bin/backup.sh
# every 10 minutes
*/10 * * * * /home/oscar/bin/check_temp.py
# Mondays at 09:00
0 9 * * 1   /home/oscar/bin/weekly_report.sh
