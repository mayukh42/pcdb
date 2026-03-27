
import argparse

def get_parser():
    parser = argparse.ArgumentParser(
        prog="playtime",
        description="Add playtime for a game on a given build"
    )

    parser.add_argument(
        '--csv', 
        help="path of csv to import from"
    )

    parser.add_argument(
        '--lines',
        type=str,
        default="",
        help="range of lines start-end (start inclusive, end exclusive) in csv to process."
    )

    parser.add_argument(
        '--build',
        default="203",
        help="id of the build"
    )

    parser.add_argument(
        '--test',
        action="store_true"
    )

    return parser
