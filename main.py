from lib import fetch_ip
def main_func():
    """" The main function of my-project """
    """ Calls function fetch_ip() for fetching IP-address and output result in terminal """
    ip_address = fetch_ip()
    print("Your IP address is:", ip_address,"!")
main_func()