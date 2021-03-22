import socket
import string
import keys
import sys
import time


class Socket:
    """
    Interface between Twitch Chat and our bot.
        -example usage:
                --create socket:
                        CHANNEL_NAME = '#the_name_of_twitch_channel'
                        BOT_USERNAME = 'your_bot_login_on_twitch'
                        BOT_TOKEN = 'oauth:a1b2c34d5efg6j789klm1n01opqrst'

                        test_socket = Socket(CHANNEL_NAME, BOT_USERNAME, BOT_TOKEN)
                        response = test_socket.socket.recv(2048).decode('utf-8')
                        print(response)

                --closing the socket:
                        test_socket.socket.close()
    """

    def __init__(self, channel_name, bot_username, bot_token):
        self.read_buffer = ""
        self.socket = socket.socket()  # create socket
        self.socket.connect((keys.HOST, keys.PORT))  # connecting to the host
        """ AUTH """
        self.socket.send(f"PASS {bot_token}\n".encode('utf-8'))  # send oauth:123423512351345 stuff
        self.socket.send(f"NICK {bot_username}\n".encode('utf-8'))  # send bot twitch login
        self.socket.send(f"JOIN {channel_name}\n".encode('utf-8'))  # send channel's name what we want to connect

    def response(self):
        response = self.socket.recv(2048).decode('utf-8')
        return response


test_socket = Socket(keys.CHANNEL_NAME, keys.BOT_USERNAME, keys.BOT_TOKEN)

while True:
    response = test_socket.socket.recv(2048).decode('utf-8')
    print(response)
    time.sleep(5)
