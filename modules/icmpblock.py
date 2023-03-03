import os

def block_icmp():
    # Block all ICMP traffic
    os.system("iptables -A INPUT -p icmp -j DROP")
    
    # Save the new rules to iptables configuration
    os.system("iptables-save > /etc/iptables/rules.v4")
    
    print("ICMP traffic has been blocked.")
