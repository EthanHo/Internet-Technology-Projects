import threading
import time
import random

import socket

def reverseString(text):
    if len(text) <= 1:
        return text

    return reverseString(text[1:]) + text[0]



def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.
    # msg = "Welcome to CS 352!"
    # csockid.send(msg.encode('utf-8'))
    SL = csockid.recv(100).decode('utf-8')
    iterateThis = int(SL)

    for i in range(iterateThis):
        reverseMe = csockid.recv(100);
        reverseMe = reverseMe.decode('utf-8')
        print("[S]: RECV " + reverseMe.strip())
        meReversed = reverseString(reverseMe)
        answer = meReversed + reverseMe
        print("[S]: SENT " + answer.strip())
        print("")
        csockid.send(answer.encode('utf-8'))

    # Close the server socket
    ss.close()
    exit()


if __name__ == "__main__":
    server()
