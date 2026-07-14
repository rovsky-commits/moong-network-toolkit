import socket
import getpass
import platform
import requests

def get_hostname():
    return socket.gethostname()

def get_username():
    return getpass.getuser()

def get_operating_system():
    return platform.system()

def get_os_release():
    return platform.release()

def get_os_version():
    return platform.version()

def get_architecture():
    return platform.architecture()[0]

def get_machine_type():
    return platform.machine()

def get_processor_info():
    return platform.processor()

def get_python_version():
    return platform.python_version()

def get_local_ip_address():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except socket.error:
        return "Unable to retrieve IP address"
    
def get_public_ip_address():
    try:
        response = requests.get(
            "https://api.ipify.org?format=json",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()["ip"]

        return "Unavailable"

    except requests.RequestException:
        return "Unavailable"
    
def show_network_information():
    
    hostname = get_hostname()
    ip_address = get_local_ip_address()
    username = get_username()
    os_name = get_operating_system()
    os_release = get_os_release()
    os_version = get_os_version()
    architecture = get_architecture()
    machine_type = get_machine_type()
    processor_info = get_processor_info()
    python_version = get_python_version()
    public_ip_address = get_public_ip_address()

    print("=" * 50)
    print("         NETWORK INFORMATION")
    print("=" * 50)
    print(f"Hostname          : {hostname}")
    print(f"Local IP Address  : {ip_address}")
    print(f"Username          : {username}")
    print(f"Operating System  : {os_name} {os_version}")
    print(f"Architecture      : {architecture}")
    print(f"Machine Type      : {machine_type}")
    print(f"Processor         : {processor_info}")
    print(f"Python Version    : {python_version}")
    print(f"Public IP Address : {public_ip_address}")