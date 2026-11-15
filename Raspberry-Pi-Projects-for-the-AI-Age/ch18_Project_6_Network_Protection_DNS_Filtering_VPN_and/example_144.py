import ipaddress

SERVER = {"endpoint": "home.example.net:51820",
          "public_key": "SERVER_PUBLIC_KEY",
          "dns": "10.8.0.1"}
NET = ipaddress.ip_network("10.8.0.0/24")

def next_ip(used):
    for host in NET.hosts():
        if str(host).endswith(".1"):      # the server
            continue
        if str(host) not in used:
            return str(host)
    raise RuntimeError("no free address")

def client_conf(name, private_key, ip):
    return "\n".join([
        f"# client: {name}",
        "[Interface]",
        f"PrivateKey = {private_key}",
        f"Address = {ip}/32",
        f"DNS = {SERVER['dns']}",
        "",
        "[Peer]",
        f"PublicKey = {SERVER['public_key']}",
        f"Endpoint = {SERVER['endpoint']}",
        "AllowedIPs = 0.0.0.0/0",
        "PersistentKeepalive = 25"])

def server_peer(name, public_key, ip):
    return "\n".join(["[Peer]", f"# {name}",
                      f"PublicKey = {public_key}",
                      f"AllowedIPs = {ip}/32"])

used = {"10.8.0.2"}                       # laptop exists
ip = next_ip(used)
print(client_conf("phone", "PHONE_PRIVATE_KEY", ip))
print()
print(server_peer("phone", "PHONE_PUBLIC_KEY", ip))
