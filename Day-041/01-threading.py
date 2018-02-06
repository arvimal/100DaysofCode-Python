#!/usr/bin/env python3

import os
import urllib.request
from threading import Thread


class DownloadThread(Thread):

    def __init__(self, url, name):
        Thread.__init__(self)
        self.url = url
        self.name = name

    def run(self):
        handle = urllib.request.urlopen(self.url)
        fname = os.path.basename(self.url)
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        message = "{} has finished downloading {}".format(self.name, self.url)
        print(message)


def main(urls):
    for i, j in enumerate(urls):
        name = "Thread {}".format(i + 1)
        thread = DownloadThread(j, name)
        thread.start()


if __name__ == "__main__":
    urls = ["http://www.buildeazy.com/plans/test.pdf",
            "http://www.orimi.com/pdf-test.pdf",
            "http://che.org.il/wp-content/uploads/2016/12/pdf-sample.pdf"
            "http://www.irs.gov/pub/irs-pdf/f1040.pdf"]

    main(urls)
