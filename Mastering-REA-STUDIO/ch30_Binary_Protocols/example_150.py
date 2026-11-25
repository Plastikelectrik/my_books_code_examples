from mitmproxy import tcp

LOG = "kb-messages.txt"


class Recorder:
    def tcp_message(self, flow: tcp.TCPFlow) -> None:
        msg = flow.messages[-1]
        side = "C" if msg.from_client else "S"
        with open(LOG, "a") as f:
            f.write(f"{side} {msg.content.hex()}\n")


addons = [Recorder()]
