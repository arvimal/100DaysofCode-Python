#!/usr/bin/env python3

import random
import time
from threading import Thread


class MyThread(Thread):
    """
    Learing how to use threads
    """

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        """
        Run a thread that just sleeps
        """
        count = random.randint(1, 10)
        time.sleep(count)
        print("{} running".format(self.name))


def create_threads():
    for num in range(10):
        name = "Thread {}".format(num + 1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_threads()
