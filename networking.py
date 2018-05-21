import socket

IP = '0.0.0.0'
PORT = 8080
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048


def respond(client_socket, client_ip_and_port):
    initial_response = "Hi there, what's up?\n".encode()
    client_socket.send(initial_response)

    client_message = client_socket.recv(BUFFER_SIZE).decode()
    echo_response = ("You said: " + client_message).encode()
    client_socket.send(echo_response)


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