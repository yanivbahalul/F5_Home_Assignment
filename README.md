# Nginx and Python Project

This project runs a web server (Nginx) on Ubuntu and tests it automatically with Python.

## How to Run

1.  **Get the code:**
    ```bash
    git clone https://github.com/yanivbahalul/F5_Home_Assignment
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

* **The Server:** Runs Nginx.
    * Port **8080**: Shows the website (Returns 200 OK).
    * Port **8000**: Shows an error (Returns 500 Error) for testing.
* **The Test:** A Python script checks if Port 8080 works and if Port 8000 gives an error.

## Decisions & Trade-offs

* **Why Ubuntu?**
    The instructions required using `ubuntu:24.04` as the base image.
* **Size Optimization:**
    Ubuntu is a large image (bigger than Alpine). To make it **as small as possible**, I added a command to delete temporary installation files (`rm -rf /var/lib/apt/lists/*`) inside the Dockerfile.
* **GitHub Actions:**
    The project uses GitHub Actions to build and test the code automatically every time I push changes.
