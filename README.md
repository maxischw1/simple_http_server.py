# Simple HTTP Server

This repository contains a simple HTTP server implementation in Python. It serves HTTP requests and can be stopped manually or programmatically.

# How to Run

1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository or download the `server.py` file.

3. Open a terminal and navigate to the directory containing `server.py`.

4. Run the server using the following command:

   ```sh
   python server.py

   ```
5. The server will start and listen on port 1612.
   Open a web browser and go to http://localhost:1612 to see the server response. 

# How to Stop

1. To stop the server, press Ctrl+C in the terminal where the server is running.
   
2. Alternatively, the server is set up to handle the SIGINT signal and will shut down gracefully.

# Code Explanation



# Import Modules

```bash
import http.server
```
This module provides basic classes for building web servers in Python.
It includes the BaseHTTPRequestHandler class, which we use to handle HTTP requests.

```bash
import socketserver
```
This module provides the TCPServer class, which allows us to create a TCP server.
We use this class to create our HTTP server by passing it an instance of our request handler.

```bash
import signal
```
This module provides mechanisms to handle asynchronous events using signal handlers.
In our code, we use it to handle the SIGINT signal, which is typically sent when the user presses Ctrl+C in the terminal
This allows us to gracefully shut down the server.

```bash
import sys
```
This module provides access to some variables used or maintained by the Python interpreter
and to functions that interact strongly with the interpreter.
We use it to call sys.exit(0), which cleanly exits the program when the server is shut down.




### Classes and Functions

```bash
class MyHandler(http.server.BaseHTTPRequestHandler):
```
This class inherits from BaseHTTPRequestHandler and handles HTTP GET requests.
The do_GET method is overridden to provide a custom response when a GET request is received.

```bash
def do_GET(self):
```
This method is called whenever a GET request is received by the server.
Here, it sends a response with status code 200 (OK),
sets the content type to text/html, and sends an HTML message.




### Signal Handler

```bash
def signal_handler(signal, frame):
    print('Stopping server...')
    httpd.shutdown()
    sys.exit(0)
```
This function is defined to handle the SIGINT signal.
When Ctrl+C is pressed, this function is called.
It prints a message, shuts down the server gracefully using httpd.shutdown(),
and exits the program with sys.exit(0).




### Server Setup and Execution

```bash
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    signal.signal(signal.SIGINT, signal_handler)
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
```

```bash
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
```
This line creates an instance of TCPServer.
The server listens on the specified port (PORT) and uses the MyHandler class to handle requests.
The with statement ensures that the server is properly cleaned up when it is no longer needed.

```bash
signal.signal(signal.SIGINT, signal_handler)
```
This line registers the signal_handler function to handle SIGINT signals.
This allows the server to be stopped gracefully when Ctrl+C is pressed.

```bash
httpd.serve_forever()
```
This method starts the server and keeps it running,
listening for and handling requests indefinitely.
