#!/bin/bash
# Print a short health report of the Raspberry Pi
echo "=== $(hostname) report: $(date) ==="
echo "Uptime : $(uptime -p)"
echo "Temp   : $(vcgencmd measure_temp)"
echo "Power  : $(vcgencmd get_throttled)"
echo "Memory : $(free -h | awk '/Mem/{print $3"/"$2}')"
echo "Disk   : $(df -h / | awk 'NR==2{print $3"/"$2}')"
echo "IP     : $(hostname -I)"
