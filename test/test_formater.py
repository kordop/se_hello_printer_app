import unittest
import random
import string
import json

from hello_world.formater import plain_text_upper_case, format_to_json


def string_generator(
    max_str_len: int, number_at_each_len: int,
    printable: str = string.printable
):
    '''
    generator for creating test string
    '''

    index = 0
    while not index > number_at_each_len * max_str_len:
        result = ""
        if index != 0:
            actual_str_len = (index-1) // (number_at_each_len)+1
            for _ in range(actual_str_len):
                result = result + \
                    printable[random.randint(0, len(printable)-1)]
        index = index + 1
        yield(result)


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        msg = r.split(" ")[0]
        name = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_json(self):
        for generated_str in string_generator(10, 10, "abcdfgHJLASKJKN"):
            with self.subTest(msg=generated_str, generated_str=generated_str):             
                formated_json = format_to_json(generated_str, "EFAF")
                generated_json = json.dumps({"imie":"EFAF","msg":str(generated_str)})
                self.assertEqual(formated_json, generated_json)
            
    def test_plain_uppercase_str_iter(self):
        for generated_str in string_generator(10, 10, "abcdfgHJLASKJKN"):
            r = plain_text_upper_case(generated_str, "EEEMSG")
            splited = r.split(" ")
            msg = splited[0]
            name = splited[-1]
            self.assertEqual(name, generated_str.upper())
            self.assertEqual(msg, "EEEMSG".upper())
