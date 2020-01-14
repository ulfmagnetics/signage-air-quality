import time
import unittest
from signage_air_quality.air_quality_packet import AirQualityPacket

class TestAirQualityPacket(unittest.TestCase):

    def test_to_bytes(self):
        now = time.strptime("Mon Jan 13 21:00:00 2020")
        timestamp = int(time.mktime(now))
        packet = AirQualityPacket(56, 'O3', timestamp).to_bytes()
        self.assertEqual(chr(packet[0]) + chr(packet[1]), "!Q")
        self.assertEqual(packet[2], 56) # little-endian
        self.assertEqual(packet[3], 0) # little-endian
        self.assertEqual(chr(packet[4]), "O")

    def test_from_bytes(self):
        bs = b'!Q8\x00O\xa0 \x1d^\xcb'
        packet = AirQualityPacket.from_bytes(bs)
        self.assertEqual(packet.metric, 'O3')
        self.assertEqual(packet.value, 56)
        self.assertEqual(packet.timestamp, 1578967200)

if __name__ == '__main__':
    unittest.main()
