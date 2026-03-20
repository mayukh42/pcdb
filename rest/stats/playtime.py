
from config import config
from rest.db.models import (
    playtime_fields,
    Playtime
)
from args import get_parser
from lib.csvtools import readers
import json


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    if args.test:
        print("test_mode", args)

    rows = readers.read_csv(
        readers.CsvReader(
            args.csv, 
            args.skiplines, 
            playtime_fields, 
            ['#'],
            {"build": args.build}, 
            lambda x: x['title'] == ''
        ))
    print("processed:", json.dumps(rows, indent=2))

