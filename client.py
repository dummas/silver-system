import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")
    # Received data from the server and shut down
    received = sock.recv(1024)

finally:
    sock.close()

print "Data send: {}".format(data)
print "Response received: {}".format(received)
