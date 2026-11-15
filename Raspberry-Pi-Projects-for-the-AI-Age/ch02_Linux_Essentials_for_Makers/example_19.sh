scp game.nes oscar@pi5.local:~/roms/       # to the Pi
scp oscar@pi5.local:~/logs/app.log .       # from the Pi
# sync folders
rsync -av ~/Music/ oscar@pi5.local:~/Music/
