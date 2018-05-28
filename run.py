# -*- coding: utf-8 -*-
from slackbot.bot import Bot


class SlackBot(object):
    def __init__(self):
        self.bot = Bot()

    def main(self):
        self.bot.run()
        return


if __name__ == '__main__':
    bot = SlackBot()
    bot.main()