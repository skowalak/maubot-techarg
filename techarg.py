from maubot import Plugin, MessageEvent
from maubot.handlers import event, command
from mautrix.types 
from .reasons import strings_arg, strings_noarg

import random


class TechargBot(Plugin):
    @command.new("ta", help="Get reasons why it just won't work. Syntax: !ta <term>")
    @command.argument("term", pass_raw=True, required=False)
    async def handler(self, event: MessageEvent, term: str) -> None:

        if term:
            # pick string with an argument
            reason = random.choice(strings_arg)
            reason.format(term=term)

        else:
            # no string specified, get reason without argument
            reason = random.choice(strings_noarg)

        await event.respond(reason)
    
