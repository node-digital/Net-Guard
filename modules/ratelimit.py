import os

def rate_limit(interface, rate):
    # Define the command to rate limit UDP traffic
    udp_command = f"sudo tc qdisc add dev {interface} root handle 1: cbq avpkt 1000 bandwidth 100Mbit"
    udp_command += f" allot 1514 cell 8 maxburst 20 minburst 5"
    udp_command += f" weight 10Kbit minidle 5 prio 1 maxrate {rate}Kbit"

    # Define the command to rate limit TCP traffic
    tcp_command = f"sudo tc qdisc add dev {interface} root handle 2: cbq avpkt 1000 bandwidth 100Mbit"
    tcp_command += f" allot 1514 cell 8 maxburst 20 minburst 5"
    tcp_command += f" weight 90Kbit minidle 5 prio 2 maxrate {rate}Kbit"

    # Run the commands to rate limit UDP and TCP traffic
    os.system(udp_command)
    os.system(tcp_command)
