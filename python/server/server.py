import socket
import threading

# Original server file: https://github.com/TiagoValdrich/python-socket-chat/tree/master

# Global variable that maintain client's connection
connections = []


def handle_user_connection(connection: socket.socket, address: str) -> None:
    """
    Get user connection in order to keep receiving their messages and
    sent to others users/connections.
    :param connection:
    :param address:
    :return: None
    """
    while True:
        try:
            # Get client message
            msg = connection.recv(1024)

            # If no message is received, there is a chance that connection has ended
            # so in this case, we need to close connection and remove it from connections list.
            if msg:
                # Log message sent by user
                print(f'{address[0]}:{address[1]} - {msg.decode()}')

                # Build message format and broadcast to users connection on server
                msg_to_send = f'From {address[0]}:{address[1]} - {msg.decode()}'
                broadcast(msg_to_send, connection)

            # Close connection if no message was sent
            else:
                remove_connection(connection)
                break

        except Exception as e:
            print(f'Error to handle user connection: {e}')
            remove_connection(connection)
            break


def broadcast(message: str, connection: socket.socket):
    """
    Broadcast message to all users connected to the server
    :param message: Message sent by user
    :param connection: Socket of the user sending the message
    """

    # Iterate on connections in order to send message to all client's connections
    for client_conn in connections:
        # Check if isn't the connection of who's send
        if client_conn != connection:
            try:
                # Sending message to client connection
                client_conn.send(message.encode())

            # if it fails, there is a chance of socket has died
            except Exception as e:
                print(f'Error broadcasting message: {e}')
                remove_connection(client_conn)


def remove_connection(conn: socket.socket) -> None:
    """
    Remove specific connection from connections list
    :param conn: connection to be removed
    :return: None
    """

    # Check if connection exists on connections list
    if conn in connections:
        # Close socket connection and remove connection from connections list
        conn.close()
        connections.remove(conn)


def server() -> None:
    """
    Main process that receive client's connections and start a new thread
    to handle their messages
    :return: None
    """

    socket_instance = None
    LISTENING_PORT = 12000

    try:
        # Create server and specifying that it can only handle 4 connections by time!
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen(4)

        print('Server running!')

        while True:

            # Accept client connection
            socket_connection, address = socket_instance.accept()
            # Add client connection to connections list
            connections.append(socket_connection)
            # Start a new thread to handle client connection and receive its message
            # in order to send to other connections
            threading.Thread(target=handle_user_connection, args=[socket_connection, address]).start()

    except Exception as e:
        print(f'AN error has occurred when instancing socket: {e}')

    finally:
        # In case of any problem we clean all connections and close the serer connection
        if len(connections) > 0:
            for conn in connections:
                remove_connection(conn)

        socket_instance.close()


if __name__ == "__main__":
    server()
