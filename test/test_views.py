
import unittest

from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output_json(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie":"Natalia", "mgs":Hello World!"}', rv.data)

    def test_msg_with_output_plain(self):
        rv = self.app.get('/?output=plain')
        self.assertEqual(b'Natalia Hello World!', rv.data)
    
    def test_msg_with_output_upper(self):
        rv = self.app.get('/?output=plain_uppercase')
        self.assertEqual(b'NATALIA HELLO WORLD!', rv.data)
    
    def test_msg_with_output_lower(self):
        rv = self.app.get('/?output=plain_lowercase')
        self.assertEqual(b'natalia hello world!', rv.data)
