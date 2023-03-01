import os

def drop():
    os.system("""iptables -I PREROUTING -t raw -p tcp --dport 1:65535 -m string --algo kmp --hex-string '|ff ff ff ff fd|' -j DROP
iptables -I PREROUTING -t raw -p tcp --dport 1:65535 -m string --algo kmp --hex-string '|ff ff ff ff fe|' -j DROP
iptables -I PREROUTING -t raw -p tcp --dport 1:65535 -m string --algo kmp --hex-string '|00 ff ff ff ff fd|' -j DROP
iptables -I PREROUTING -t raw -p tcp --dport 1:65535 -m string --algo kmp --hex-string '|00 ff ff ff ff fe|' -j DROP
iptables -I PREROUTING -t raw -p udp --dport 1:65535 -m string --algo kmp --hex-string '|ff ff ff ff fd|' -j DROP
iptables -I PREROUTING -t raw -p udp --dport 1:65535 -m string --algo kmp --hex-string '|ff ff ff ff fe|' -j DROP
iptables -I PREROUTING -t raw -p udp --dport 1:65535 -m string --algo kmp --hex-string '|00 ff ff ff ff fd|' -j DROP
iptables -I PREROUTING -t raw -p udp --dport 1:65535 -m string --algo kmp --hex-string '|00 ff ff ff ff fe|' -j DROP
iptables -A INPUT -p udp -m multiport --dports 135,137,138,139,445,1433,1434 -j DROP
iptables -A INPUT -p tcp -m multiport --dports 135,137,138,139,445,1433,1434 -j DROP
iptables -A INPUT -p udp -m multiport --sports 135,137,138,139,445,1433,1434 -j DROP
iptables -A INPUT -p tcp -m multiport --sports 135,137,138,139,445,1433,1434 -j DROP 
iptables -A INPUT -p udp -m multiport --dports 853,4433,4740,5349,5684,5868,6514,6636,8232,10161 -j DROP
iptables -A INPUT -p tcp -m multiport --dports 853,4433,4740,5349,5684,5868,6514,6636,8232,10161 -j DROP
iptables -A INPUT -p udp -m multiport --sports 853,4433,4740,5349,5684,5868,6514,6636,8232,10161 -j DROP
iptables -A INPUT -p tcp -m multiport --sports 853,4433,4740,5349,5684,5868,6514,6636,8232,10161 -j DROP
iptables -A INPUT -p udp -m multiport --dports 10162,12346,12446,12546,12646,12746,12846,12946,13046 -j DROP 
iptables -A INPUT -p tcp -m multiport --dports 10162,12346,12446,12546,12646,12746,12846,12946,13046 -j DROP
iptables -A INPUT -p udp -m multiport --sports 10162,12346,12446,12546,12646,12746,12846,12946,13046 -j DROP
iptables -A INPUT -p tcp -m multiport --sports 10162,12346,12446,12546,12646,12746,12846,12946,13046 -j DROP
iptables -A INPUT -p udp -m multiport --dports 1645,1812,2049,3283,2302,6481,17185,26000,26001,26002 -j DROP
iptables -A INPUT -p tcp -m multiport --dports 1645,1812,2049,3283,2302,6481,17185,26000,26001,26002 -j DROP
iptables -A INPUT -p udp -m multiport --sports 1645,1812,2049,3283,2302,6481,17185,26000,26001,26002 -j DROP
iptables -A INPUT -p tcp -m multiport --sports 1645,1812,2049,3283,2302,6481,17185,26000,26001,26002 -j DROP
iptables -A INPUT -p udp -m multiport --dports 26003,26004,27960,27961,27962,27963,27964,30720,30721 -j DROP
iptables -A INPUT -p tcp -m multiport --dports 26003,26004,27960,27961,27962,27963,27964,30720,30721 -j DROP
iptables -A INPUT -p udp -m multiport --sports 26003,26004,27960,27961,27962,27963,27964,30720,30721 -j DROP
iptables -A INPUT -p tcp -m multiport --sports 26003,26004,27960,27961,27962,27963,27964,30720,30721 -j DROP
iptables -A INPUT -p udp -m multiport --dports 30722,30723,30724,44400,3784,64378,8767,11211,1645,1812,520 -j DROP
iptables -A INPUT -p tcp -m multiport --dports 30722,30723,30724,44400,3784,64378,8767,11211,1645,1812,520 -j DROP
iptables -A INPUT -p udp -m multiport --sports 30722,30723,30724,44400,3784,64378,8767,11211,1645,1812,520 -j DROP
iptables -A INPUT -p tcp -m multiport --sports 30722,30723,30724,44400,3784,64378,8767,11211,1645,1812,520 -j DROP
iptables-save""")