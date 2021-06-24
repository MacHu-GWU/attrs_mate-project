#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
find md5 checksum of a file.
"""

import hashlib


def find_md5_sum(path):
    md5 = hashlib.md5()
    with open(path, "rb") as f:
        md5.update(f.read())
    return md5.hexdigest()


if __name__ == "__main__":
    import sys

    print(find_md5_sum(sys.argv[1]))
