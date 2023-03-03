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

def handle_choice(choice):
    if choice == "1":
        ratelimit.limit()
    elif choice == "2":
        whitelist.Whitelist()
    elif choice == "3":
        asn.asnblock()
    elif choice == "4":
        ipforward.forward()
    elif choice == "5":
        icmp.block()
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
