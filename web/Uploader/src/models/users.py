from models.db import LksModel, me
from datetime import datetime

class Users(LksModel):
    meta = {"collection": "g_users"}

    username = me.StringField(max_length=100, required=True)
    password = me.StringField(max_length=100, required=True)
    last_active = me.DateTimeField(default=datetime.now, required=True)
    verified_at = me.DateTimeField(required=False)