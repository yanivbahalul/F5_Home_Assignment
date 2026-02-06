import requests
import sys

#port 8080 check
try:
    f_response = requests.get("http://nginx_servers:8080")
    if f_response.status_code == 200:
        print("Port 8080, returning 200 as expected")
    else:
        print(f"Port 8080 Failed: {f_response.status_code}")
        sys.exit(1) 

except Exception as e:
    print(f"Error connecting to 8080: {e}")
    sys.exit(1)


#port 8000 check
try:
    s_response = requests.get("http://nginx_servers:8000")
    if s_response.status_code == 500:
        print("Port 8000, returning 500 as expected")
    else:
        print(f"Port 8000 Failed: {s_response.status_code}")
        sys.exit(1) 

except Exception as e:
    print(f"Error connecting to 8000: {e}")
    sys.exit(1)

print("Success")
sys.exit(0)