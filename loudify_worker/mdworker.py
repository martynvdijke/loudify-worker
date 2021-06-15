"""Majordomo Protocol worker example.

Uses the mdwrk API to hide all MDP aspects

Author: Min RK <benjaminrk@gmail.com>
"""

import sys
from mdwrkapi import MajorDomoWorker
from time import sleep

def main():
    verbose = '-v' in sys.argv
    worker = MajorDomoWorker("tcp://localhost:5555", b"echo", verbose)
    reply = None
    while True:
        request = worker.recv(reply)
        # sleep(0.025)
        if request is None:
            break # Worker was interrupted
        reply = request # Echo is complex... :-)


if __name__ == '__main__':
    main()
