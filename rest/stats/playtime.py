
from config import config
from rest.db.models import (
    playtime_fields,
    Playtime
)
from args import get_parser
from rest.utils.readers import CsvReader
import sys, csv


def read_csv(rdr):
    def filter_fields(row):
        filtered = {}
        for field in rdr.fields:
            if field in row and field != '#':
                v = row[field]
                if field == 'hours':
                    v = float(v)
                filtered[field] = v
        
        filtered['build'] = rdr.build
        return filtered

    rows = []
    try:
        with open(rdr.path, 'r') as f:
            reader = csv.DictReader(f, fieldnames=rdr.fields)
            count = 0
            for row in reader:
                count += 1
                if count >= rdr.droplines and row['title']:
                    filtered = filter_fields(row)
                    rows.append(filtered)
                    print(filtered)
    except Exception as e:
        print("error", e)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    if args.test:
        print("test_mode", args)
    read_csv(CsvReader(args.csv, args.build, args.droplines, playtime_fields))
