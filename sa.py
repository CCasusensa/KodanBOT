# -*- coding: utf-8 -*-
import linepy
from linepy import *
import json, time, random, tempfile, os, sys, requests, datetime, codecs, thread
reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient()
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)

poll = LinePoll(client)
mode = 'self'


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def kick_group():
    _name = msg.text.replace("666", "")
    gs = client.getGroup(msg.to)
    targets = []
    for g in gs.members:
        if _name in g.displayName:
            targets.append(g.mid)
    for target in targets:
        try:
            client.kickoutFromGroup(msg.to, [target])
        except Exception as e:
            client.log("[Error]:" + str(e))


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops != None:
            for op in ops:
                if op.type == 25:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    sender = msg._from
                    try:
                        if msg.contentType == 0:
                            if msg.toType == 2:
                                client.sendChatChecked(receiver, msg_id)
                                contact = client.getContact(sender)
                                if ("666" in msg.text):
                                    thread.start_new_thread(kick_group)
                                    thread.start_new_thread(kick_group)
                    except Exception as e:
                        client.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
# Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)

    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
