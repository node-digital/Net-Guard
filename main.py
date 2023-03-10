import os, sys
import modules.ratelimit as ratelimit
import modules.whitelist as whitelist
import modules.asnblock as asn
import modules.icmpblock as icmp
import modules.ipforward as ipforward
import modules.portdrop as port
import modules.ddosprot as ddos
def Clear():
    os.system("clear")


def main():
    Clear()
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
    choice = input("Enter your choice: ")
    if choice == "1":
        ratelimit.limit()
        pass
    elif choice == "2":
        whitelist.Whitelist()
        pass
    elif choice == "3":
        asn.asnblock()
        pass
    elif choice == "4":
        ipforward.forward()
        pass
    elif choice == "5":
        icmp.block()
        pass
    elif choice == "6":
        port.drop()
        pass
    elif choice == "7":
        sys.exit()
        pass
    else:
        print("Invalid. Try again.")
        main()
        
if __name__ == "__main__":
    main()