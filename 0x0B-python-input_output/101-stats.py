#!/usr/bin/python3
"""Reads from standard input line by line and computes metrics."""


def print_metrics(size, stat_codes):
    """Print gotten metrics"""
    print("File size: {}".format(size))
    for key in sorted(stat_codes):
        print("{}: {}".format(key, stat_codes[key]))


if __name__ == "__main__":
    from sys import stdin

    size = 0
    stat_codes = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in stdin:
            if count == 10:
                print_metrics(size, stat_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes:
                    if stat_codes.get(line[-2], -1) == -1:
                        stat_codes[line[-2]] = 1
                    else:
                        stat_codes[line[-2]] += 1
            except IndexError:
                pass

        print_metrics(size, stat_codes)

    except KeyboardInterrupt:
        print_metrics(size, stat_codes)
        raise
