import unittest
import random
import string

from hello_world.formater import plain_text_upper_case

class StringIterator():
   '''
   iterator for creating test string
   '''
   def __init__(self, max_str_len: int, number_at_each_len: int, printable: str=string.printable):
       self._max_str_len = max_str_len
       self._number_at_each_len = number_at_each_len
       self._printable = printable
       self._index = 0

   def __next__(self):
        if self._index > self._number_at_each_len * self._max_str_len:
            # End of Iteration
            raise StopIteration

        result = ""
        if self._index != 0:
            actual_str_len = (self._index-1) // (self._number_at_each_len)+1
            for _ in range(actual_str_len):
                result = result + self._printable[random.randint(0,len(self._printable)-1)]

        self._index = self._index + 1
        return result


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        msg = r.split(" ")[0]
        name = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_uppercase_str_iter(self):
        string_iterator = StringIterator(10,10,)
        while True:
            try:
                generated_str = next(string_iterator)
                r = plain_text_upper_case(generated_str, "EEEMSG")
                splited = r.split(" ")
                msg = splited[0]
                name = splited[-1]
                self.assertEqual(name, generated_str.upper())
                self.assertEqual(msg, "EEEMSG".upper())
            except StopIteration:
                break

