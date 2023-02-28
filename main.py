import os, sys
import modules.ratelimit as ratelimit



def Clear():
    os.system("clear")


def main():
    Clear()
    banner = """Welcome To Net-Guard
    Please select a feature to use:
    1. Rate Limiting
    2. IP Whitelisting
    3. ASN blocking
    4. IP-range-blocking
    5. Block Botnet Packets
    6. Exit"""
    print(banner)
    choice = input("Enter your choice: ")
    if choice == "1":
        ratelimit.limit()
        pass
    elif choice == "2":
        # Call the Rate limiting function
        pass
    elif choice == "3":
        # Call the ASN blocking function
        pass
    elif choice == "4":
        # Call the IP range blocking function
        pass
    elif choice == "5":
        # Call the IP range blocking function
        pass
    elif choice == "6":
        sys.exit()
        pass
    else:
        print("Invalid. Try again.")