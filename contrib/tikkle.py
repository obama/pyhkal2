!obby
session version="0.4.7"
 user_table
  user colour="ccccff" id="1" name="StruC"
  user colour="fcffba" id="2" name="npx"
 chat
  user_message text="RegExp(string)" timestamp="1264894720" user="1"
 document encoding="UTF-8" id="1" owner="2" suffix="1" title="tikkle.py"
  chunk author="2" content="\"\"\"\n\n    Der fabuloese TikkleMod\n\n    - Ein-/Auslog-Phrase                          [x]\n    - AFK-Phrase                                  [x]\n    - Abos requesten von DigestMod                [ ]\n    - Ein und ausloggen via user.py               [x]\n\n\"\"\"\n\n__version__ = \"0.1a\"\n__requires__ = ['user','digest']\n\n@hook('PRIVMSG','/.*/')\ndef startTheTikkleFun(origin, args):\n    if (origin.type == 'channel'):\n\n        # 1) Phrase basteln!\n        msg = ' '.join(args[1:])\n        \n        # 2) Ist der User schon eingeloggt?\n        acc = user.getAccountByOrigin(origin)\n\n        if (acc != None):                           ######## User ist eingeloggt\n            \"\"\"\n                Digests?\n                Afk setzen?\n                Ausloggen?\n            \"\"\"\n            ## Logout\n            accounts = getAccountsThatMatchPhrase('logout', msg)\n            for acc in accounts:\n                if origin.user == acc[\"loggedinas\"]:\n                    user.logout(acc)\n                    return None\n            \n            ## AFK setzen\n            accounts = getAccountsThatMatchPhrase('afk', msg)\n            for acc in accounts:\n                if origin.user == acc[\"loggedinas\"]:\n                    user.setLastActivity(acc)\n                    return None\n            \n            ## Digest\n            accounts = getAccountsThatMatchPhrase('login', msg)\n            for acc in accounts:\n                if origin.user == acc[\"loggedinas\"]:\n                    doStuff(acc)\n                    return None\n\n        else:                                       ## User ist nicht eingeloggt\n            accounts = getAccountsThatMatchPhrase('login', msg)\n            for acc in accounts:\n                def takeItToTheNextLevel(qauth):\n                    if (qauth != ''):                            # User geauthed\n                        if (qauth == acc[\"qauth\"]):\n                            user.identify(qauth)\n                            return None\n                    else:                                  # User nicht geauthed\n                        irc.notice(origin.user, \"PENIS PENIS PENIS PENIS PENIS PENIS! (... and a baseball bat...)\")\n                        return None\n                channel.get_auth_nick(origin.user, takeItToTheNextLevel(qauth))\n\ndef getAccountsThatMatchPhrase(typ, phrase):\n    if typ == 'afk':\n    \"\"\"\n    function(doc) {\n        if (RegExp(doc.XXXXXphrase).test(%s)) {\n            emit(\"penis\",doc)\n        }\n    }\n    \"\"\" % phrase\n        return [] ## afkphrase\n    elif typ == 'logout':\n        return [] ## logoutphrase\n    else\n        return [] ## loginphrase\n\n@hook(\""
  chunk author="1" content="user."
  chunk author="2" content="loggedin\")\ndef doStuff(acc):\n    irc.notice(origin.user, \"hi %s! DIGESTS UND SO!\" % acc)"