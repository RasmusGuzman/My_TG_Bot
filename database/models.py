from datetime import datetime
import peewee as pw

db = pw.SqliteDatabase('TG_bot_base.db')

class ModelBase(pw.Model):
    init_time = pw.DateTimeField(default=datetime.now())
    class Meta():
        my_database = db
class User(ModelBase):
    id_user = pw.TextField
    id_req = pw.TextField
    id_time = ModelBase.init_time