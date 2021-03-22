import socket
import string
import keys
import sys


class Socket:
    """
    Interface between Twitch Chat and our bot.
        -example usage:
                        test_socket = Socket(CHANNEL_NAME, BOT_USERNAME, BOT_TOKEN)
                        response = test_socket.socket.recv(2048).decode('utf-8')
                        print(response)
    """

    def __init__(self, channel_name, bot_username, bot_token):
        self.read_buffer = ""
        self.socket = socket.socket()  # create socket with his own host, pass and
        self.socket.connect((keys.HOST, keys.PORT))  #connecting to the host
        """ AUTH """
        self.socket.send(f"PASS {bot_token}\n".encode('utf-8'))  # send oauth:123423512351345 stuff
        self.socket.send(f"NICK {bot_username}\n".encode('utf-8'))  # send bot twitch login
        self.socket.send(f"JOIN {channel_name}\n".encode('utf-8'))  # send channel's name what we want to connect


test_socket = Socket(keys.CHANNEL_NAME, keys.BOT_USERNAME, keys.BOT_TOKEN)
resp = test_socket.socket.recv(2048).decode('utf-8')

print(resp)
