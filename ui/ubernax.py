#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return "Ubernax 0.0.1"

if __name__ == "__main__":
    time.sleep(5)
    app.run(host='127.0.0.1', port=5000)

