
from config import config
from rest.db.models import (
    PLAYTIME_FIELDS,
    Playtime
)
from args import get_parser
from lib.csvtools.readers import CsvReader
import json, math


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
        PLAYTIME_FIELDS, 
        ['#'],
        {"build": args.build}, 
        lambda x: x['title'] == ''
    )
    rows = rdr.read()
    print("processed:", json.dumps(rows, indent=2))

