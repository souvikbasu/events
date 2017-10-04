# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, request
from hasweb.models import Event
from .. import app


@app.route('/')
def index():
    event = Event.query.first()
    return "Hello \n"+request.headers['Host']+"---"+event.title