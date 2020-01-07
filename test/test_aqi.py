import unittest
from signage_air_quality.aqi import Aqi

class TestAqi(unittest.TestCase):

    def test_levels(self):
        aqi = Aqi()
        self.assertEqual(len(aqi.levels), 6)
        self.assertEqual(aqi.level_at(3).label, 'USG')

if __name__ == '__main__':
    unittest.main()
