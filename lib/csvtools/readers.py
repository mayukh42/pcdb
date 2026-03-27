
from dataclasses import dataclass
from collections.abc import Callable
import csv

@dataclass
class CsvReader():
    path: str
    line_start: int
    line_end: int
    fields: []
    drop_fields: []
    add_fields: {}
    skip_condition: Callable

    ''' read_csv(rdr)
        Reads a csv with custom options like
            line_start, line_end (int): use only lines (including header) between start (inclusive) and end (exclusive)
            projection ([]str): select a subset of fields in output
            custom_fields: ({str: object}): add more custom fields provided as (k, v) dict
            skip_condition: a boolean function

        This function gives more control to the caller rather than depending on csv lib for the content
    '''
    def read(self) -> []:
        def process_row(row):
            filtered = {}
            if self.skip_condition and self.skip_condition(row):
                return filtered

            for field in self.fields:
                if field in row:
                    filtered[field] = row[field]
            
            for field in self.drop_fields:
                filtered.pop(field)
            
            filtered.update(self.add_fields)
            return filtered

        rows = []
        try:
            with open(self.path, 'r') as f:
                reader = csv.DictReader(f, fieldnames=self.fields)
                count = 0
                for row in reader:
                    count += 1
                    if count >= self.line_start and count < self.line_end:
                        filtered = process_row(row)
                        if filtered:
                            rows.append(filtered)
            return rows
        except Exception as e:
            print("error in csv read:", e)

