"""some utils for the app"""
import logging
import sys

def setup_logging(level=logging.DEBUG):
    """setup stdout logging"""
    root = logging.getLogger()
    root.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s - %(pathname)s - %(funcName)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

