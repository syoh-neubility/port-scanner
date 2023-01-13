#!/usr/bin/python3
import sys
from socket import socket
from socket import timeout

def scan_port(host: str, port: int):
    s = socket()
    s.settimeout(5)
    try:
        s.connect((host, port))
    except timeout as err:
        print("Time Out!")
        return False

    except Exception as err:
        print("ERROR: ", err)
        return False
    else:
        return True


if __name__ == "__main__":
    host, port = sys.argv[1:]
    print(f"scanning {host}:{port}...")
    port_open = scan_port(host, int(port))
    print("OPEN" if port_open else "CLOSED")