# -*- coding: utf-8 -*-
import unittest
from flask import Flask
from flask.ext.testing import TestCase
from pkpserver import app as application


class BaseTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        application.configure_api(app)
        return app


class TestPinValidationError(BaseTest):
    def test_server_is_running(self):
        self.assert405(self.client.get('/'))

    def test_server_denies_get(self):
        self.assert405(self.client.get('/'))

    def test_server_allows_post(self):
        self.assert200(self.client.post('/'))

    def test_server_accepts_json(self):
        result = self.client.post('/', data={
            "date-time": "2014-04-06T13:00:50Z",
            "hostname": "www.example.com",
            "port": 443,
            "effective-expiration-date": "2014-05-01T12:40:50Z",
            "include-subdomains": False,
        })
        self.assert200(result)

if __name__ == '__main__':
    unittest.main()
