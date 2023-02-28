import os


def Whitelist():
    print("""    1. Whitelist Server
    2. Whitelist Server And Web""")
    choices = input("Select A Choice: ")
    if choices == "1":
        ip = input("Enter Your Personal IP Address: ")
        print("Whitelisting Server!")
        os.system(f"""iptables -I INPUT -p tcp --dport 22 -s {ip} -j ACCEPT
                  iptables -A INPUT -p tcp --dport 22 -j DROP
                  iptables -I INPUT -p udp --dport 1194 -s {ip} -j ACCEPT
                  iptables -A INPUT -p udp --dport 1194 -j DROP
                  iptables -I INPUT -p tcp --dport 1194 -s {ip} -j ACCEPT
                  iptables -A INPUT -p tcp --dport 1194 -j DROP
                  iptables -A INPUT -p tcp --dport 53 -j DROP
                  iptables -I INPUT -p udp --dport 53 -s {ip} -j ACCEPT
                  iptables -A INPUT -p udp --dport 53 -j DROP
                  iptables -I INPUT -p tcp --dport 21 -s {ip} -j ACCEPT
                  iptables -A INPUT -p udp --dport 21 -j DROP
                  iptables -I INPUT -p tcp --dport 21 -s {ip} -j ACCEPT
                  iptables -A INPUT -p tcp --dport 21 -j DROP
                  iptables -I INPUT -p udp --dport 80 -s {ip} -j ACCEPT
                  iptables -A INPUT -p udp --dport 80 -j DROP
                  iptables-save > rules.v4""")
    elif choices == "2":
        ip = input("Enter Your Personal IP Address: ")
        print("Whitelisting Server And Web!")
        os.system("""iptables -I INPUT -p tcp --dport 443 -s {ip} -j ACCEPT
                  iptables -A INPUT -p tcp --dport 443 -j DROP
                  iptables -I INPUT -p udp --dport 443 -s {ip} -j ACCEPT
                  iptables -A INPUT -p udp --dport 443 -j DROP
                  iptables -I INPUT -p tcp --dport 80 -s {ip} -j ACCEPT
                  iptables -A INPUT -p tcp --dport 80 -j DROP
                  iptables -I INPUT -p udp --dport 80 -s {ip} -j ACCEPT
                  iptables -A INPUT -p udp --dport 80 -j DROP
                  iptables -I INPUT -p tcp --dport 53 -s {ip} -j ACCEPT
                  iptables -I INPUT -p tcp --dport 22 -s {ip} -j ACCEPT
                  iptables -A INPUT -p tcp --dport 22 -j DROP
                  iptables -I INPUT -p udp --dport 1194 -s {ip} -j ACCEPT
                  iptables -A INPUT -p udp --dport 1194 -j DROP
                  iptables -I INPUT -p tcp --dport 1194 -s {ip} -j ACCEPT
                  iptables -A INPUT -p tcp --dport 1194 -j DROP
                  iptables -A INPUT -p tcp --dport 53 -j DROP
                  iptables -I INPUT -p udp --dport 53 -s {ip} -j ACCEPT
                  iptables -A INPUT -p udp --dport 53 -j DROP
                  iptables -I INPUT -p tcp --dport 21 -s {ip} -j ACCEPT
                  iptables -A INPUT -p udp --dport 21 -j DROP
                  iptables -I INPUT -p tcp --dport 21 -s {ip} -j ACCEPT
                  iptables -A INPUT -p tcp --dport 21 -j DROP
                  iptables-save > rules.v4""")
