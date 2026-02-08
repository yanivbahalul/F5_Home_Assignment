import requests
import sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def check_port(url, expected_status,name):
    try:
        response = requests.get(url, verify=False)
        if response.status_code == expected_status:
            print(f"{name} check passed: {response.status_code} as expected")
        else:
            print(f"{name} check failed: {response.status_code} instead of {expected_status}")
            sys.exit(1)

    except Exception as e:
        print(f"Error connecting to {name}: {e}")
        sys.exit(1)

check_port("http://nginx_servers:8080", 200, "HTTP Port 8080")
check_port("http://nginx_servers:8000", 500, "Error Port 8000")
check_port("https://nginx_servers:443", 200, "HTTPS Port 443")

print("Success")
sys.exit(0)