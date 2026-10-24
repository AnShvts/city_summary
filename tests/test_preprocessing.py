import unittest
from processing.preprocessing import add_weather_flags, add_rate_flags

class TestPreprocessing(unittest.TestCase):
    def test_warm_clothes_true(self):
        weather = {'temp_c': -5.0}
        result = add_weather_flags(weather)
        self.assertTrue(result['warm_clothes'])

    def test_warm_clothes_false(self):
        weather = {'temp_c': 10.0}
        result = add_weather_flags(weather)
        self.assertFalse(result['warm_clothes'])

    def test_expensive_true(self):
        rate = {'rate_to_rub': 105.5}
        result = add_rate_flags(rate)
        self.assertTrue(result['expensive'])

    def test_expensive_false(self):
        rate = {'rate_to_rub': 90.0}
        result = add_rate_flags(rate)
        self.assertFalse(result['expensive'])

if __name__ == '__main__':
    unittest.main()
