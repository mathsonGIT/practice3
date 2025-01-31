import unittest
from fin_accouting import app, storage



class TestFinAccountingApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global storage
        storage.update({'2020': {'12': {'20': 10, 'total': 30, '21': 20}, 'total': 30},
                        '2022': {'12': {'21': 30, 'total': 30}, 'total': 30}})


    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.base_url='/'


    def test_can_add_data_with_costs(self):
        cases = ({'case': 'checking year total', 'expected_rez': 300, 'date': '20221225', 'cost': 270},
                 {'case': 'checking year month total', 'expected_rez': 500, 'date': '20221227', 'cost': 200})
        for item in cases:
            with self.subTest(item['case']):
                self.app.get(f'{self.base_url}add/{item['date']}/{item['cost']}')
                self.assertTrue(item['expected_rez'], storage['2022']['total'])


    def test_value_error(self):
        date = 'ttteee13'
        cost = 12
        
        with self.assertRaises(ValueError):
            self.app.get(f'{self.base_url}add/{date}/{cost}')


    def test_can_calculate_year(self):
        year = '2020'
        expected_rez = 30
        response = self.app.get(f'{self.base_url}calculate/{year}')
        self.assertEqual(expected_rez, storage[year]['total'])
        

    def test_can_calculate_year_month(self):
        year = '2020'
        month = '12'
        expected_rez = 30
        response = self.app.get(f'{self.base_url}calculate/{year}/{month}')
        self.assertEqual(expected_rez, storage[year][month]['total'])
        




        



