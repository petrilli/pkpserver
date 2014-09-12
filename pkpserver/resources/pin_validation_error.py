# -*- coding: utf-8 -*-
from flask.ext import restful


class PinValidationError(restful.Resource):
    """Represents a single instance of a Pin Validation error from a user
    agent (UA) when a Known Pinned Host has set the report-uri directive."""
    def post(self):
        return {'status': 'OK'}

