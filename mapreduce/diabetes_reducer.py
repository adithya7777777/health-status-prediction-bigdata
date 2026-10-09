#!/usr/bin/env python3

import sys

current_status = None
total_count = 0

for line in sys.stdin:

    line = line.strip()

    status, count = line.split("\t")

    count = int(count)

    if current_status != status:

        if current_status is not None:
            print(f"{current_status}\t{total_count}")

        current_status = status
        total_count = count

    else:
        total_count += count

if current_status is not None:
    print(f"{current_status}\t{total_count}")
