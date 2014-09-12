# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext import restful


app = Flask(__name__)
api = restful.Api(app)

# If we're run as a script, start a debug server
if __name__ == '__main__':
    app.run(debug=True)
