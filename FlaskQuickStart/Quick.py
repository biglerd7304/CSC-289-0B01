#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:57:06 2020

@author: daniel
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index ():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'
