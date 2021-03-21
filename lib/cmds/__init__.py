from time import time
from . import misc

PREFIX = "!"
CHAT_COMMANDS = {
    "hello": bot.send_message('hello!'),
}


def process(bot, user, message):
    if message.startswith(prefix):
        cmd = message.split(" ")[0][len(prefix):]
        args = message.split(" ")[1:]
        perform(bot, user, cmd, *args)


def perform(bot, user, cmd, *args):
    for name, func in CMDS.items():
        if cmd == name:
            func(bot, user, *args)
            return ()
    if cmd == "help":
        misc.help(bot, prefix, CMDS)

    else:
        bot.send_message(f"{user['name']}, \"{cmd}\" ? Не знаю такой команды BibleThump")
