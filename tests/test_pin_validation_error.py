# -*- coding: utf-8 -*-
import unittest
from flask import Flask
from flask.ext.testing import TestCase
from pkpserver import pkpserver


class BaseTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        pkpserver.configure_api(app)
        return app


class TestPinValidationError(BaseTest):
    def test_server_is_running(self):
        self.assert405(self.client.get('/'))

    def test_server_denies_get(self):
        self.assert405(self.client.get('/'))

    def test_server_allows_post(self):
        self.assert200(self.client.post('/'))


if __name__ == '__main__':
    unittest.main()
