import socket

IP = '0.0.0.0'
PORT = 8080
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048


def respond(client_socket, client_ip_and_port):
    request = client_socket.recv(BUFFER_SIZE).decode()
    response_headers = "HTTP/1.1 200 OK\n\n"
    response_body = "Your request was:\n" + request
    encoded_response = (response_headers + response_body).encode()
    client_socket.send(encoded_response)


def serverloop():
    listening_socket = socket.socket()
    listening_socket.bind((IP, PORT))
    listening_socket.listen(MAXIMUM_QUEUE_SIZE)

    while True:
        (client_socket, client_ip_and_port) = listening_socket.accept()
        respond(client_socket, client_ip_and_port)
        client_socket.close()


if __name__ == '__main__':  # is this file executed directly (not just imported)
    print('Server launched on %s:%s, press ctrl+c to kill the server'
          % (IP, PORT))
    serverloop()

