# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:45:57 2021

@author: gaffa
"""

import flask

app = flask.Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run()
