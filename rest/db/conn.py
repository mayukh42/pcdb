
from peewee import SqliteDatabase
from rest.db.models import DB
import os, time

def connect_sqlitedb(db_cfg, existing=None):
    try:
        name = f"{db_cfg['name']}_{int(time.time())}.{db_cfg['ext']}"
        location = f"{db_cfg['location']}"
        if not os.stat(location):
            os.makedirs(location, exist_ok=True)

        if not existing:
            full_path = os.path.join(location, name)
        else:
            full_path = os.path.join(location, existing)
        db = SqliteDatabase(full_path, pragmas={
            'journal_mode': db_cfg['journal_mode'],
            'cache_size': -1000 * db_cfg['cache_size_MB'],
            'foreign_keys': db_cfg['foreign_keys']
        })
        DB.initialize(db)
        return db
    except Exception as e:
        print("error in connecting to sqlitedb: ", e)
        return None

