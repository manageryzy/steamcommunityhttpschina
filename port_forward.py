# Author: Mario Scondo (www.Linux-Support.com)
# Date: 2010-01-08
# Script template by Stephen Chappell
#
# This script forwards a number of configured local ports
# to local or remote socket servers.
#
# Configuration:
# Add to the config file port-forward.config lines with
# contents as follows:
#   <local incoming port> <dest hostname> <dest port>
#
# Start the application at command line with 'python port-forward.py'
# and stop the application by keying in <ctrl-c>.
#
#

import socket
import sys
import time
if sys.version_info >= (3, 0):
    import _thread as thread
else:
    import thread



def main(setup):
    # read settings for port forwarding
    for settings in parse(setup):
        thread.start_new_thread(server, settings)
    # wait for <ctrl-c>
    while True:
       time.sleep(60)


def parse(setup):
    settings = list()
    for line in open(setup):
        # skip comment line
        if line.startswith('#'):
            continue

        parts = line.split()
        settings.append((int(parts[0]), parts[1], int(parts[2])))
    return settings


def server(*settings):
    print('forwarding localhost:'+ str(settings[0]) + ' to ' + str(settings[1]) + ':' + str(settings[2]))
    try:
        dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dock_socket.bind(('', settings[0]))
        dock_socket.listen(5)
        while True:
            client_socket = dock_socket.accept()[0]
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((settings[1], settings[2]))
            thread.start_new_thread(forward, (client_socket, server_socket))
            thread.start_new_thread(forward, (server_socket, client_socket))
    finally:
        thread.start_new_thread(server, settings)


def forward(source, destination):
    string = ' '
    while string:
        string = source.recv(1024)
        if string:
            destination.sendall(string)
        else:
            source.shutdown(socket.SHUT_RD)
            destination.shutdown(socket.SHUT_WR)


if __name__ == '__main__':
    main('port-forward-test.conf')
