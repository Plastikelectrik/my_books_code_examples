cat notes.txt          # print a whole file
# scroll through a long file (q quits)
less /var/log/syslog
head -n 20 file.txt    # first 20 lines
tail -n 20 file.txt    # last 20 lines
tail -f logfile.log    # follow a file as it grows
grep "error" app.log   # show lines that contain "error"
