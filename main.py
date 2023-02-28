import os, sys

def Clear():
    os.system("clear")

banner = """Welcome To NetGuard - V0.1
1. Rate Limiting
2. Exit"""

banner()
choice = input("Choose An Option: ")

if choice == "1":
    import modules.ratelimit as ratelimit
    ratelimit.ratelimit()

if choice == "2":
    sys.exit()