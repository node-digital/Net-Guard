import os

def block():
    print("Blocking ICMP")
    os.system("""sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
              sudo iptables -A OUTPUT -p icmp --icmp-type echo-reply -j DROP
              iptables-save > rules.v4""")