from socketIO_client import SocketIO, LoggingNamespace
from time import sleep

HOST, PORT = "localhost", 3000

def createSocket():
    return SocketIO(HOST, PORT, LoggingNamespace)
