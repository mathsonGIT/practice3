import unittest
from decrypt import decrypt

#абра-кадабра. → абра-кадабра
#абраа..-кадабра → абра-кадабра
#абраа..-.кадабра → абра-кадабра
#абра--..кадабра → абра-кадабра
#абрау...-кадабра → абра-кадабра
#абра........ → <пустая строка>
#абр......a. → a
#1..2.3 → 23
#. → <пустая строка>
#1....................... → <пустая строка>


class TestDecrypt(unittest.TestCase):


    def test_can_one_point_processing(self):

        cases = ({'case': 'One Points Proccessing', 'expected_rez': 'абра-кадабра', 'function_inputs': 'абра-кадабра.'},
                 {'case': 'Two Points Processing', 'expected_rez': 'абра-кадабра', 'function_inputs': 'абраа..-кадабра'},
                 {'case': 'Mix Points Processing', 'expected_rez': 'абра-кадабра', 'function_inputs': 'абраа..-.кадабра'},
                 {'case': 'Mix Points Processing 2', 'expected_rez': 'абра-кадабра', 'function_inputs': 'абра--..кадабра'},
                 {'case': 'Mix Points Processing 3', 'expected_rez': 'абра-кадабра', 'function_inputs': 'абрау...-кадабра'},
                 {'case': 'Mix Points Processing 4', 'expected_rez': 'a', 'function_inputs': 'абр......a.'},
                 {'case': 'Mix Points Processing 5', 'expected_rez': '23', 'function_inputs': '1..2.3'},
                 {'case': 'Empty string', 'expected_rez': '', 'function_inputs': 'абра........'},
                 {'case': 'Empty string 2', 'expected_rez': '', 'function_inputs': '.'},
                 {'case': 'Empty string 3', 'expected_rez': '', 'function_inputs': '1.......................'}
                 
                 )
        for item in cases:
            with self.subTest(item['case']):
                function_rez = decrypt(item['function_inputs'])
                self.assertEqual(item['expected_rez'], function_rez)
    


