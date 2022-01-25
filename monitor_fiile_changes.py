#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：monitor_fiile_changes
@IDE    ：pycharm
@Author ：xz98y
@Date   ：2022/1/24 22:58
=================================================='''

import time

def print_file_changes(file_path):
    with open(file_path, "r") as f:
        f.seek(0, 2)
        while True:
            current_position = f.tell()
            line = f.readline()
            if not line:
                f.seek(current_position)
                time.sleep(1)
            else:
                print(line.strip())

if __name__ == "__main__":
    print_file_changes("1.txt")