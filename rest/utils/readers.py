
from dataclasses import dataclass

@dataclass
class CsvReader():
    path: str
    build: int
    droplines: int
    fields: []

