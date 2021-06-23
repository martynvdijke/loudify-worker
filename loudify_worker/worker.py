"""Actual Loudify worker

Uses the mdwrk API to hide all MDP aspects

Author: Martyn van Dijke
Based on ZMQ example by Min RK <benjaminrk@gmail.com>
"""

import sys
from . import worker_api


def main():
    """
    Main function
    """
    verbose = "-v" in sys.argv
    worker = worker_api.Worker("tcp://localhost:5555", b"echo", verbose)
    reply = None
    while True:
        request = worker.recv(reply)
        # sleep(0.025)
        if request is None:
            break  # Worker was interrupted
        reply = request  # Echo is complex... :-)


if __name__ == "__main__":
    main()
