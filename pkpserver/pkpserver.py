# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext import restful
from .resources.pin_validation_error import PinValidationError


def configure_api(app):
    api = restful.Api(app)
    api.add_resource(PinValidationError, '/')


app = Flask(__name__)
configure_api(app)


# If we're run as a script, start a debug server
if __name__ == '__main__':
    app.run(debug=True)
