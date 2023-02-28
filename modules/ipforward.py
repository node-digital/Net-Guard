import os

def forward():
    ip = input("Destination IP: ")
    port = input("Destination Port: ")
    print(f"Forwarding All Traffic On Port {port} To {ip}:{port}")
    os.system(f"sysctl -w net.ipv4.ip_forward=1")
    os.system(f"iptables -A FORWARD -i eth0 -j ACCEPT")
    os.system(f"iptables -A FORWARD -o eth0 -j ACCEPT")
    os.system(f"iptables -I FORWARD -i eth0 -p tcp --dport {port} -j ACCEPT"),
    os.system(f"iptables -t nat -A PREROUTING -p tcp --dport {port} -j DNAT --to-destination {ip}:{port}")
    os.system(f"iptables -t nat -A POSTROUTING -j MASQUERADE")