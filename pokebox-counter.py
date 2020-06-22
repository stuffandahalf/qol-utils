#!/usr/bin/env python

from __future__ import print_function

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main(args):
    if len(args) != 2:
        eprint(args[0] + ' requires one argument')
        return 1

    num = int(args[1]) - 1
    box = (num // 30) + 1
    offset = num % 30

    print('BOX ' + str(box) + ' OFFSET ' + str(offset + 1))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

