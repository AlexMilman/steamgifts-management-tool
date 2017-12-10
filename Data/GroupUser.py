# GroupUser object used to all group users data
# Copyright (C) 2017  Alex Milman


class GroupUser(object):
    user_name=None
    group_won=0.0
    group_sent=0.0
    global_won=0
    global_sent=0
    steam_id=None
    level=0

    def __init__(self, user_name, group_won=0.0, group_sent=0.0, global_won=0.0, global_sent=0.0, steam_id=None, level=0):
        self.user_name = user_name
        self.group_won = float(group_won)
        self.group_sent = float(group_sent)
        self.global_won = int(global_won)
        self.global_sent = int(global_sent)
        self.steam_id = steam_id
        self.level = int(level)
