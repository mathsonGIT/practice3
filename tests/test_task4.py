import unittest
from task4 import Person



class TestPersonClass(unittest.TestCase):

    def setUp(self):
        self.person = Person('Natalya', 2000, 'Moscow')


    def test_get_age(self):
        '''Проверка правильности возраста'''
        expected_rez = 25
        self.assertEqual(expected_rez, self.person.get_age())

    def test_get_age_value_error(self):
        '''Проверка ошибки типа данных'''
        self.person = Person('Natalya', 'dfdf', 'Moscow')
        with self.assertRaises(TypeError):
            self.person.get_age()

    def test_set_name(self):
        '''Проверка правильности установки имени '''
        self.person.set_name('Masha')
        self.assertEqual('Masha', self.person.get_name())

    def test_set_address(self):
        '''Проверка правильности установки адреса '''
        self.person.set_address('Novgorod')
        self.assertEqual('Novgorod', self.person.get_address())

    def test_is_homeless(self):
        '''Проверка возвращения логического оператора: есть ли адрес '''
        #self.person.set_address('')
        self.assertFalse(self.person.is_homeless())

    def test_is_homeless_true(self):
        '''Проверка возвращения логического оператора: есть ли адрес '''
        self.person.set_address('')
        self.assertTrue(self.person.is_homeless())



    


