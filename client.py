import threading
import time
import random

import socket


def client(textInput):
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
        print(" ")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    try:
        file = open(textInput, 'r')
    except OSError as exception:
        print(exception)
        print("Exiting program.")
        exit()

    numStrings = file.readlines();
    totalL = str(len(numStrings))

    answer = open("out-proj0.txt", "w+")

    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    cs.send(totalL.encode('utf-8'))
    time.sleep(2)

    for inputs in numStrings:
        cs.send(inputs.encode('utf-8'))
        print("[C]: SENT " + inputs.strip())
        ds = cs.recv(100)
        rs = ds.decode('utf-8')
        answer.write(rs)
        print("[C]: RECV " + rs.strip())


    # close the client socket
    cs.close()
    print("[C]: Output has been written to \"out-proj0.txt\"")
    exit()


if __name__ == "__main__":
    txtInput = raw_input("Please enter the input text file (example: \"in-proj0.txt\"): ")
    client(txtInput)
