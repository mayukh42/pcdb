
from dataclasses import dataclass
from collections.abc import Callable
import csv

@dataclass
class CsvReader():
    path: str
    skiplines: int
    fields: []
    drop_fields: []
    add_fields: {}
    skip_condition: Callable


''' read_csv(rdr)
    Reads a csv with custom options like 
        skiplines (int): drop content of first n lines (including header)
        projection ([]str): select a subset of fields in output
        custom_fields: ({str: object}): add more custom fields provided as (k, v) dict
        skip_condition: a boolean function

    This function gives more control to the caller rather than depending on csv lib for the content
'''
def read_csv(rdr):
    def process_row(row):
        filtered = {}
        if rdr.skip_condition and rdr.skip_condition(row):
            return filtered

        for field in rdr.fields:
            if field in row:
                filtered[field] = row[field]
        
        for field in rdr.drop_fields:
            filtered.pop(field)
        
        filtered.update(rdr.add_fields)
        return filtered

    rows = []
    try:
        with open(rdr.path, 'r') as f:
            reader = csv.DictReader(f, fieldnames=rdr.fields)
            count = 0
            for row in reader:
                count += 1
                if count >= rdr.skiplines:
                    filtered = process_row(row)
                    if filtered:
                        rows.append(filtered)
        return rows
    except Exception as e:
        print("error in csv read:", e)

