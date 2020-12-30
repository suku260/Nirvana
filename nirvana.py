import socket
import ipaddress
from html.parser import HTMLParser
import os

class Nirvana():
    def server_open(ip,port):
        print(f"connecting to {str(ip)} at port {str(port)}...")
        echoSocket = socket.socket()
        echoSocket.bind((ip, int(port)))
        echoSocket.listen(10)
        print("Connection successful")
        while True:
            # Establish connection with client.    
            c, (client_host, client_port) = echoSocket.accept()
            print('Got connection from', ip, port)
    
            c.recv(1000) # should receive request from client. (GET ....)
            html=("""
            <html>
            <body>
            <h1>Hello World</h1> this is my server!
            </body>
            </html>
            """)
            c.send(f"{html}".encode('ascii')) # send request
             # Use triple-quote string.
    
            c.close()
            
    def setup():
        print("Getting the environment ready...")
        os.makedirs("Nirvana_Project")
        os.makedirs("Nirvana_Project/files")
        os.makedirs(" Nirvana_Project/images")
        os.system("touch setup.py")
        info = open('Nirvana_Project/setup.py', 'w') 
        info.write('''paths=[]
        db=[sqlite3]
        ip="127.0.0.1"
        port="80"
        def setup_info():
            stuff=[ip,port]
            return stuff
        ''')
        info.close()

        os.system("touch Nivana_Project/paths.py")
        print("environment ready")

