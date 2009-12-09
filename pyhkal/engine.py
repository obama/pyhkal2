#!/usr/bin/env python
# encoding: utf-8

import pyhkal.shopping as shopping
import pyhkal.davenport as davenport

commands = {}
modules = []
# dict of str -> (callback, dict of str -> (callback, dict ...))

def run(location=None):
    """Run PyHKAL on a CouchDB available at `location`."""
    davenport.use(location)
    for mod in davenport.remember("modules"):
        shopping.buy(mod)
    #+ config parsen
    #+ module laden
    #+ irc/web starten?


def dispatch_event(event, origin, args):
    pass
    #+ event dispatch

def dispatch_command(origin, command, *args):
    # Erwartet den Command in Listen-Form:
    # z.B.: ['rep', '-svn', 'install', 'stfumod']
    # Andere Transportschichten müssen dieses Format entsprechend einhalten.
    #+ subcommand dispatch
    #   !rep
    #     -svn ('install', 'stfumod')
    if command in commands:
        commands[command](origin, args)

class Origin(object):
    def __init__(self, typ, user, public=None):
        self.type = typ # of (query, channel, notice, dcc, web)
        self.user = user
        self.public = public
# origin:
#   query (user)
#   notice (user, channel)
#   channel (user, channel)
#   dcc (user)
#   web (user)
