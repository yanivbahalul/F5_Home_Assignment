# Nginx and Python Project

This project runs a web server (Nginx) on Ubuntu and tests it automatically with Python.

## How to Run

1.  **Get the code:**
    ```bash
    git clone [https://github.com/yanivbahalul/F5_Home_Assignment](https://github.com/yanivbahalul/F5_Home_Assignment)
    cd F5_Home_Assignment
    ```

2.  **Start the project:**
    Run this command to build and start everything:
    ```bash
    docker-compose up --build
    ```
    * The server will start.
    * The test script will run and check the server.

3.  **Stop:**
    ```bash
    docker-compose down
    ```

## How it Works

* **The Server:** Runs Nginx on Ubuntu.
    * Port **8080**: Shows the website via HTTP (Returns 200 OK).
    * Port **443**: Shows the website via **HTTPS** (Secured with a self-signed certificate).
    * Port **8000**: Shows an error (Returns 500 Error) for testing purposes.
* **The Test:** A Python script checks connectivity to all ports (HTTP & HTTPS) and validates that the error page and rate limiting work as expected.

## Decisions & Trade-offs

* **Why Ubuntu?**
    The instructions required using `ubuntu:24.04` as the base image.
* **Size Optimization:**
    Ubuntu is a large image (bigger than Alpine). To make it **as small as possible**, I added a command to delete temporary installation files (`rm -rf /var/lib/apt/lists/*`) inside the Dockerfile.
* **Security (HTTPS):**
    I used OpenSSL to generate a self-signed certificate during the build process to enable HTTPS support on port 443.
* **GitHub Actions:**
    The project uses GitHub Actions to build and test the code automatically every time I push changes.

## Rate Limiting Configuration

This project implements a rate limiting mechanism to protect the server from abuse and DoS attacks.

### How it Works
The rate limiting is handled by Nginx using the `limit_req_module`.
* **Zone Definition:** Nginx allocates a shared memory zone (`limit_rule`) to track the IP addresses of incoming requests.
* **Rate:** The server allows a maximum of **5 requests per second** (`5r/s`) from a single IP address.
* **Burst & Nodelay:** To allow legitimate traffic spikes (like loading a page with multiple assets), we allow a **burst of 10 requests**. The `nodelay` directive ensures these burst requests are processed immediately without waiting, provided they fit within the burst limit.
* **Exceeding the Limit:** If a client exceeds the rate and the burst buffer, Nginx returns a **503 Service Unavailable** error.

### How to Change the Rate Limit Threshold
To change the allowed number of requests per second:

1.  Open the configuration file: `nginx_image/servers.conf`.
2.  Locate the first line defining the zone:
    ```nginx
    limit_req_zone $binary_remote_addr zone=limit_rule:5m rate=5r/s;
    ```
3.  Change the `rate` value. For example, to allow 20 requests per second:
    ```nginx
    rate=20r/s
    ```
4.  Rebuild the container to apply changes:
    ```bash
    docker-compose up --build
    ```
