import os


def Whitelist():
    ip = input("Enter Your Personal IP Address: ")
    print("Whitelisting IP Address!")
    os.system(f"""iptables -I INPUT -p tcp --dport 22 -s {ip} -j ACCEPT
              iptables -A INPUT -p tcp --dport 22 -j DROP
              iptables -I INPUT -p udp --dport 1194 -s {ip} -j ACCEPT
              iptables -A INPUT -p udp --dport 1194 -j DROP
              iptables -I INPUT -p tcp --dport 1194 -s {ip} -j ACCEPT
              iptables -A INPUT -p tcp --dport 1194 -j DROP
              iptables -I INPUT -p tcp --dport 443 -s {ip} -j ACCEPT
              iptables -A INPUT -p tcp --dport 443 -j DROP
              iptables -I INPUT -p udp --dport 443 -s {ip} -j ACCEPT
              iptables -A INPUT -p udp --dport 443 -j DROP
              iptables -I INPUT -p tcp --dport 80 -s {ip} -j ACCEPT
              iptables -A INPUT -p tcp --dport 80 -j DROP
              iptables -I INPUT -p udp --dport 80 -s {ip} -j ACCEPT
              iptables -A INPUT -p udp --dport 80 -j DROP
              iptables -I INPUT -p tcp --dport 53 -s {ip} -j ACCEPT
              iptables -A INPUT -p tcp --dport 53 -j DROP
              iptables -I INPUT -p udp --dport 53 -s {ip} -j ACCEPT
              iptables -A INPUT -p udp --dport 53 -j DROP
              iptables -I INPUT -p tcp --dport 21 -s {ip} -j ACCEPT
              iptables -A INPUT -p udp --dport 21 -j DROP
              iptables -I INPUT -p tcp --dport 21 -s {ip} -j ACCEPT
              iptables -A INPUT -p tcp --dport 21 -j DROP
              iptables-save > rules.v4
            """)