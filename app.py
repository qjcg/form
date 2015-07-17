#!/usr/bin/env python3
"""Example of interpreting form data using bottle."""

import os
from bottle import get, post, request, template, run

HOST = '0.0.0.0'
PORT = 9999


@get('/')
def form():
    """Display a simple login form."""
    return template(
        """
        <h1>Unsuspicious form</h1>
        <form action="/submit" method="POST">
            Username: <input name="username" autofocus /> <br />
            Password: <input name="password" type="password" /><br />
            Credit card number: <input name="ccnum" type="number" /><br />
            Number to be exponentiated: <input name="exnum" type="number" /><br />
            <button>Submit</button>
        </form>
        """)


@post('/submit')
def submit_form():
    """Display results of POSTing form to the user."""
    return template(
        """
        <a href="/">Go back</a><br /><br />
        Username: {{ username }}<br />
        Password: {{ password }}<br />
        Credit card number: {{ ccnum }}<br />
        Exnum ** 5: {{ exnum }}<br />
        """,
        username=request.forms.username,
        password=request.forms.password,
        ccnum=request.forms.ccnum,
        exnum=int(request.forms.exnum) ** 5
        )

run(host=HOST, port=PORT)
