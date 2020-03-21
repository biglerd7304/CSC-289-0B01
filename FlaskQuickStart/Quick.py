#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:57:06 2020

@author: daniel
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


#ROUTING
@app.route('/')
def index ():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

#VARIABLE RULES
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s'  % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

#UNIQUE URL/REDIRECTION BEHAVIOR