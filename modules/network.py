import socket
import getpass
import platform

def show_network_information():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    username = getpass.getuser()
    os_name = platform.system()
    python_version = platform.python_version()
    
    print("\n========== NETWORK INFORMATION ==========")
    print(f"Hostname          : {hostname}")
    print(f"Local IP Address  : {ip_address}")
    print(f"Username          : {username}")
    print(f"Operating System  : {os_name}")
    print(f"Python Version    : {python_version}")
    print("=" * 40)