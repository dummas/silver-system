import SocketServer

class TCPHandler(SocketServer.BaseRequestHandler):
    """

    """
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} received: {}".format(self.client_address[0], self.data)
        print "Processing data..."
        response = str(sum([int(x) for x in self.data.split()]))
        self.request.sendall(response)
        print "Response sent"

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
    server.serve_forever()
