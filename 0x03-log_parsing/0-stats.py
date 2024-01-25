#!/usr/bin/python3
"""
Log parsing script.
"""

import sys

def print_stats(total_size, status_codes):
    """
    Print statistics.
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line, total_size, status_codes):
    """
    Parse a log line and update statistics.
    """
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        total_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1

    except (ValueError, IndexError):
        pass

    return total_size, status_codes


def main():
    """
    Main function for log parsing.
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_codes = parse_line(line, total_size, status_codes)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
