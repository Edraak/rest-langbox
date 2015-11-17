import os
from app import app
import unittest
import tempfile


class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def _run_file(self, name):
        full_path = 'fixtures/{}'.format(name)

        with open(full_path) as code_file:
            code = '\n'.join(code_file.readlines())

            return self.app.post(
                '/v1/run',
                data=code,
            ).data

    def test_hello_world(self):
        self.assertEqual('Hello, World\n', self._run_file('HelloWorld.java'))


if __name__ == '__main__':
    unittest.main()
