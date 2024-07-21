# Simple HTTP Server

This repository contains a simple HTTP server implementation in Python. It serves HTTP requests and can be stopped manually or programmatically.

## How to Run

1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository or download the `server.py` file.

3. Open a terminal and navigate to the directory containing `server.py`.

4. Run the server using the following command:

   ```sh
   python server.py

   ```
5. The server will start and listen on port 8000.
   Open a web browser and go to http://localhost:8000 to see the server response. 

## How to Stop

1. To stop the server, press Ctrl+C in the terminal where the server is running.
   
2. Alternatively, the server is set up to handle the SIGINT signal and will shut down gracefully.

