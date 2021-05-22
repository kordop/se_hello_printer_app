import unittest
import random
import string

from hello_world.formater import plain_text_upper_case


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

    def test_plain_uppercase_str_iter(self):
        for generated_str in string_generator(10, 10, "abcdfgHJLASKJKN"):
            r = plain_text_upper_case(generated_str, "EEEMSG")
            splited = r.split(" ")
            msg = splited[0]
            name = splited[-1]
            self.assertEqual(name, generated_str.upper())
            self.assertEqual(msg, "EEEMSG".upper())
