import sys
import threading
import frida

done = threading.Event()
pid = frida.spawn(sys.argv[2:])
session = frida.attach(pid)
session.on("detached", lambda *a: done.set())
with open(sys.argv[1]) as f:
    script = session.create_script(f.read())
script.load()
frida.resume(pid)
done.wait(10)
