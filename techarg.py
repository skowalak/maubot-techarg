from maubot import Plugin
from maubot.handlers import event, command
from mautrix.types import MessageEvent
from .excuses import strings_arg, strings_noarg

import random


class TechargBot(Plugin):
    @command.new("ta", help="Get excuses why it just won't work. Syntax: !ta <term>")
    @command.argument("term", pass_raw=True, required=False)
    async def handler(self, event: MessageEvent, term: str) -> None:

        if term:
            # pick string with an argument
            excuse = random.choice(strings_arg)
            excuse = excuse.format(term=term)

        else:
            # no term specified, get string without argument
            excuse = random.choice(strings_noarg)

        await event.respond(excuse)
