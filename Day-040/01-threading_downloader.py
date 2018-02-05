#!/usr/bin/env python3

import os
import urllib2
from threading import Thread


class DownloadThread(Thread):

    def __init__(self, url, name):
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        handle = urllib2.urlopen(self.url)
        fname = os.path.basename(self.url)
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        message = "{} finished downloading {}".format(self.name, self.url)
        print(message)


def main(urls):
    for item, url in enumerate(urls):
        name = "Thread {}".format(item + 1)
        thread = DownloadThread(url, name)
        thread.start()


if __name__ == "__main__":
    urls = ["http://www.buildeazy.com/plans/test.pdf",
            "http://www.orimi.com/pdf-test.pdf",
            "http://che.org.il/wp-content/uploads/2016/12/pdf-sample.pdf"
            "http://www.irs.gov/pub/irs-pdf/f1040.pdf"]

    main(urls)

# This will print:
# python 01-threading_downloader.py                                                                                                                                                                                                                                                 1 ↵
# Thread 2 finished downloading http://www.orimi.com/pdf-test.pdf
# Thread 1 finished downloading http://www.buildeazy.com/plans/test.pdf
# ....
