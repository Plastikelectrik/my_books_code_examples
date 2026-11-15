import subprocess

cmd = ["vcgencmd", "get_throttled"]
out = subprocess.run(cmd, capture_output=True,
                     text=True).stdout
# the output looks like "throttled=0x0"
value = int(out.strip().split("=")[1], 16)
print(decode_throttled(value) or "all good")
