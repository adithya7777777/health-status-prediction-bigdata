#!/usr/bin/env python3

import sys

for line in sys.stdin:

    line = line.strip()

    if line.startswith("Diabetes_binary"):
        continue

    columns = line.split(",")

    diabetes_status = columns[0]

    print(f"{diabetes_status}\t1")
