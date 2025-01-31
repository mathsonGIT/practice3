import unittest
from datetime import datetime
from hello_world_with_day import app
from freezegun import freeze_time

#@freeze_time("2025-01-29")
class TestHelloWorldWithDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.base_url='/hello-world/'


    def test_can_get_correct_username(self):
        username = 'username'
        response = self.app.get(self.base_url+username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)


    def test_can_get_correct_username_with_weekdate(self):
        index_day = datetime.today().weekday()
        weekdays = ('понедельник', 'вторник', 'сред', 'четверг', 'пятниц', 'суббот', 'воскресень')
        username = 'Хорошей среды'
        response = self.app.get(self.base_url+username)
        response_text = response.data.decode()
        self.assertTrue(weekdays[index_day] in response_text)


