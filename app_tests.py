import os
import unittest
import tempfile
import json
import subprocess

from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def run_case(self, code_file, stdin_file=None):
        if stdin_file:
            with open('fixtures/{}'.format(stdin_file)) as stdin_file_obj:
                stdin = stdin_file_obj.read()
        else:
            stdin = ''

        with open('fixtures/{}'.format(code_file)) as code_file_obj:
            code = code_file_obj.read()

        post_data = json.dumps({
            'code': code,
            'stdin': stdin,
        })

        return self.app.post(
            '/v1/run',
            data=post_data,
        ).data

    def test_hello_world(self):
        self.assertEqual('Hello, World', self.run_case('HelloWorld.java'))


if __name__ == '__main__':
    unittest.main()
