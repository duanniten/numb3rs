import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip : str):
    if re.search(r"^((25[0-5]|2[0-4][0-9]|(1[0-9]{2})|[0-9]{1,2})\.){3}"
                    r"(25[0-5]|2[0-4][0-9]|(1[0-9]{2})|[0-9]{1,2})$", ip):
        return True
    return False

if __name__ == "__main__":
    main()