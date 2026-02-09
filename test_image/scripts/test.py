import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# check port function
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

print("Starting port tests...")
check_port("http://nginx_servers:8080", 200, "HTTP Port 8080")
check_port("http://nginx_servers:8000", 500, "Error Port 8000")
check_port("https://nginx_servers:443", 200, "HTTPS Port 443")


# check rate limit
blocked_count = 0
total_requests = 20

print("Starting rate limit test...")
for i in range(total_requests):
    try:
        res = requests.get("https://nginx_servers:443", verify=False)

        if res.status_code == 503:
            blocked_count += 1
            print(f"Request {i+1}: Blocked (503)")

    except:
        pass

if blocked_count > 0:
    print(f"Rate limit test passed: {blocked_count} requests were blocked as expected")
    sys.exit(0)
else:
    print("Rate limit test failed: No requests were blocked")
    sys.exit(1)

print("Success")
sys.exit(0)