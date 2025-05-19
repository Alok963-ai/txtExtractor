#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN","")
    API_ID = int(os.environ.get("API_ID", "20288951"))
    API_HASH = os.environ.get("API_HASH", "e8cb5fb7a475b5f5eb3b0ef0e6ca03a8")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7833842279")
