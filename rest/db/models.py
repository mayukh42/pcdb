from peewee import (
    DatabaseProxy,
    AutoField,
    IntegerField,
    FloatField,
    CharField,
    DateTimeField,
    Model
)

from datetime import datetime

DB = DatabaseProxy()

TS_FORMAT = "%Y-%m-%d %H:%M:%S"

def now() -> str:
    return datetime.now().strftime(TS_FORMAT)

ID = '#'
PLAYTIME_FIELDS = [ID, 'title', 'hours', 'last played', 'gpu', 'gpad', 'remarks']
GPU_FIELDS = {ID: id, 'GPU': 'gpu', 'Desc': 'model', 'Start': 'start', 'End': 'end', 'Age': 'age', 'Add. Age': 'additional_age', 'Age Effect.': 'effective_age', 
    'Hours': 'hours', 'Price': 'price', 'Res X': 'resx', 'Res Y': 'resy', 'RoIF': 'roif', 
    'Target Hrs Delta': 'target_hrs_delta', 'Utilization': 'utilization', 'Inf Factr 2025': 'inf_2025', 'Price InfAdj': 'price_inf_adj', 
    'Gen': 'gen', 
    'Ideal Res X': 'resx_ideal', 'Ideal Res Y': 'resy_ideal', 'Ideal Price 1440p=40k': 'price_ideal_1440p', 'Year of Ideal Purchase': 'year_ideal',
    'Inf Factor': 'inf', 'Ideal Price': 'price_ideal', 'Price Delta': 'price_delta', 'Price Delta Hours 50ph': 'price_delta_hrs_50ph', 
    'Target Hrs Delta Adj': 'target_hrs_delta_adj', 'Total Target Utilization': 'total_target_utilization','RoI/ hr': 'roi_hr', 'Usage %': 'usage_percent'}

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

class GPUStats(BaseModel):
    gpu = CharField()
    model = CharField()
    start = CharField()
    end = CharField()
    age = IntegerField()
    additional_age = IntegerField()
    effective_age = IntegerField()
    hours = FloatField()
    price = FloatField()
    resx = IntegerField()
    resy = IntegerField()
    roif = FloatField()
    target_hrs_delta = FloatField()
    utilization = FloatField()
    inf_2025 = FloatField()
    price_inf_adj = FloatField()
    gen = IntegerField()
    resx_ideal = IntegerField()
    resy_ideal = IntegerField()
    price_ideal_1440p = FloatField()
    year_ideal = IntegerField()
    inf = FloatField()
    price_ideal = FloatField()
    price_delta = FloatField()
    price_delta_hrs_50ph = FloatField()
    target_hrs_delta_adj = FloatField()
    total_target_utilization = FloatField()
    roi_hr = FloatField()
    usage_percent = FloatField()
    last_updated = DateTimeField(default=now())

