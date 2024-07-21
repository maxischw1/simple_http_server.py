
import http.server
import socketserver
import signal
import sys

PORT = 1612

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Congratulations</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                    background: #fff;
                    padding: 2em;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Congratulations!</h1>
                <p>You have successfully set up a simple HTTP server in Python.</p>
                <p>Great job and keep up the good work!</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

def signal_handler(signal, frame):
    print('Stopping server...')
    httpd.shutdown()
    sys.exit(0)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    signal.signal(signal.SIGINT, signal_handler)
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
