from peewee import (
    DatabaseProxy,
    AutoField,
    IntegerField,
    FloatField,
    CharField,
    Model
)

DB = DatabaseProxy()

playtime_fields = ['#', 'title', 'hours', 'last played', 'gpu', 'gpad', 'remarks']

class BaseModel(Model):
    class Meta:
        database = DB

class Playtime(BaseModel):
    build = IntegerField()
    title = CharField()
    hours = FloatField()
    gpu = CharField()
    gpad = CharField()
    remarks = CharField()
