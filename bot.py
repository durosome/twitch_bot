import socket
import string
import twitch_keys
import sys
import time
import discord


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
        self.socket.connect((twitch_keys.HOST, twitch_keys.PORT))  # connecting to the host
        """ AUTH """
        self.socket.send(f"PASS {bot_token}\n".encode('utf-8'))  # send oauth:123423512351345 stuff
        self.socket.send(f"NICK {bot_username}\n".encode('utf-8'))  # send bot twitch login
        self.socket.send(f"JOIN {channel_name}\n".encode('utf-8'))  # send channel's name what we want to connect


class Listener:
    """
    function that listen socket at background and give response to ping
    -example usage:
                -- create a listener:
                    CHANNEL_NAME = '#the_name_of_twitch_channel'
                    BOT_USERNAME = 'your_bot_login_on_twitch'
                    BOT_TOKEN = 'oauth:a1b2c34d5efg6j789klm1n01opqrst'

                    test_socket = Socket(CHANNEL_NAME, BOT_USERNAME, BOT_TOKEN)
                    test_listener = Listener(test_socket)

                -- get response/send respond from/to socket:
                    test_listener.get_response()

                -- self.send_message('SeriousSloth')
    """

    def __init__(self, socket):
        self.socket = socket

    def send_message(self, message):
        self.socket.socket.send(("PRIVMSG " + twitch_keys.CHANNEL_NAME + " :" + message + "\r\n").encode('utf-8'))

    def parse_message(self, response):
        user = response.split(':')[1]
        user = user.split('!')[0]
        message = response.split(':')[2]
        print(user, ': ', message)
        return (user, message)

    def ping_response(self, response):
        if response.startswith('PING'):
            self.socket.socket.send("PONG\n".encode('utf-8'))
            self.send_message('SeriousSloth')

    def listen(self):
        self.send_message('I am connected. All systems report normal, Captain. SeemsGood')
        while True:
            self.response = self.socket.socket.recv(2048).decode('utf-8')
            self.ping_response(self.response)
            self.parse_message(self.response)
            time.sleep(5)


class Discord(discord.Client):
    def __init__(self):
        super().__init__()
        self.TOKEN = twitch_keys.DISCORD_TOKEN

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


test_discord_bot = Discord()
test_discord_bot.run(test_discord_bot.TOKEN)

test_socket = Socket(twitch_keys.CHANNEL_NAME, twitch_keys.BOT_USERNAME, twitch_keys.BOT_TOKEN)
test_listener = Listener(test_socket)
test_listener.listen()
