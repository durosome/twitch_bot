import socket
import string
import keys
import sys
import time
import asyncio


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
        self.socket = socket.socket()  # create socket
        self.socket.connect((keys.HOST, keys.PORT))  # connecting to the host
        """ AUTH """
        self.socket.send(f"PASS {bot_token}\n".encode('utf-8'))  # send oauth:123423512351345 stuff
        self.socket.send(f"NICK {bot_username}\n".encode('utf-8'))  # send bot twitch login
        self.socket.send(f"JOIN {channel_name}\n".encode('utf-8'))  # send channel's name what we want to connect

    def response(self):
        response = self.socket.recv(2048).decode('utf-8')
        return response


class Listener:
    """
    function that listen socket at background and give response
    -example usage:
                -- create a listener:
                    CHANNEL_NAME = '#the_name_of_twitch_channel'
                    BOT_USERNAME = 'your_bot_login_on_twitch'
                    BOT_TOKEN = 'oauth:a1b2c34d5efg6j789klm1n01opqrst'

                    test_socket = Socket(CHANNEL_NAME, BOT_USERNAME, BOT_TOKEN)
                    test_listener = Listener(test_socket)
                -- get response from socket:
                    test_listener.get_response()
    """

    def __init__(self, socket):
        pass

    def get_response(self):
        pass


test_socket = Socket(keys.CHANNEL_NAME, keys.BOT_USERNAME, keys.BOT_TOKEN)

while True:
    response = test_socket.socket.recv(2048).decode('utf-8')
    print(test_socket.response())
    time.sleep(5)
