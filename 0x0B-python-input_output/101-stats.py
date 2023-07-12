#!/usr/bin/python3
# 101-stats.py
"""A script that reads stdin line by line and computes metrics"""


def print_stats(size, status_codes):
    """ Return print accumulated metrics.

    Args:
        size : int
        status_codes : dict
    """
    print("File size: {}".format(size))
    for k in sorted(status_codes):
        print("{}: {}".format(k, status_codes[k]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    counter = 0

    try:
        for li in sys.stdin:
            if counter == 10:
                print_stats(size, status_codes)
                counter = 1
            else:
                counter += 1

            li = li.split()

            try:
                size += int(l[-1])
            except (IndexError, ValueError):
                pass

            try:
                if li[-2] in valid_codes:
                    if status_codes.get(li[-2], -1) == -1:
                        status_codes[li[-2]] = 1
                    else:
                        status_codes[li[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
