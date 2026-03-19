from peewee import (
    DatabaseProxy,
    AutoField,
    IntegerField,
    FloatField,
    CharField,
    Model
)

DB = DatabaseProxy()

class BaseModel(Model):
    class Meta:
        database = DB

class GameStat(BaseModel):
    id = AutoField(primary_key=True)
    title = CharField()
    hours = FloatField()
    gpu = CharField()
    gpad = CharField()
    remarks = CharField()
