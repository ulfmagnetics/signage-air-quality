import unittest
from signage_air_quality.aqi import Aqi

class TestAqi(unittest.TestCase):

    def test_levels(self):
        aqi = Aqi()
        self.assertEqual(len(aqi.levels), 6)
        self.assertEqual(aqi.level_at(3).label, 'USG')

    def test_level_for_value(self):
        aqi = Aqi()
        self.assertEqual(aqi.level_for_value(0).label, 'Good')
        self.assertEqual(aqi.level_for_value(250).label, 'Very Unhealthy')
        self.assertRaises(ValueError, aqi.level_for_value, 501)

if __name__ == '__main__':
    unittest.main()
