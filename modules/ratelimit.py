import os

def limit():
    print("Rate Limiting TCP Connections")
    #Rate Limiting TCP
    os.system("ufw limit 1:65535/tcp")
    os.system("iptables -t mangle -I PREROUTING -p tcp -m conntrack --ctstate NEW -j DROP")
    os.system("iptables -t mangle -I PREROUTING -p tcp -m conntrack --ctstate NEW -m hashlimit --hashlimit-name portlimit --hashlimit-mode srcip --hashlimit-srcmask 32 --hashlimit-upto 23/sec --hashlimit-burst 30 --hashlimit-htable-expire 60000 -j ACCEPT")
    #Rate Limiting UDP
    print("Rate Limiting UDP connections")
    os.system("iptables -t mangle -I PREROUTING -p udp -m conntrack --ctstate NEW -j DROP")
    os.system("iptables -t mangle -I PREROUTING -p udp -m conntrack --ctstate NEW -m hashlimit --hashlimit-name portlimit --hashlimit-mode srcip --hashlimit-srcmask 32 --hashlimit-upto 23/sec --hashlimit-burst 30 --hashlimit-htable-expire 60000 -j ACCEPT")