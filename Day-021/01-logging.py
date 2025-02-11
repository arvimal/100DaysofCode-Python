#!/usr/bin/env python3

import logging
import module


def main() -> None:
    logging.basicConfig(filename="test.log", level=logging.INFO)
    logging.info("Starting the program.")
    result = module.add(10, 100)
    logging.info("Addition completed.")


if __name__ == "__main__":
    main()
