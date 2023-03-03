import os
import sys
import modules.ratelimit as ratelimit
import modules.whitelist as whitelist
import modules.asnblock as asn
import modules.icmpblock as icmp
import modules.ipforward as ipforward
import modules.portdrop as port
import modules.ddosprot as ddos

def clear_screen():
    os.system("clear")

def print_banner():
    banner = """Welcome To Net-Guard
    Please select a feature to use:
    1. Rate Limiting
    2. IP Whitelisting
    3. ASN blocking
    4. IP Forwarding
    5. Disable ICMP
    6. Drop Not Needed Ports
    7. Exit"""
    print(banner)

def handle_rate_limit():
    interface = input("Enter the network interface to rate limit (e.g., eth0): ")
    rate = input("Enter the rate limit in kilobits per second (e.g., 1000): ")
    ratelimit.rate_limit(interface, rate)

def handle_ip_forward():
    src_ip = input("Enter the source IP address to forward (e.g., 192.168.1.1): ")
    dst_ip = input("Enter the destination IP address to forward (e.g., 10.0.0.1): ")
    port = input("Enter the port to forward (e.g., 80): ")
    ipforward.ip_forward(src_ip, dst_ip, port)

def handle_choice(choice):
    if choice == "1":
        handle_rate_limit()
    elif choice == "2":
        whitelist.Whitelist()
    elif choice == "3":
        asn.asnblock()
    elif choice == "4":
        handle_ip_forward()
    elif choice == "5":
        icmp.icmp_block()
    elif choice == "6":
        port.drop()
    elif choice == "7":
        sys.exit()
    else:
        print("Invalid. Try again.")
        main()

def main():
    clear_screen()
    print_banner()
    choice = input("Enter your choice: ")
    handle_choice(choice)

if __name__ == "__main__":
    main()
