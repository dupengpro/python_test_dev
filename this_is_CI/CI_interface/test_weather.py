import unittest
import requests


class Weather(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://www.weather.com.cn/data/cityinfo'

    def test_beijing(self):
        city_code = '101020100'
        url = self.base_url + city_code + '.html'
        r = requests.get(url)
        r.encoding = 'utf-8'
        assert r.status_code == 200

    def test_shenzhen(self):
        city_code = '101280601'
        url = self.base_url + city_code + '.html'
        r = requests.get(url)
        r.encoding = 'utf-8'
        assert r.status_code == 200


if __name__ == '__main__':
    unittest.main()





