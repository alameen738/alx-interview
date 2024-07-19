#!/usr/bin/python3

import sys
from collections import defaultdict

def print_metrics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        try:
            _, _, request, status_code_str, file_size_str = line.strip().split(" ", 4)
            status_code = int(status_code_str)
            file_size = int(file_size_str)
            total_size += file_size
            status_counts[status_code] += 1
        except (ValueError, IndexError):
            pass
        line_count += 1
        if line_count % 10 == 0:
            print_metrics(total_size, status_counts)
except KeyboardInterrupt:
    print_metrics(total_size, status_counts)
