import os

def ip_forward(source_ip, destination_ip, port):
    os.system("sudo iptables -t nat -A PREROUTING -p tcp -d {source_ip} --dport {port} -j DNAT --to-destination {destination_ip}:{port}")
    os.system("sudo iptables -t nat -A POSTROUTING -j MASQUERADE")
    print("IP forwarding set up successfully.")
