import keys
from irc.bot import SingleServerIRCBot
from requests import get


class Bot(SingleServerIRCBot):
    def __init__(self):
        self.host = keys.HOST
        self.port = keys.PORT
        self.username = keys.BOT_USERNAME
        self.client_id = keys.CLIENT_ID
        self.token = keys.TOKEN
        self.channel = keys.OWNER

        url = f"https://api.twitch.tv/kraken/users?login={self.username}"
        headers = {"Client-ID": self.client_id, "Accept": "application/vnd.twitchtv.v5+json"}
        resp = get(url, headers=headers).json()
        self.channel_id = resp["users"][0]["_id"]

        super().__init__([(self.host, self.port, f"oauth:{self.token}")], self.username, self.username)

    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        cxn.join(self.channel)
        self.send_message("Привет, ты покушал?")

    def on_pubmsg(self, cxn, event):
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"]}
        message = event.arguments[0]

        if user["name"] != name:
            cmds.process(bot, user, message)

    def send_message(self, message):
        self.connection.privmsg(self.channel, message)


if __name__ == "__main__":
    bot = Bot()
    bot.start()
