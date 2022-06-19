import os

os.path.getsize("spider.txt")
os.path.getmtime("spider.txt")

import datetime

timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
os.path.abspath("spider.txt")