
from config import config
from rest.db.models import (
    GPU_FIELDS,
    Playtime, 
    now,
    GPUStats
)
from rest.db.conn import connect_sqlitedb
from args import get_parser
from lib.csvtools.readers import CsvReader
import json, math


def convert_keys(row_dict): 
    all_fields = {'last_updated': 'last_updated'}
    all_fields.update(GPU_FIELDS)
    return dict(map(lambda x: (all_fields[x], row_dict[x]), row_dict.keys()))


def csv_rows(rdr):
    rows = rdr.read()
    row_dicts = list(map(convert_keys, rows))
    print("processed:", json.dumps(row_dicts, indent=2))
    # print(GPU_FIELDS)
    return row_dicts


def create_tables(db, models):
    try:
        db.create_tables(models)
        print("created tables for", models)
    except Exception as e:
        print("exception in creating tables (perhaps already exist(s))", e)


def db_insert(rows):
    try:
        cfg = config.get_config()
        existing = "pcdb-test_1774635657.db"
        # existing = None
        db = connect_sqlitedb(cfg['db'], existing=existing)
        create_tables(db, [GPUStats])
        print(f"inserting {len(rows)} rows...")
        GPUStats.insert_many(rows).execute()
        print(f"inserted")
        db.close()
    except Exception as e:
        print("error during insert: ", e)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    if args.test:
        print("test_mode", args)

    line_range = list(map(lambda x: int(x), args.lines.split('-'))) if args.lines else [0, int(math.inf)]
    rdr = CsvReader(
        args.csv, 
        line_range[0],
        line_range[1], 
        GPU_FIELDS.keys(), 
        ['#'],
        {'last_updated': now()}, 
        lambda x: x['GPU'] == ''
    )
    row_dicts = csv_rows(rdr)
    print(f"processed {len(row_dicts)} rows")

    db_insert(row_dicts)

