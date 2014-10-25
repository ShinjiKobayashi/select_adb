#!/usr/bin/env python
# -*- cording: utf-8 -*-
__author__ = 'skobayashi'

import subprocess
import sys

def main(args):
    args.insert(0, "adb")
    test = ["adb", "shell"]
    if subprocess.call(test):
        devlist = subprocess.check_output(["adb", "devices"]).split("\n")
        while '' in devlist:
            devlist.remove('')

        for cnt, name in enumerate(devlist[1:]):
            print str(cnt+1), '-', name[:-7]

        num = raw_input("select [1:"+str(cnt + 1)+"] volumes ")
        if int(num) > (cnt + 1) or int(num) <= 0:
            sys.exit()

        args.insert(1, "-s")
        args.insert(2, devlist[int(num)][:-7])
        subprocess.call(args)
    else:
        subprocess.call(args)

if __name__ == "__main__":
    args = sys.argv
    main(args[1:])