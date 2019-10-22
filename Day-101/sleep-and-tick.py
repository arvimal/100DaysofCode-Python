#!/usr/bin/env python3

import time


def sleep_n_tick(s=None, t=None):
    """
    Tick and sleep for the specified counts
    """
    if s is None or t is None:
        print("Sleep and tick values required.")
    else:
        print("-Ticking for {} counts, and sleeping {} sec in-between".format(t, s))
        for i in range(t):
            print("Tick...")
            time.sleep(s)


sleep_n_tick(1, 4)
sleep_n_tick(2, 5)
sleep_n_tick(4, 10)
