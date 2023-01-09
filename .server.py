# #!/usr/bin/env python3
# import socket
# import http.server
# import socketserver

# host_name = socket.gethostname()
# ip = socket.gethostbyname(host_name)

# host = 'localhost'
# port = 80

# handler = http.server.SimpleHTTPRequestHandler
# with socketserver.TCPServer((host, port), handler) as httpd:
#     print(f'Server is listening on {host} on port {port}.')
#     httpd.serve_forever()
# httpd.server_close()
import paramiko

host = "192.168.83.135"
port = 22
username = "adesh"
password = "GreyHat"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
while True:
    stdin, stdout, stderr = ssh.exec_command(input())
    lines = stdout.readlines()
    print(lines)
