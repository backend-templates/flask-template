#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"