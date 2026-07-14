from utils.banner import show_banner
from utils.menu import show_menu
from modules.network import show_network_information

show_banner()
choice = show_menu()

print(f"Pilihanmu Adalah: {choice}")

if choice == "1":
    show_network_information()