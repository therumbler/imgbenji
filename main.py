#!/usr/bin/env python3
from imgbenji.api import make_api
from imgbenji.utils import setup_logging

if __name__ == "__main__":
    setup_logging()
    api = make_api()
    api.run(port=8080)
